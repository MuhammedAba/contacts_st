# -*- coding: utf-8 -*-
{
    'name': "STK",

    'summary': """
      STK 
    """,

    'author': "Rasard Tech",
    'website': "https://rasard.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Contacts',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['contacts', 'website', 'base_address_city'],
    
    'sequence': -101,
    'application': True,

    # always loaded
    'data': [
        "security/ir.model.access.csv",
        "data/partner.blood.groups.csv",
        "data/partner.languages.csv",
        "data/partner.driving.license.csv",
        "data/partner.education.status.csv",
        "views/partner_member_types_views.xml",
        "views/partner_view.xml",
        "views/partner_blood_groups.xml",
        "views/partner_education_status_views.xml",
        "views/partner_driving_license_view.xml",
        "views/partner_website_from_view.xml"

    ],

}
