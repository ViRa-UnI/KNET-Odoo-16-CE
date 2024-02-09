from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestKNETIntegration(TransactionCase):

    def setUp(self):
        super(TestKNETIntegration, self).setUp()
        # Setup test data
        self.KnetConfig = self.env['knet.configuration'].create({
            'merchant_id': 'test_merchant',
            'secret_key': 'test_secret',
            'sandbox_mode': True,
        })
        self.PaymentTransaction = self.env['payment.transaction']

    def test_knet_integration(self):
        # Test KNET Payment Gateway integration
        transaction_values = {
            'amount': 100.0,
            'currency_id': self.env.ref('base.USD').id,
            'acquirer_id': self.env.ref('payment.payment_acquirer_knet').id,
            'partner_id': self.env.ref('base.res_partner_2').id,
            'reference': 'test_ref_001',
        }
        transaction = self.PaymentTransaction.create(transaction_values)
        # Simulate transaction processing
        transaction.form_feedback({
            'transaction_id': transaction.reference,
            'payment_status': 'done',
        }, 'knet')
        # Check if transaction is processed successfully
        self.assertEqual(transaction.state, 'done', 'Transaction was not processed successfully.')

    def test_knet_integration_failure(self):
        # Test KNET Payment Gateway integration failure
        transaction_values = {
            'amount': 100.0,
            'currency_id': self.env.ref('base.USD').id,
            'acquirer_id': self.env.ref('payment.payment_acquirer_knet').id,
            'partner_id': self.env.ref('base.res_partner_2').id,
            'reference': 'test_ref_002',
        }
        transaction = self.PaymentTransaction.create(transaction_values)
        # Simulate transaction failure
        with self.assertRaises(ValidationError):
            transaction.form_feedback({
                'transaction_id': transaction.reference,
                'payment_status': 'error',
            }, 'knet')
        # Check if transaction is marked as failed
        self.assertEqual(transaction.state, 'error', 'Transaction failure was not handled properly.')