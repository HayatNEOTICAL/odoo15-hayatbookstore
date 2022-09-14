from odoo import api, fields, models


class detail_items(models.Model):
    _name = 'hayatbookstore.detail_items'
    _description = 'New Description'

    name = fields.Selection([
        ('novel', 'Novel'), ('karya_ilmiah', 'Karya Ilmiah'),('science','Ilmu Pengetahuan'),('majalah','Majalah'),('komik','Komik')
    ], string='Jenis Buku')
    kode_buku = fields.Char(string='Kode Buku')

    @api.onchange('name')
    def _onchange_kode_kelompok(self):
        if (self.name=='novel'):
            self.kode_buku = 'BN001'
        elif (self.name == 'karya_ilmiah'):
            self.kode_buku = 'BKI001'        
        elif (self.name == 'science'):
            self.kode_buku ='BSC001'
        elif (self.name == 'komik'):
            self.kode_buku = 'BK001' 
        elif (self.name == 'majalah'):
            self.kode_buku = 'BM001'    


    kode_rak = fields.Char(string='Kode Rak')
    items_ids = fields.One2many(comodel_name='hayatbookstore.items', inverse_name='detail_items_id', string='Daftar Items') 
    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Item')
    daftar = fields.Char(string = 'Daftar Isi')

    @api.depends('items_ids')
    def _compute_jml_item(self):
        for rec in self:
            a = self.env['hayatbookstore.items'].search([('detail_items_id','=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
            rec.daftar = a        

      