from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Penjualan(models.Model):
    _name = 'hayatbookstore.penjualan'
    _description = 'Penjualan'

    name = fields.Char(string='No. Nota')
    nama_pembeli = fields.Many2one(comodel_name='res.partner',string='Nama Pembeli')
    tgl_penjualan = fields.Datetime(string='Tgl. Transaksi', 
                                    default = fields.Datetime.now())
    total_bayar = fields.Integer(compute='_compute_totalbayar', string='Total Pembayaran')
    detailpenjualan_ids = fields.One2many(comodel_name='hayatbookstore.detailpenjualan', 
                                          inverse_name='penjualan_id', 
                                          string='Detail Penjualan')
    state = fields.Selection(string = 'Status', 
            selection=[('draft','Draft'),('confirm','Confirm'),('done','Done'),('cancelled','Cancelled')],
            required=True, readonly=True, default='draft')

    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancelled(self):
        self.write({'state': 'cancelled'})                

    def action_draft(self):
        self.write({'state': 'draft'})

    @api.depends('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for rec in self:
            a = sum(self.env['hayatbookstore.detailpenjualan'].search([('penjualan_id', '=', rec.id)]).mapped('subtotal'))
            rec.total_bayar = a                                  

    @api.depends('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for rec in self:
            a = sum(self.env['hayatbookstore.detailpenjualan'].search([('penjualan_id', '=', rec.id)]).mapped('subtotal'))
            rec.total_bayar = a

    def unlink(self):
        if self.filtered(lambda line: line.state != 'draft'):
            raise ValidationError("Tidak Dapat Menghapus Jika Status Bukan Draft")
        else:
            if self.detailpenjualan_ids:
                a=[]
                for rec in self:
                    a = self.env['hayatbookstore.detailpenjualan'].search([('penjualan_id','=',rec.id)])
                    print(a)
                for ob in a:
                    print(str(ob.items_id.name) + ' ' + str(ob.qty))
                    ob.items_id.stok += ob.qty
            record = super(Penjualan, self).unlink()

    def write(self,vals):
        for rec in self:
            a = self.env['hayatbookstore.detailpenjualan'].search([('penjualan_id','=',rec.id)])
            print(a)
            for data in a:
                print(str(data.items_id.name)+' '+str(data.qty)+' '+str(data.items_id.stok))
                data.items_id.stok += data.qty
        record = super(Penjualan,self).write(vals)
        for rec in self:
            b = self.env['hayatbookstore.detailpenjualan'].search([('penjualan_id','=',rec.id)])
            print(a)
            print(b)
            for newdata in b:
                if newdata in a:
                    print(str(newdata.items_id.name)+' '+str(newdata.qty)+' '+str(newdata.items_id.stok))
                    newdata.items_id.stok -= newdata.qty
                else:
                    pass    
        return record

    _sql_constraints = [
        ('no_nota_unik','unique (name)','Nomor Nota Tidak Boleh Sama!')
    ]     

class DetailPenjualan(models.Model):
    _name = 'hayatbookstore.detailpenjualan'
    _description = 'Detail Penjualan'

    name = fields.Char(string='Nama')
    penjualan_id = fields.Many2one(comodel_name='hayatbookstore.penjualan', 
                                string='Detail Penjualan',)
    items_id = fields.Many2one(comodel_name='hayatbookstore.items', 
                                string='List Item')
    harga_satuan = fields.Integer(string='Harga Satuan')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')

    @api.depends('harga_satuan', 'qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.qty * rec.harga_satuan

    @api.onchange('items_id')
    def onchange_items_id(self):
        if (self.items_id.harga_jual):
            self.harga_satuan = self.items_id.harga_jual        

    @api.model
    def create(self,vals):
        record = super(DetailPenjualan,self).create(vals)
        if record.qty:
            self.env['hayatbookstore.items'].search([('id','=',record.items_id.id)]).write({'stok' : record.items_id.stok - record.qty})
        return record

    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
            if rec.qty <1:
                raise ValidationError("Mau Belanja {} berapa banyak sih...".format(rec.items_id.name))
            elif (rec.items_id.stok < rec.qty):
                raise ValidationError('Stok {} tidak mencukupi, hanya tersedia {}'.format(rec.items_id.name,rec.items_id.stok))            