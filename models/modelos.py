from odoo import models, fields

class ModelosElectro(models.Model):
    _name = 'electro.modelos'
    codigo = fields.Integer('Codigo', required=True)
    modelo = fields.Char('Modelo', required=True)


    def name_get(self):
        res=[]
        for record in self:
            name = record.modelo
            res.append((record.id, name))
        return res

