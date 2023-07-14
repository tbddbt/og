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

def split_sheet_by_empty_row(d):
    split_data = {}
    chunk = {}
    for row in d:
        if any(row):
            chunk.append(row)
        elif chunk:
            split_data.append(chunk)
            #chunk = {}
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

            sheets = filehandle.get_book()
            sheet_names = sheets.sheet_names()
            sheet_data = {}
            
            for name, sheet in zip(sheet_names, sheets):
                sheet.name_columns_by_row(0)
                data = sheet.get_array()
                
                sheet_data[name] = {"sheet_data": [[x[0], x[2]] for x in data[1:]]}
                print(sheet_data)
                #sheet_data_values=sheet_data.keys()
                #print(sheet_data_values)
                
                #print(sheet_data.get('sheet_name'))
                #d=dict(sheet_data_values)
                #print(type(d))
                res = sheet_data.get('Sheet1', {}).get('sheet_data')
                print(res)
                d=dict(res)
                print(type(d))
                #sample_name=sheets.column_at(0)
                #sample_header=sheets.column_at(2)
      
                #print(sample_name)
                #print(sample_header))

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
