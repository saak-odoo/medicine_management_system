# -*- coding: utf-8 -*-
{
    'name': "Medicine_Management_Sysytem",
    'summary': "Medicine Management System",
    'author': "Aman Kumar Sah",
    'website': "https://www.odoo.com",
    'category': 'medicine management/System',
    'version': '1.0',
    'depends': ['base'],


    'data': [
        'security/ir.model.access.csv',
        'views/medicine_menu_list_view.xml',
        'views/medicine_menu_view.xml',
        'views/medicine_management_view.xml',
        'views/medicine_symptoms-view.xml',
        'views/medicine_offer_view.xml',
        'views/medicine_block_view.xml',
    ],

}


