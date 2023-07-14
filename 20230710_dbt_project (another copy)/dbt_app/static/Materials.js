function getColumnFormat_Materials() {         
    var columns;
    
        columns = [
        {readOnly: true },{},{},
        {type: 'numeric', numericFormat: { pattern: '0' }, validator: positiveIntegerValidator },{},{type: 'date',},{},{type: 'date',},
        {type: 'numeric', numericFormat: { pattern: '0' }, validator: positiveIntegerValidator },{},{type: 'date',},
        {type: 'numeric', numericFormat: { pattern: '0' }, validator: positiveIntegerValidator },{},{type: 'checkbox'},
        ];
        return columns;
     } 