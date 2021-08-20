# Copyright 2015 Antiun Ingeniería, S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, exceptions
from odoo.exceptions import ValidationError


class ModeloHerramientasTecnologicas(models.Model):
    _name = "modelo.herramientas.tecnologicas"


    name = fields.Char("Name")

    descripcion = fields.Char(
        string="Descripcion",
        help="Ingrese la descripcion",
        readonly=False
    )
