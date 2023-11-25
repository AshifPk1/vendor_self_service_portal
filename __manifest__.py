# -*- coding: utf-8 -*-

{
    'name': 'Vendor Self-Service Portal',
    'version': '16.0.1.0.0',
    "sequence": '16',
    'complexity': "easy",
    'license': 'LGPL-3',
    'description': """
    * Vendor Can See Upcoming Demand For Next Quarter.
    * Vendor Can Submit Adjustment Request
    """,
    'author': 'Ashif',
    'depends': ['base', 'sale'],
    'data': [
        'security/security.xml',
        'data/mail_template.xml',
        'security/ir.model.access.csv',
        'views/vendor_forecast_view.xml',
        'views/vendor_adjustment_request.xml',
        'views/menu.xml'

    ],

    'installable': True,
    'auto_install': False,
}
