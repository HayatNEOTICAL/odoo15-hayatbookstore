from odoo import models, fields
from datetime import timedelta

class MitraXlsx(models.AbstractModel):
    _name = 'report.hayatbookstore.report_transaksi_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, penjualan):
        sheet = workbook.add_worksheet('Daftar Penjualan')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap), bold)   
        sheet.write(1, 0, 'No. Nota', bold)
        sheet.write(1, 1, 'Nama Pembeli', bold)
        sheet.write(1, 2, 'Tgl. Transaksi', bold)
        sheet.write(1, 3, 'Items', bold)
        sheet.write(1, 4, 'Harga Satuan', bold) 
        sheet.write(1, 5, 'Quantity', bold)
        sheet.write(1, 6, 'Subtotal', bold)
        sheet.write(1, 7, 'Total Pembayaran', bold)
        sheet.write(1, 8, 'Status', bold)          
        row = 2
        col = 0
        for obj in penjualan:
           col = 0 
           sheet.write(row, col, obj.name)
           sheet.write(row, col+1, obj.nama_pembeli.name)
           sheet.write(row, col+2, (obj.tgl_penjualan+ timedelta(hours=7)).strftime("%d/%m/%Y, %H:%M:%S"))
           sheet.write(row, col+7, obj.total_bayar)
           sheet.write(row, col+8, obj.state)
           for xxx in obj.detailpenjualan_ids:
               sheet.write(row, col+3, xxx.items_id.name)
               sheet.write(row, col+4, xxx.harga_satuan)
               sheet.write(row, col+5, xxx.qty)
               sheet.write(row, col+6, xxx.subtotal)   
               row += 1
           row += 1

