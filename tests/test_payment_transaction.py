from odoo.tests.common import TransactionCase

class TestPaymentTransaction(TransactionCase):

    def setUp(self):
        super(TestPaymentTransaction, self).setUp()
        self.payment_transaction_model = self.env['payment.transaction']
        self.knet_configuration_model = self.env['knet.configuration']
        # Setup a dummy KNET configuration
        self.knet_configuration = self.knet_configuration_model.create({
            'merchant_id': 'dummy_merchant_id',
            'secret_key': 'dummy_secret_key',
            'sandbox_mode': True,
        })

    def test_payment_transaction_creation(self):
        # Create a dummy payment transaction
        payment_transaction = self.payment_transaction_model.create({
            'transaction_id': 'test123',
            'payment_status': 'pending',
            'amount': 100.0,
            'transaction_date': '2024-02-10',
        })
        self.assertTrue(payment_transaction, "Payment transaction should be created.")

    def test_payment_transaction_fields(self):
        # Create a dummy payment transaction
        payment_transaction = self.payment_transaction_model.create({
            'transaction_id': 'test123',
            'payment_status': 'pending',
            'amount': 100.0,
            'transaction_date': '2024-02-10',
        })
        # Check if the fields are correctly set
        self.assertEqual(payment_transaction.transaction_id, 'test123', "Transaction ID should match.")
        self.assertEqual(payment_transaction.payment_status, 'pending', "Payment status should be 'pending'.")
        self.assertEqual(payment_transaction.amount, 100.0, "Amount should be 100.0.")
        self.assertEqual(payment_transaction.transaction_date, '2024-02-10', "Transaction date should match.")

    def test_payment_status_update(self):
        # Create a dummy payment transaction
        payment_transaction = self.payment_transaction_model.create({
            'transaction_id': 'test123',
            'payment_status': 'pending',
            'amount': 100.0,
            'transaction_date': '2024-02-10',
        })
        # Update the payment status
        payment_transaction.write({'payment_status': 'done'})
        self.assertEqual(payment_transaction.payment_status, 'done', "Payment status should be updated to 'done'.")

    def tearDown(self):
        # Clean up after tests
        self.payment_transaction_model.search([]).unlink()
        self.knet_configuration_model.search([]).unlink()
        super(TestPaymentTransaction, self).tearDown()