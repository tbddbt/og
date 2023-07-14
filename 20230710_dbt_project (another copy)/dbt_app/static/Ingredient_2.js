function getColumnFormat_Ingredient_2() {         
    var columns;
    
        columns = [
        {readOnly: true },{},
        {type: 'numeric', numericFormat: { pattern: '0' }, validator: positiveNumberValidator},{type: 'date',},{},{type: 'date',},
        {type: 'numeric', numericFormat: { pattern: '0' }, validator: positiveNumberValidator},
        {type: 'numeric', numericFormat: { pattern: '0' }, validator: positiveNumberValidator},
        {type: 'numeric', numericFormat: { pattern: '0' }, validator: positiveIntegerValidator},{},{type: 'date',},
        {type: 'numeric', numericFormat: { pattern: '0' }, validator: positiveNumberValidator},{},{type: 'checkbox'},
        ];
        return columns;
     } 