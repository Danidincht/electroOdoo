
from odoo import models, fields

class ElectroMarcas(models.Model):
    _name = 'electro.marcas'
    codigo = fields.Integer('Codigo', required=True)
    nombre = fields.Char('Nombre de la marca', required=True)

    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res
