from odoo import api, fields, models


class items(models.Model):
    _name = 'hayatbookstore.items'
    _description = 'Daftar Items'

    name = fields.Char(string='Judul Buku')
    penulis = fields.Char(string='Penulis')
    publisher = fields.Char(string='Publisher')
    tgl_terbit = fields.Date(string='Tanggal Terbit')
    harga_beli = fields.Integer(string='Harga Modal',required=True)
    harga_jual = fields.Integer(string='Harga Jual',required=True)
    detail_items_id = fields.Many2one(comodel_name='hayatbookstore.detail_items', 
                                        string='Jenis Buku', 
                                        ondelete='cascade')
    mitra_id = fields.Many2many(comodel_name='hayatbookstore.mitra', string='mitra')
    stok = fields.Integer(string='Stok')
    picture = fields.Image(string='Cover Buku')