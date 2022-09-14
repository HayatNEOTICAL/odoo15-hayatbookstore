from odoo import api, fields, models


class Konsumen(models.Model):
    _inherit = 'res.partner'
    _description = 'Pelanggan'

    is_direksi = fields.Boolean(string='Dalam Kontrak')
    is_konsumen = fields.Boolean(string='Promo')
    is_pelanggan = fields.Boolean(string='Status : Pelanggan')
    poin = fields.Integer(string='Point')
    level = fields.Char(string='Membership Level')