{
    'name': 'Cash on Delivery',
    'version': '1.0',
    'category': 'Payment',
    'summary': 'Enable Cash on Delivery payments',
    'description': """
        Allows customers to place orders without immediate payment
        using Cash on Delivery option.
    """,
    'depends': ['payment', 'website_sale'],
    'data': [
        'views/payment_cod_templates.xml',
        'data/payment_method_data.xml',
        'data/payment_acquirer_data.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}