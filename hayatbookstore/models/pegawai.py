from odoo import api, fields, models


class Pegawai(models.Model):
    _name = 'hayatbookstore.pegawai'
    _description = 'Pegawai'
    _rec_name = 'nama_pegawai'

    name = fields.Char(string='ID Pegawai')
    nama_pegawai = fields.Char(string='Nama Pegawai')
    tgl_lahir_pegawai = fields.Date(string="Tanggal Lahir")
    alamat_pegawai = fields.Char(string = "Alamat")
    jenis_kelamin_pegawai = fields.Selection([('Laki-Laki', 'Laki - Laki'),('Perempuan','perempuan')], string="Jenis Kelamin")

class Kasir(models.Model):
    _name = 'hayatbookstore.kasir'
    _inherit = 'hayatbookstore.pegawai'
    _description = "Kasir"
    id_kasir =  fields.Char(String='ID Kasir')
    picture_kasir = fields.Image(string='foto')

    _sql_constraints = [
        ('no_id_kasir_unik','unique (id_kasir)','Ups, ID sudah terdaftar, silahkan gunakan ID lain')
    ]

class OfficeBoy(models.Model):
    _name = 'hayatbookstore.officeboy'    
    _inherit = 'hayatbookstore.pegawai'
    _description = "Office Boy"
    id_officeboy =  fields.Char(String='ID Kasir')
    picture_officeboy = fields.Image(string='foto')

    _sql_constraints = [
        ('no_id_officeboy_unik','unique (id_officeboy)','Ups, ID sudah terdaftar, silahkan gunakan ID lain')
    ]