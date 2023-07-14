function getColumnFormat_Ingredient_3() {         
    var columns;
    
        columns = [
        {readOnly: true },{},{},{},
        {type: 'numeric', numericFormat: { pattern: '0' }, validator: positiveNumberValidator},{type: 'date',},
        {type: 'numeric', numericFormat: { pattern: '0' }, validator: positiveIntegerValidator },
        {type: 'numeric', numericFormat: { pattern: '0' }, validator: positiveIntegerValidator },
        {type: 'numeric', numericFormat: { pattern: '0' }, validator: positiveIntegerValidator },
        {type: 'numeric', numericFormat: { pattern: '0' }, validator: positiveIntegerValidator },
        {type: 'numeric', numericFormat: { pattern: '0' }, validator: positiveIntegerValidator },{},{type: 'date',},
        {type: 'numeric', numericFormat: { pattern: '0' }, validator: positiveNumberValidator},{},{type: 'checkbox'},
        ];
        return columns;
     } 