function getColumnFormat_Stage_11() {         
    var columns;
    
        columns = [
        {readOnly: true },{type: 'date',readOnly: true },{readOnly: true },{readOnly: true },{readOnly: true },{readOnly: true },{readOnly: true },{readOnly: true },{type: 'date',},{},{},
        {type: 'numeric', numericFormat: { pattern: '0' }, validator: positiveNumberValidator},{},{},{type: 'date',},{},{},{type: 'checkbox'},
        ];
        return columns;
     } 