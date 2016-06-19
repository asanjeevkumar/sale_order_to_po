{ 'sequence': 22,

'name': 'Sale order to purchase order',
'version': '0.5',
'category': 'Sale Management',
'description': """
This module converts the sale order to purchase order.
""",
'author': 'Sanjeev Kumar - sanjeeve.kumar@gmail.com',
'depends': [ 'sale','purchase','account' ,'stock'],
'data': [
  ],
'data':
  [
  'wizards/sale_order_purcharse_order_wiz.xml',
  'views/sale_order.xml',
  ],
'demo_xml': [],
'installable': True,
'active': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: