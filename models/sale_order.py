# -- coding: utf-8 --
from openerp import models, fields, api, _
from openerp.osv import osv

import logging
from datetime import datetime

_logger = logging.getLogger()
class sale_order(models.Model):
    _inherit = 'sale.order'
    
    def action_convert_to_purchase_order(self, cr, uid, ids, context=None):
        pass
    
sale_order()