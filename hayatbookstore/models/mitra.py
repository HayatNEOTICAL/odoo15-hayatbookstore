from odoo import api, fields, models


class ModuleName(models.Model):
    _name = 'hayatbookstore.mitra'
    _description = 'Mitra'

    name = fields.Char(string='Nama Perusahaan')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No Telepon')
    items_id = fields.Many2many(comodel_name='hayatbookstore.items', string='Items')
    picture_mitra = fields.Image(string='Logo Perusahaan')