from odoo import http
from odoo.http import request

class KnetPaymentController(http.Controller):

    @http.route('/payment/knet/transaction', type='json', auth='public', methods=['POST'], csrf=False)
    def knet_payment_transaction(self, **post):
        # Process the payment transaction
        transaction = request.env['payment.transaction'].sudo().create({
            'transaction_id': post.get('transaction_id'),
            'amount': post.get('amount'),
            'transaction_date': fields.Date.today(),
            'payment_status': 'pending'
        })
        # Additional logic to handle the transaction can be added here
        return {
            'success': True,
            'transaction_id': transaction.transaction_id,
            'message': 'Transaction has been created successfully.'
        }

    @http.route('/payment/knet/feedback', type='http', auth='public', methods=['POST'], csrf=False)
    def knet_payment_feedback(self, **post):
        # Handle the feedback from KNET after payment processing
        transaction_id = post.get('transaction_id')
        payment_status = post.get('payment_status')
        transaction = request.env['payment.transaction'].sudo().search([('transaction_id', '=', transaction_id)])
        if transaction:
            transaction.sudo().write({
                'payment_status': payment_status
            })
            # Additional logic for post-payment processing can be added here
            return request.render('payment_knet.payment_confirmation_template', {
                'transaction_id': transaction_id,
                'payment_status': payment_status
            })
        else:
            return request.render('payment_knet.payment_error_template', {
                'error_message': 'Transaction not found.'
            })