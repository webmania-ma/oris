# -*- coding: utf-8 -*-
{
    'name': "Show orders in Expenses",

    'summary': 'Adds additional functionality to the Expenses module',

    'description': """
     This module adds a new field to the Expenses module that tracks the status of the payment and confirmation 
        of the delivery receipt    """,
    'author': "WEBMANIA",

    'website': "http://www.webmania.ma",

    'category': 'Accounting & Finance',

    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale', 'hr_expense'],

    'data': [
        'views/checkbox_paye.xml',
        'views/view_inherit_depenses.xml',
    ],

}
