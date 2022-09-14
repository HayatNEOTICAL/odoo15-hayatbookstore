from odoo import http, models, fields
from odoo.http import request
import json

class Hayatbookstore(http.Controller):
    @http.route('/hayatbookstore/getitems', auth='public', method=['GET'])
    def getBarang(self, **kw):
        barang = request.env['hayatbookstore.items'].search([])
        isi = []
        for bb in barang:
            isi.append({
                'nama_items' : bb.name,
                'harga_jual' : bb.harga_jual,
                'stok' : bb.stok
            })
        return json.dumps(isi)

    @http.route('/hayatbookstore/getmitra/', auth='public', method=['GET'])
    def getSupplier(self, **kw):
        supplier = request.env['hayatbookstore.mitra'].search([])
        sup = []
        for s in supplier:
            sup.append({
                'nama_perusahaan' : s.name,
                'alamat' : s.alamat,
                'no_telepon' : s.no_telp,
                'items' : s.items_id[0].name   
            })  
        return json.dumps(sup)        