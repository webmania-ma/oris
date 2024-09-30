# -*- coding: utf-8 -*-
{
    'name': "Sales Margin Analysis with Expense Integration",
    'description': """
        This module is ideal for businesses looking to have a more complete view of their sales profitability while taking into account associated expenses. It bridges the gap between sales and expense management, providing a more accurate picture of the true margin of each sale.
    """,
    'author': "WEBMANIA",
    'website': "www.webmania.ma",
    'category': 'Sale',
    'version': '0.1',
    'depends': ['base', 'sale', 'sale_margin', 'hr_expense', 'orders_in_expense'],
    'data': [
        'security/group.xml',
        'views/view_res_config_settings.xml',
        'views/view_sale_order.xml',
        'views/view_tree_order.xml',
        'data/server_actions.xml',
    ],
}
