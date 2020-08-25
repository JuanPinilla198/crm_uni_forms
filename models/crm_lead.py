# Copyright 2015 Antiun Ingeniería, S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class CountryStateCity(models.Model):
    """
    Model added to manipulate separately the cities on Partner address.
    """
    _description = 'Model to manipulate Cities'
    _name = 'res.country.state.city'

    code = fields.Char('City Code', size=5, help='Code DANE - 5 digits-',
                       required=True)
    name = fields.Char('City Name', size=64, required=True)
    state_id = fields.Many2one('res.country.state', 'State', required=True)
    country_id = fields.Many2one('res.country', 'Country', required=True, default='Colombia')
    _order = 'code'


class Lead(models.Model):
    _inherit = "crm.lead"

    x_vereda = fields.Char(
        string="Barrio/Vereda",
        help="Tax Identification Number. The first 2 characters are the "
        "country code.",
    )

    doctype = fields.Selection(
        [
            ('1', 'Sin identificación'),
            ('2', 'Cédula'),
            ('3', 'Cédula de extranjería'),
            ('4', 'Pasaporte'),
            ('5', 'Permiso especial de permanencia (PEP)'),

        ], "Tipo de identificación", default='1'
    )

    xidentification = fields.Integer(
        string="Número de identificación",
        help="Ingrese el tipo de identificación ",
    )

    _sql_constraints = [
        ('ident_unique',
         'UNIQUE(xidentification)',
         "El número de docuemnto debe ser único!"),
    ]

    x_sexo = fields.Selection(
        #string="Sexo",
        [
            ('10', 'Masculino'),
            ('11', 'Femenino'),
            ('12', 'LGTBI'),

        ], "Sexo", default='10'
    )

    x_etnia = fields.Selection(
        #string="¿Pertenece a algún tipo de etnia?",
        [
            ('20', 'NARP'),
            ('21', 'Gitano ROM'),
            ('22', 'Indígena'),
            ('22', 'No pertenezco'),

        ], "¿Pertenece a algún tipo de etnia?", default='22'
    )

    x_edad = fields.Integer(
        string="Edad",
        help="Escriba su edad",
    )

    x_limitacion = fields.Char(
        string="¿Usted tiene algún tipo de limitación?",
        help="Describa sus limitaciones fisicas",
    )

    x_escolaridad = fields.Selection(
        [
            ('30', 'Primaria incompleta'),
            ('31', 'Primaria completa'),
            ('32', 'Secundaria incompleta'),
            ('33', 'Secundaria completa'),
            ('34', 'Pregrado ¿Cuál?'),
            ('35', 'Postgrado ¿Especialización? ¿Maestría? ¿Cuál?'),
            ('36', 'Otro ¿Cuál?'),
            ('37', 'Ninguno'),

        ], "Ultimo año de escolaridad",
    )

    x_grupos = fields.Char(
        string="¿Pertenece a alguna organización:  asociación, corporación, cooperativa, grupo?",
        help="Escriba el tipo de organización a la cual pertenece",
    )

    x_estrato = fields.Selection(
        [
            ('40', '1'),
            ('41', '2'),
            ('42', '3'),
            ('43', '4'),
            ('44', '5'),
            ('45', '6'),
        ], "Estrato", default='40'
    )

    x_situacion = fields.Selection(
        [
            ('40', 'Cuenta propia'),
            ('41', 'Empleador'),
            ('42', 'Empleado'),
        ], "Actualmente usted es", default='40'
    )

    x_actcomer = fields.Char(
        string="¿Cuál es la actividad comercial de su micronegocio?",
        help="Escriba la actividad comercial de su negocio ",
    )

    x_posgrado = fields.Char(
        string="Posgrado",
        help="Escriba el Posgrado",
    )
    
    x_pregrado = fields.Char(
        string="Pregrado",
        help="Escriba el Pregrado",
    )
        
    x_otro = fields.Char(
        string="Cual",
        help="Escriba que otra cosa ha hecho",
    )

    x_state_id = fields.Many2one('res.country.state', 'Departamento del Micronegocio')

    x_city_id = fields.Many2one('res.country.state', 'Municipio del Micronegocio')

    x_ubic = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Cabecera Urbana'),
            ('51', 'Zona rural'),

        ], "Ubicación del negocio",
    )

    country_id = fields.Many2one('res.country', "Country")
    xcity = fields.Many2one('res.country.state.city', "Municipality")
    city = fields.Char(related="xcity.name")

    @api.onchange('country_id', 'state_id')
    def onchange_location(self):
        """
        This functions is a great helper when you enter the customer's
        location. It solves the problem of various cities with the same name in
        a country
        @param country_id: Country Id (ISO)
        @param state_id: State Id (ISO)
        @return: object
        """
        
        #if self.country_id and not self.state_id:
         #   mymodel = 'res.country.state'
          #  filter_column = 'country_id'
           # check_value = self.country_id.id
            #domain = 'state_id'

        if self.state_id:
            mymodel = 'res.country.state.city'
            filter_column = 'state_id'
            check_value = self.state_id.id
            domain = 'xcity'
        else:
            return {}

        obj = self.env[mymodel]
        ids = obj.search([(filter_column, '=', check_value)])
        id_domain = []
        for id in ids:
            id_domain.append(id.id)
        
        return {
            'domain': {domain: [('id', 'in', id_domain)]},
            'value': {domain: ''}
        }


