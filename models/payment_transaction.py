from odoo import models, fields, api

class PaymentTransaction(models.Model):
    _name = 'payment.transaction'
    _description = 'Payment Transaction'

    transaction_id = fields.Char(string='Transaction ID', required=True, readonly=True, index=True)
    payment_status = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
        ('error', 'Error')
    ], string='Payment Status', default='draft', readonly=True)
    amount = fields.Monetary(string='Amount', required=True, readonly=True)
    transaction_date = fields.Datetime(string='Transaction Date', readonly=True)
    currency_id = fields.Many2one('res.currency', string='Currency', required=True, readonly=True)
    partner_id = fields.Many2one('res.partner', string='Customer', readonly=True)
    acquirer_id = fields.Many2one('payment.acquirer', string='Payment Acquirer', readonly=True)
    knet_txn_reference = fields.Char(string='KNET Transaction Reference', readonly=True)

    @api.model
    def create(self, vals):
        # Custom logic for creating a payment transaction
        # This can include calling external APIs or adding additional processing
        record = super(PaymentTransaction, self).create(vals)
        return record

    def action_set_to_done(self):
        self.write({'payment_status': 'done'})

    def action_cancel(self):
        self.write({'payment_status': 'cancel'})

    def action_set_to_error(self):
        self.write({'payment_status': 'error'})