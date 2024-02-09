{
    'name': 'KNET Payment Integration',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Integrate KNET Payment Gateway with Odoo',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'depends': ['payment'],
    'data': [
        'security/ir.model.access.csv',
        'views/payment_transaction_dashboard.xml',
        'views/knet_configuration_form.xml',
        'data/payment_acquirer_data.xml',
    ],
    'demo': [],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'assets': {
        'web.assets_frontend': [
            'static/src/js/payment_form.js',
            'static/src/css/payment_form.css',
        ],
        'web.assets_qweb': [
            'static/src/xml/*.xml',
        ],
    },
    'images': ['static/src/img/knet_logo.png'],
    'test': [
        'tests/test_payment_transaction.py',
        'tests/test_knet_configuration.py',
        'tests/test_integration.py',
    ],
    'maintainer': 'Your Company',
    'support': 'support@yourcompany.com',
}