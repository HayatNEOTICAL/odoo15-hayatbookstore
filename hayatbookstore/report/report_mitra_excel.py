from dataclasses import fields
from odoo import models, fields

class MitraXlsx(models.AbstractModel):
    _name = 'report.hayatbookstore.report_mitra_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, mitra):
        sheet = workbook.add_worksheet('Daftar Mitra')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap), bold)   
        sheet.write(1, 0, 'Nama Perusahaan', bold)
        sheet.write(1, 1, 'Alamat', bold)
        sheet.write(1, 2, 'No. Telepon', bold)
        sheet.write(1, 3, 'Items', bold)
        sheet.write(1, 4, 'Harga Modal', bold) 
        sheet.write(1, 5, 'Harga Jual', bold)
        sheet.write(1, 6, 'Type Items', bold)        
        row = 2
        col = 0
        for obj in mitra:
           col = 0 
           sheet.write(row, col, obj.name)
           sheet.write(row, col+1, obj.alamat)
           sheet.write(row, col+2, obj.no_telp)
           for xxx in obj.items_id:
               sheet.write(row, col+3, xxx.name)
               sheet.write(row, col+4, xxx.harga_beli)
               sheet.write(row, col+5, xxx.harga_jual)
               sheet.write(row, col+6, xxx.detail_items_id.kode_buku)   
               row += 1
           row += 1

