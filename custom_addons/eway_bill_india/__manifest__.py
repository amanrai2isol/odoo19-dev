{
    'name': 'Indian E-Way Bill Integration',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Configure GST API Credentials for E-Way Bills',
    'depends': ['account', 'stock'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}