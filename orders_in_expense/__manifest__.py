# -*- coding: utf-8 -*-
{
    'name': "Orders in Expenses",
    'summary': 'Adds additional functionality to the Expenses module',
    'description': """
     This module adds a new field to the Expenses module that tracks the status of the payment and confirmation 
        of the delivery receipt    """,
    'author': "webmania",
    'website': "http://www.webmania.ma",
    'category': 'Accounting & Finance',
    'version': '0.1',
    'depends': ['base','sale', 'hr_expense'],
    'data': [
        'views/view_hr_expense.xml',
        'views/view_sale_order.xml',
    ],

}
