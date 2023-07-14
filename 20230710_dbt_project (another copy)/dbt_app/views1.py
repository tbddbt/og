from django import forms
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pyexcel
import json
import numpy as np

filename = None

class UploadFileForm(forms.Form):
    file = forms.FileField()


import pyexcel
import json

def split_sheet_by_empty_row(resultList):
    split_data = []
    chunk = []
    for row in resultList:
        if any(row):
            chunk.append(row)
        elif chunk:
            split_data.append(chunk)
            #chunk = []
    if chunk:
        split_data.append(chunk)
    return split_data
    
@csrf_exempt
def save(request):
    global filename
    sheet_name = request.POST['name']
    json_data = request.POST['json_data']
    y = json.loads(json_data)
    data = y['hot_data']
    header = y['header']
    data.insert(0, header)
    
    book = pyexcel.get_book(file_name=filename)
    new_book = pyexcel.Book()   # Creates a new book 
    for sheet in book:
        if sheet.name == sheet_name:
            split_data = split_sheet_by_empty_row(data)
            for chunk in split_data:
                new_sheet = pyexcel.Sheet(chunk)
                new_sheet.name_columns_by_row(0)
                new_sheet.column.format("Lock", str)
                new_sheet.name = sheet_name
                new_book += new_sheet 
        else:
            new_book += sheet
    
    new_book.save_as(filename)

    return JsonResponse({'response': 'success'})


def upload(request):
    global filename, sheet_data

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            filehandle = request.FILES["file"]
            filename = './store/' + str(filehandle)
            index = 1
            sheets = filehandle.get_sheet()
            
            #sheet_names = sheets.sheet_names()
            sheet_data = {}
            
            #for sheet in sheets:
                #sheet.name_columns_by_row(0)
            data = sheets.get_array()
            print(data)
            print(sheets)
            print(type(sheets))

                #sheet_data[name] = {"sheet_name": name, "sheet_data": [[x[0], x[2]] for x in data[1:]], "header": [data[0][0], data[0][2] ]}
            sheet_data = {"sheet_name": name, "sheet_data": [[x[0], x[2]] for x in data[1:]], "header": [data[0][0], data[0][2] ]}
                
            sample_name=sheets.column_at(0)
            sample_header=sheets.column_at(2)
  
            #print(type(sample_name))
            #print(type(sample_header))
            resultList = list(sheet_data.items())
            print(type(resultList))

            return render(
                request,
                "dbt_app/handsontable.html",
                {"data": sheet_data}
            )

    else:
        form = UploadFileForm()

    return render(
        request,
        "dbt_app/upload_form.html",
        {
            "form": form,
            "title": "Excel file upload and download example",
            "header": "Please choose any excel file from your cloned repository:",
        },
    )
