from openerp.osv import fields, osv
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp

class sale_advance_purchase_order(osv.osv_memory):
    _name = "sale.advance.purchase.order"
    _description = "Sales Advance Purchase Order"
    _columns = {
        'advance_purchase_order':fields.selection(
            [('all', 'covert the whole sales order'), ('lines', 'Some order lines')],
            'What do you want to Convert to PO?', required=True,
            help="""Use 'Convert the whole sale order'  to convert all the products to purcharse order.""")
        
    }
    
    def _prepare_advance_po_vals(self,uid, ids, context=None):
        pass
    
    def create_purchase_order(self, cr, uid, ids, context=None):
        """ create invoices for the active sales orders """
        sale_obj = self.pool.get('sale.order')
        act_window = self.pool.get('ir.actions.act_window')
        wizard = self.browse(cr, uid, ids[0], context)
        sale_ids = context.get('active_ids', [])
        if wizard.advance_purchase_order == 'all':
            # create the final invoices of the active sales orders
            res = sale_obj.manual_purchase_order(cr, uid, sale_ids, context)
            
            return {'type': 'ir.actions.act_window_close'}

        if wizard.advance_purchase_order == 'lines':
            # open the list view of sales order lines to invoice
            res = act_window.for_xml_id(cr, uid, 'sale', 'action_order_line_tree2', context)
            res['context'] = {
                
                'search_default_order_id': sale_ids and sale_ids[0] or False,
            }
            return res        

        inv_ids = []
        for sale_id, inv_values in self._prepare_advance_po_vals(cr, uid, ids, context=context):
            inv_ids.append(self._create_purchase_order(cr, uid, inv_values, sale_id, context=context))

        
        return {'type': 'ir.actions.act_window_close'}
sale_advance_purchase_order()