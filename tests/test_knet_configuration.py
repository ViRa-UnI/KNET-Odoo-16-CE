from odoo.tests.common import TransactionCase

class TestKnetConfiguration(TransactionCase):

    def setUp(self):
        super(TestKnetConfiguration, self).setUp()
        self.KnetConfig = self.env['knet.configuration']

    def test_knet_configuration(self):
        # Create a new KNET configuration
        knet_config = self.KnetConfig.create({
            'merchant_id': 'test_merchant_id',
            'secret_key': 'test_secret_key',
            'sandbox_mode': True,
        })

        # Check if the configuration is created with correct values
        self.assertEqual(knet_config.merchant_id, 'test_merchant_id')
        self.assertEqual(knet_config.secret_key, 'test_secret_key')
        self.assertTrue(knet_config.sandbox_mode)

        # Check if the configuration can be written to
        knet_config.write({
            'sandbox_mode': False,
        })
        self.assertFalse(knet_config.sandbox_mode)

    def test_knet_configuration_unlink(self):
        # Create a new KNET configuration
        knet_config = self.KnetConfig.create({
            'merchant_id': 'test_merchant_id',
            'secret_key': 'test_secret_key',
            'sandbox_mode': True,
        })

        # Unlink the created configuration
        knet_config.unlink()
        # Check if the configuration is deleted
        self.assertFalse(self.KnetConfig.search([('id', '=', knet_config.id)]))