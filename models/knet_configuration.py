from odoo import models, fields

class KnetConfiguration(models.Model):
    _name = 'knet.configuration'
    _description = 'KNET Payment Gateway Configuration'

    merchant_id = fields.Char(string='Merchant ID', required=True, help='The Merchant ID provided by KNET.')
    secret_key = fields.Char(string='Secret Key', required=True, help='The Secret Key provided by KNET for secure transactions.')
    sandbox_mode = fields.Boolean(string='Sandbox Mode', default=True, help='Enable sandbox mode for testing purposes before going live.')