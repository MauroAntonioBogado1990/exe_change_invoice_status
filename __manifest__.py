{
    'name': 'Exe Change Invoice Status',
    'version': '17.0',
    'category': 'Tools',
    'author':'Mauro Bogado,Exemax',
    'summary': 'Modulo para poder cambiar el estado de las facturas desde la orden de venta y compra',
    'depends': ['base','sale', 'account', 'mail', 'stock'],
    'data': [
        'views/sale_order.xml',
        'views/purchase_order.xml',
    ],
    
    'installable': True,
    'application': False,
}   