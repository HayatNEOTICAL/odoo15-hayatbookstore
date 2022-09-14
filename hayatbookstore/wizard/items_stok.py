from odoo import api, fields, models


class Items_Stok(models.Model):
    _name = 'hayatbookstore.items_stok'
    _description = 'New Description'

    items_id = fields.Many2one(comodel_name='hayatbookstore.items', string='Nama Items', required=True)
    
    jumlah = fields.Integer(
        string='jumlah', required=False
    )
    
    def button_items_stok(self):
        for rec in self:
            self.env['hayatbookstore.items'].search([('id', '=', rec.items_id.id)]).write({'stok' : rec.items_id.stok + rec.jumlah})