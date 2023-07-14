function getColumnFormat_Raw_2() {         
    var columns;    
        columns = [
        {readOnly: false },
        {},
        {type: 'numeric', numericFormat: { pattern: '0' }, validator: positiveNumberValidator, allowInvalid: false},
        {type: 'date',},
        {},
        {type: 'date',},
        {type: 'numeric', numericFormat: { pattern: '0' }, validator: percentageValidator},
        {type: 'numeric', numericFormat: { pattern: '0' }, validator: positiveIntegerValidator },
        {type: 'dropdown',source: ['language', 'ide','a','b','c','d','r']},
        {type: 'date',},
        {type: 'numeric', numericFormat: { pattern: '0' }, validator: positiveNumberValidator},
        {},
        {type: 'checkbox'},
        ];
        return columns;
     } 