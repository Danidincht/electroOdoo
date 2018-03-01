from odoo import models, fields, api

class ElectroElectrodomesticos(models.Model):
    _name = 'electro.electrodomesticos'
    tipo = fields.Char('Tipo de electrodomestico', required=True)
    marca = fields.Many2one('electro.marcas', 'Marca')
    modelo = fields.Many2one('electro.modelos', 'Modelo')
    precio = fields.Integer('Precio', required=True)

    def name_get(self):
        res=[]
        for record in self:
            name = record.tipo
            res.append((record.id, name))
        return res


    @api.one
    def limpiar(self):
        self.marca = ""
        return True

    @api.multi
    def limpia_todo(self):
        done_recs = self.search([('marca', '=', 'fender')])
        done_recs.write({'marca': 'Fender'})
        return True

