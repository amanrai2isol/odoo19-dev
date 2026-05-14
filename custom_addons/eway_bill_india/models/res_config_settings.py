from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    ewaybill_gstin = fields.Char(string="Company GSTIN", config_parameter='eway_bill_india.ewaybill_gstin')
    ewaybill_username = fields.Char(string="E-Way Bill API Username", config_parameter='eway_bill_india.ewaybill_username')
    ewaybill_password = fields.Char(string="E-Way Bill API Password", config_parameter='eway_bill_india.ewaybill_password')
    ewaybill_client_id = fields.Char(string="E-Way Bill Client ID", config_parameter='eway_bill_india.ewaybill_client_id')
    ewaybill_client_secret = fields.Char(string="E-Way Bill Client Secret", config_parameter='eway_bill_india.ewaybill_client_secret')

    ewaybill_environment = fields.Selection([
        ('sandbox', 'Testing (Sandbox)'),
        ('production', 'Live (Production)')
    ], string="E-Way Bill Environment", default='sandbox', config_parameter='eway_bill_india.ewaybill_environment')