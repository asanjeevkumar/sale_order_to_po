# -- coding: utf-8 --
from openerp import models, fields, api, _
from openerp.osv import osv

import logging
from datetime import datetime

_logger = logging.getLogger()
class sale_order(models.Model):
    _inherit = 'sale.order'
    purchase_ids = fields.Many2many('purchase.order', 'sale_order_purchase_order_rel', 'purchase_order_id', 'sale_order_id', 'Purchase Orders'),
    def manual_purchase_order(self, cr, uid, ids, context=None):
        mod_obj = self.pool.get('ir.model.data')
        
        # create invoices through the sales orders' workflow
        inv_ids0 = set(inv.id for sale in self.browse(cr, uid, ids, context) for inv in sale.purchase_ids)
        self.signal_workflow(cr, uid, ids, 'manual_invoice')
        inv_ids1 = set(inv.id for sale in self.browse(cr, uid, ids, context) for inv in sale.purchase_ids)
        # determine newly created invoices
        new_inv_ids = list(inv_ids1 - inv_ids0)

        res = mod_obj.get_object_reference(cr, uid, 'purchase_order', 'purchase_order_form')
        res_id = res and res[1] or False,

        return {
            'name': _('Purchase Order'),
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': [res_id],
            'res_model': 'purchase.order',
            'context': "{'type':'so_to_po'}",
            'type': 'ir.actions.act_window',
            'nodestroy': True,
            'target': 'current',
            'res_id': new_inv_ids and new_inv_ids[0] or False,
        }
    
sale_order()