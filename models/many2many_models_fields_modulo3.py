# Copyright 2015 Antiun Ingeniería, S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, exceptions
from odoo.exceptions import ValidationError


class ModeloPorqueCompranClientes(models.Model):
    _name = "modelo.porque.compran.clientes"


    name = fields.Char("Name")

    descripcion = fields.Char(
        string="Descripcion",
        help="Ingrese la descripcion",
        readonly=False
    )


class ModeloNegociosModel(models.Model):
    _name = "modelo.negocios.model"


    name = fields.Char("Name")

    descripcion = fields.Char(
        string="Descripcion",
        help="Ingrese la descripcion",
        readonly=False
    )


class ModeloMetodosVenta(models.Model):
    _name = "modelo.metodos.venta"


    name = fields.Char("Name")

    descripcion = fields.Char(
        string="Descripcion",
        help="Ingrese la descripcion",
        readonly=False
    )


class ModeloPromocionProductos(models.Model):
    _name = "modelo.promocion.productos"


    name = fields.Char("Name")

    descripcion = fields.Char(
        string="Descripcion",
        help="Ingrese la descripcion",
        readonly=False
    )

    
class ModeloConseguirNuevosClientes(models.Model):
    _name = "modelo.conseguir.nuevos.clientes"


    name = fields.Char("Name")

    descripcion = fields.Char(
        string="Descripcion",
        help="Ingrese la descripcion",
        readonly=False
    )


class ModeloTemasParaAsesorarse(models.Model):
    _name = "modelo.temas.para.asesorarse"


    name = fields.Char("Name")

    descripcion = fields.Char(
        string="Descripcion",
        help="Ingrese la descripcion",
        readonly=False
    )

