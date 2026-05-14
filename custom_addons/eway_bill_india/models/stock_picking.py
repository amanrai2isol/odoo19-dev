from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # These fields store the transport info
    l10n_in_distance = fields.Integer(string="Distance (km)")
    l10n_in_mode = fields.Selection([
        ('1', 'Road'),
        ('2', 'Rail'),
        ('3', 'Air'),
        ('4', 'Ship')
    ], string="Transp. Mode", default='1')
    l10n_in_vehicle_no = fields.Char(string="Vehicle Number")
    eway_bill_no = fields.Char(string="E-Way Bill No.", readonly=True, copy=False)

    def action_generate_ewaybill(self):
        # 1. Initialize the API service
        api_service = self.env['ewaybill.api.service']

        # 2. Generate the JSON data
        json_data = api_service.prepare_ewaybill_json(self)

        # 3. For testing, let's print the JSON to the log
        print("--- DEBUG E-WAY BILL JSON ---")
        print(json_data)

        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'JSON Generated! Check your terminal log.',
                'type': 'rainbow_man',
            }
        }