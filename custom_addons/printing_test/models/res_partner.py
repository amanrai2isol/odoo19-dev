from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    priority_level = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string='Customer Priority', default='low')