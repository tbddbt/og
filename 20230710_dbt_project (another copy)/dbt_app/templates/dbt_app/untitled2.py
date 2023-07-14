{% load static %}
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Handsontable Example</title>
    <link rel="stylesheet" href="{% static 'handsontable/handsontable.full.min.css' %}">
    <script src="{% static 'handsontable/handsontable.full.min.js' %}"></script>
    <script src="{% static 'utility.js' %}"></script>
    <script src="{% static 'Raw_1.js' %}"></script>
    <script src="{% static 'Raw_2.js' %}"></script>
    <script src="{% static 'Ingredient_1.js' %}"></script>
    <script src="{% static 'Ingredient_2.js' %}"></script>
    <script src="{% static 'Ingredient_3.js' %}"></script>
    <script src="{% static 'Materials.js' %}"></script>
    <script src="{% static 'Stage_1.js' %}"></script>
    <script src="{% static 'Stage_2.js' %}"></script>
    <script src="{% static 'Stage_3.js' %}"></script>
    <script src="{% static 'Stage_4.js' %}"></script>
    <script src="{% static 'Stage_5.js' %}"></script>
    <script src="{% static 'Stage_6.js' %}"></script>
    <script src="{% static 'Stage_7.js' %}"></script>
    <script src="{% static 'Stage_8.js' %}"></script>
    <script src="{% static 'Stage_9.js' %}"></script>
    <script src="{% static 'Stage_10.js' %}"></script>
    <script src="{% static 'Stage_11.js' %}"></script>
    <script src="{% static 'Stage_12.js' %}"></script>
    <script src="{% static 'Stage_13.js' %}"></script>
    <script src="{% static 'Stage_14.js' %}"></script>
    <script src="{% static 'Stage_15.js' %}"></script>
    <script src="{% static 'Stage_16.js' %}"></script>
    <script src="{% static 'jquery.min.js' %}"></script>
    
    <script>
        
        function save_data(data){
            let title_container = document.getElementById("handsontable-container-title");
            let current_sheet = title_container.value
            console.log(current_sheet)
            
            let data_container = document.getElementById("handsontable-container-data");
            
            console.log(data[current_sheet])
            console.log(data_container)
        }
              
       	
        function showHandsontable(sheet) {
            let data_container = document.getElementById("handsontable-container-data");
            data_container.innerHTML = "";
            
            var columns;
            if (sheet.sheet_name == 'Raw_1') 
            {
                columns = getColumnFormat_Raw_1()
            } 
            else if(sheet.sheet_name == 'Raw_2') 
            {
                columns = getColumnFormat_Raw_2()
            }
            else if(sheet.sheet_name == 'Ingredient_1') 
            {
                columns = getColumnFormat_Ingredient_1()
            }
            else if(sheet.sheet_name == 'Ingredient_2') 
            {
                columns = getColumnFormat_Ingredient_2()
            }
            else if(sheet.sheet_name == 'Ingredient_3') 
            {
                columns = getColumnFormat_Ingredient_3()
            }
            else if(sheet.sheet_name == 'Materials') 
            {
                columns = getColumnFormat_Materials()
            }
            else if(sheet.sheet_name == 'Stage_1') 
            {
                columns = getColumnFormat_Stage_1()
            }
            else if(sheet.sheet_name == 'Stage_2') 
            {
                columns = getColumnFormat_Stage_2()
            }
            else if(sheet.sheet_name == 'Stage_3') 
            {
                columns = getColumnFormat_Stage_3()
            }
            else if(sheet.sheet_name == 'Stage_4') 
            {
                columns = getColumnFormat_Stage_4()
            }
            else if(sheet.sheet_name == 'Stage_5') 
            {
                columns = getColumnFormat_Stage_5()
            }
            else if(sheet.sheet_name == 'Stage_6') 
            {
                columns = getColumnFormat_Stage_6()
            }
            else if(sheet.sheet_name == 'Stage _7') 
            {
                columns = getColumnFormat_Stage_7()
            }
            else if(sheet.sheet_name == 'Stage _8') 
            {
                columns = getColumnFormat_Stage_8()
            }
            else if(sheet.sheet_name == 'Stage _9') 
            {
                columns = getColumnFormat_Stage_9()
            }
            else if(sheet.sheet_name == 'Stage _10') 
            {
                columns = getColumnFormat_Stage_10()
            }
            else if(sheet.sheet_name == 'Stage _11') 
            {
                columns = getColumnFormat_Stage_11()
            }
            else if(sheet.sheet_name == 'Stage _12') 
            {
                columns = getColumnFormat_Stage_12()
            }
            else if(sheet.sheet_name == 'Stage _13') 
            {
                columns = getColumnFormat_Stage_13()
            }
            else if(sheet.sheet_name == 'Stage _14') 
            {
                columns = getColumnFormat_Stage_14()
            }
            else if(sheet.sheet_name == 'Stage _15') 
            {
                columns = getColumnFormat_Stage_15()
            }
            else //(sheet.sheet_name == 'Stage _16') 
            {
                columns = getColumnFormat_Stage_16()
            }
            	    
            var hot = new Handsontable(data_container, {
                                    data: sheet.sheet_data,
                                    width: '100%',
                                    height: 320,
                                    rowHeaders: true,
                                    colHeaders: sheet.header,
                                    contextMenu: true,
                                    licenseKey: 'non-commercial-and-evaluation',
                                    columns: columns,	
                                    fixedColumnsStart: 4,
                                    fixedRowsStart: 1,
                                    manualRowMove: true,
                                  
                                    });

	     
            let title_container = document.getElementById("handsontable-container-title");
            title_container.hidden = false;
            title_container.value = sheet.sheet_name;
            
            const download_file = document.getElementById("download_file")
            const exportPlugin = hot.getPlugin('exportFile');            
            download_file.addEventListener('click', () => {
              exportPlugin.downloadFile('csv', {
                bom: false,
                columnDelimiter: ',',
                columnHeaders: true,
                exportHiddenColumns: true,
                exportHiddenRows: true,
                fileExtension: 'xls',
                filename: 'Handsontable-CSV-file_[YYYY]-[MM]-[DD]',
                mimeType: 'text/csv',
                rowDelimiter: '\r\n',
                rowHeaders: true
              });
            });
            

            const save_file = document.getElementById("save_file");
			save_file.addEventListener('click', () => {
    			
    		  var retval = false;
              hot.validateCells((valid) => {
    			console.log('inside callback: ' + valid)
                retval = valid;
              });
              console.log(retval)
            
			  $.ajax({
				type: "POST",
				url: "/save",
				data: {
				  name: sheet.sheet_name,
				  json_data: JSON.stringify({ header: sheet.header, hot_data: hot.getData() })
				},
				success: function (data) {
				  if (data.valid) {
					console.log("Saved Data");
				  } else {
					alert("ERROR: Invalid data present. Please correct the data before saving.");
				  }
				},
				

			  });
			});

        }
    </script>
</head>
<body>
    <ul>
        {% for key, item in data.items %}            
            <li><a href="#" onclick="showHandsontable(  {{ item }})"> {{key}}</a></li>            
        {% endfor %}
    </ul>
	<input type="text" id="handsontable-container-title" hidden readonly><br><br>
	<div id="handsontable-container-data"></div>
	
    	<button id="download_file">Download</button>
	<button id="save_file">Save</button>
</body>
</html>


