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
    x_state_id = fields.Many2one('res.country.state', 'State', required=True)
    country_id = fields.Many2one('res.country', 'Country', required=True, default='Colombia')
    _order = 'code'


class Lead(models.Model):
    _inherit = "crm.lead"

    x_vereda = fields.Char(
        string="Barrio/Vereda",
        help="Tax Identification Number. The first 2 characters are the "
        "country code.",
    )

    x_datos1 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "ACEPTA ENTREGARLE A UNIMINUTO LOS DATOS GENERALES SUYOS Y DEL MICRONEGOCIO CON FINES ACADÉMICOS",
    )

    doctype = fields.Selection(
        [
            ('1', 'Sin identificación'),
            ('2', 'Cédula'),
            ('3', 'Cédula de extranjería'),
            ('4', 'Pasaporte'),
            ('5', 'Permiso especial de permanencia (PEP)'),

        ], "Tipo de identificación", default='1', required=True
    )

    xidentification = fields.Integer(
        string="Número de identificación",
        help="Ingrese el tipo de identificación ", required=True
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

        ], "Sexo", required=True
    )

    x_etnia = fields.Selection(
        #string="¿Pertenece a algún tipo de etnia?",
        [
            ('20', 'NARP'),
            ('21', 'Gitano ROM'),
            ('22', 'Indígena'),
            ('23', 'No pertenezco'),

        ], "¿Pertenece a algún tipo de etnia?", required=True
    )

    x_edad = fields.Integer(
        string="Edad",
        help="Escriba su edad", required=True
    )

    x_limitacion = fields.Char(
        string="¿Usted tiene algún tipo de diversidad funcional?",
        help="Describa sus limitaciones fisicas", required=True
    )

    x_escolaridad = fields.Selection(
        [
            ('30', 'Primaria incompleta'),
            ('31', 'Primaria completa'),
            ('32', 'Secundaria incompleta'),
            ('33', 'Secundaria completa'),
            ('34', 'Tecnico'),
            ('35', 'Tecnólogo'),
            ('36', 'Educacion No formal: Cursos libres, diplomados,seminarios.'),
            ('37', 'Tecnólogo'),
            ('38', 'Pregrado'),
            ('39', 'Especialización'),
            ('40', 'Maestría'),
            ('41', 'Otro'),
            ('42', 'Ninguno'),

        ], "Ultimo año de escolaridad", required=True
    )

    #x_cual = fields.Char(
        #string="Cual?",
        #help="Escriba los detalles",
    #)

    x_grupos = fields.Selection(
    	[
            ('40', 'Si'),
            ('41', 'No'),

        ], "¿Pertenece a alguna organización:  asociación, corporación, cooperativa, grupo?",

        help="Escriba el tipo de organización a la cual pertenece",
    )

    x_grupos_cual = fields.Char(
        string="¿Cuál?",
        help="¿A qué tipo de organización, asociación, corporación, cooperativa, grupo pertenece?",
    )

    x_estrato = fields.Selection(
        [
            ('40', '1'),
            ('41', '2'),
            ('42', '3'),
            ('43', '4'),
            ('44', '5'),
            ('45', '6'),
        ], "Estrato socioeconomico de residencia ",
    )

    x_situacion = fields.Selection(
        [
            ('40', 'Cuenta propia'),
            ('41', 'Empleador'),
        ], "Actualmente usted es", default='40'
    )

    x_actcomer = fields.Selection(
    	[
            ('40', 'Peluqueria, salon de belleza, barberia, arreglo de uñas'),
            ('41', 'Cafeteria o  salon de onces'),
            ('42', 'Elaboracion de productos de panaderia, tortas, pasteles, pudin, ponques'),
            ('43', 'Comidas rapidas '),
            ('44', 'Bar, taberna, estanco, licorera, discoteca, rumbeadero'),
            ('45', 'Tienda'),
            ('46', 'Billares, juegos de mesa, rana, gallera'),
            ('47', 'Comercio  de colchones, muebles'),
            ('48', 'Comercio de elementos deportivos, implementos, balones, tienda de bicicletas'),
            ('49', 'Veterinaria, venta de alimento o enseres para mascotas o animales, perros, gatos, peces.'),
            ('50', 'Comercio de productos de tecnologia, celulares, computadores'),
            ('51', 'Productos asociados al arte, cuadros, pintura, joyeria, relojeria, actividades de fotografia'),
            ('52', 'Comercio de regalos, variedades, adornos, tajetas, articulos diversos.'),
            ('53', 'Heladeria o fruteria '),
            ('54', 'Carnicería, pescadería, charcutería, quesos, lácteos, salsamentaria'),
            ('55', 'Cerrajería, Ferretería, ferreléctricos, vidriería'),
            ('56', 'Servicios de salud, óptica, odontología, consultorio médico, ortodoncia, tienda naturista'),
            ('57', 'Droguería'),
            ('58', 'Envíos, giros, recargas, chance, apuestas, servicios financieros, banco, corresponsal'),
            ('59', 'Café internet, telecomunicaciones, videojuegos, venta de películas, mantenimiento computadores, telefonía, informática'),
            ('60', 'Floristería, abono, venta de gallinas, actividad pecuaria'),
            ('61', 'Retaurante, fondo paisa, corrientazo, asadero'),
            ('62', 'Papelería, Fotocopias, impresiones, miscelanea'),
            ('63', 'Casa comercial, monte de piedad, compraventa, prestamista'),
            ('64', 'Eventos, refrigerios, casa de banquetes'),
            ('65', 'Gimnasio, academia de baile, establecimiento para deportes'),
            ('66', 'Academia de idiomas, lectura rápida'),
            ('67', 'Inmobiliaria'),
            ('68', 'Asesoría comercial, publicidad, mercadeo imagen corporativa, asesoria juridica, tributaria'),
            ('69', 'Mantenimiento de bicicletas, automóbiles, despinche, vulcanizadora, taller automotriz, mecánica general'),
            ('70', 'Lavandería'),
            ('71', 'Supermercado, minimercado, mercado, venta de elementos de aseo, venta de frutas y verduras'),
            ('72', 'Venta de ropa, zapatos, calzado, modestería, uniformes, accesorios, prendas y elementos de vestir, remontadora de calzado'),
            ('73', 'Parqueadero de carros, motos, bicicletas'),
            ('74', 'Productos de belleza, spa, tatuajes'),
            ('75', 'Fábrica de manufacturas textiles ropa calzado balones deportivos cueros marroquinería'),
            ('76', 'Venta y comercio de autopartes, carros, vehículos, motos, partes de motocicleta, cascos, automotores'),
            ('77', 'Fábrica y venta de productos metálicos hierro acero maquinaria y otras aplicaciones industriales'),
            ('78', 'Jardín infantil, salacuna, educación'),
            ('79', 'Transporte de pasajeros'),
        ], "¿Cuál es la actividad comercial de su negocio?",
        help="Escriba la actividad comercial de su negocio",
    )

    x_sector = fields.Selection(
        [
            ('40', 'Agropecuario'),
            ('41', 'Comercio'),
            ('42', 'Servicios'),
            ('43', 'Industrial'),
        ], "¿En qué sector económico se encuentra su negocio?",
        help="Escriba el sector económico de su negocio ",
    )

    x_ubic = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Zona Urbana'),
            ('51', 'Zona rural'),

        ], "Ubicación del negocio",
    )

    x_com_cuenta = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Establecimiento'),
            ('51', 'Sin establecimiento'),

        ], "Su actividad comercial cuenta con",
    )

    x_cont1 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "Una vez comprendido el programa de acompañamiento, ¿usted desea continuar?",
    )

    x_datos3 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "ACEPTA ENTREGARLE A UNIMINUTO LOS DATOS GENERALES SUYOS Y DEL MICRONEGOCIO CON FINES ACADÉMICOS",
    )

    x_sisben = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "¿Usted pertenece al Sisben?",
    )

    x_tsisben = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Urbano'),
            ('51', 'Rural'),

        ], "¿Su Sisben es?",
    )

    x_nsisben = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Nivel 1 '),
            ('51', 'Nivel 2 '),
            ('52', 'Nivel 3 '),

        ], "¿Cuál es el nivel de Sisben que usted tiene?",
    )

    x_tactiv = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Menos de un año '),
            ('51', 'Mas de un año'),

        ], "¿Cuánto tiempo lleva ejerciendo su actividad?",
    )

    x_tactiv_anos = fields.Integer(
        string="¿Cuantos años?",
        help="Ingrese un numero mayor a 1 ",
    )

    x_horas_trab = fields.Integer(
        string="¿Cuantas horas de trabajo diario dedica para el funcionamiento del negocio?",
    )

    x_cotiza = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Salud y pensión'),
            ('51', 'Solo salud'),
            ('52', 'Solo pensión'),
            ('53', 'No aporta '),

        ], "¿Usted cotiza a salud y pensión?",
    )

    x_motivo = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Por necesidad de generar ingresos'),
            ('51', 'Oportunidad de negocio en el mercado'),
            ('52', 'Por tradición familiar o herencia '),
            ('53', 'Complementar el ingreso familiar o mejorar el ingreso'),
            ('54', 'Para ejercer su oficio, carrera o profesión'),
            ('55', 'Pocas oportunidades de empleo'),
            ('56', 'Otro (administrar horario, gusto, desplazamiento, búsqueda de independencia)'),

        ], "¿Cuál fue el motivo principal para la creación del negocio?",
    )

    x_sitio_ubi = fields.Selection(
        #string="Sexo",
        [
            ('50', 'En su vivienda'),
            ('51', 'Establecimiento'),
            ('52', 'De puerta a puerta o a domicilio'),
            ('53', 'Ambulante - sitio al descubierto'),
            ('54', 'Vehículo con o sin motor'),
            ('55', 'Otro (cancha de futbol, parqueadero)'),

        ], "¿Cual es el sitio, lugar o ubicación del negocio?",
    )

    x_microneg = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Formalizado'),
            ('51', 'Informal'),

        ], "¿Su micronegocio está?",
    )

    x_desc_act = fields.Char('Describa la actividad comercial de su negocio', required=True)

    x_desc_act_sec = fields.Char('¿Cuál es la actividad secundaria de su negocio? (si la tiene)')

    x_merca = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "¿Adquiere mercancía y comercializa con ella?",
    )

    x_merca_tipo = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Artículos de uso doméstico'),
            ('51', 'Ropa y calzado'),
            ('52', 'Artículos para empresas u oficinas'),
            ('53', 'Artículos para uso industrial'),
            ('54', 'Materias primas para fábricas o industrias'),
            ('55', 'Artículos para construcción'),
            ('56', 'Alimentos o bebidas de consumo humano'),
            ('57', 'Artículos para salud humana'),
            ('58', 'Artículos para consumo animal'),
            ('69', 'Artículos veterinarios'),
            ('60', 'Artículos religiosos'),
            ('61', 'Frutas '),
            ('62', 'Artículos para carros'),
            ('63', 'Otros'),

        ], "¿Qué tipo de mercancías?",
    )

    x_fabric = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Sí, nosotros los fabricamos'),
            ('51', 'No, nosotros no los fabricamos'),

        ], "Los productos que comercializa, ¿son fabricados por usted o por sus empleados?",
    )

    x_fabric_si = fields.Selection(
        #string="Sexo",
        [
            ('50', ' Artículos de uso doméstico'),
            ('51', ' Ropa y calzado'),
            ('52', 'Artículos para empresas u oficinas'),
            ('53', '  Artículos para uso industrial'),
            ('54', 'Materias primas para fábricas o industrias'),
            ('55', 'Artículos para construcción'),
            ('56', 'Alimentos o bebidas de consumo humano'),
            ('57', 'Artículos para salud humana'),
            ('58', 'Artículos para consumo animal'),
            ('59', 'Artículos veterinarios'),
            ('60', 'Artículos religiosos'),
            ('61', 'Frutas '),
            ('62', 'Otros'),

        ], "¿Qué tipo de mercancías?",
    )

    x_servicios = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Artículos de uso doméstico'),
            ('51', 'Culturales o creativos'),
            ('52', 'Transporte'),
            ('53', 'Almacenamiento'),
            ('54', 'Alojamiento'),
            ('55', 'Turismo'),
            ('56', 'Inmobiliario o finca raíz'),
            ('57', 'Actividades Financieras'),
            ('58', 'Servicios administrativos o de apoyo'),
            ('59', 'Actividades Profesionales'),
            ('60', 'Actividades Técnicas'),
            ('61', 'Suministro de servicios para hogares'),
            ('62', 'Suministro de servicios empresariales'),
            ('63', 'Suministro de servicios para fábrica o industria'),
            ('64', 'Otros'),

        ], "Si presta servicios o realiza consultorías, ¿De qué tipo son?",
    )

    x_ambula = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Móvil'),
            ('51', 'Estacionario'),
            ('52', 'No aplica'),

        ], "Los productos que comercializa, ¿son fabricados por usted o por sus empleados?",
    )

    x_ambula_2 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Llega muy temprano'),
            ('51', 'Paga vigilancia'),
            ('52', 'Paga una cuota'),
            ('53', 'Le respetan el puesto'),
            ('54', 'Agrupado con otros vendedores'),
            ('55', 'Tiene carné'),
            ('56', 'No aplica'),
            ('57', 'Otro ¿Cuál?'),

        ], "Si el negocio es ambulante - sitio al descubierto, ¿cómo hace para conservar diariamente el mismo sitio de trabajo?",
    )

    x_ambula_cual = fields.Char(
        string="¿Cuál?",
    )

    x_mprima = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Diariamente'),
            ('51', 'Semanalmente'),
            ('52', 'Quincenalmente'),
            ('53', 'Mensualmente'),

        ], "¿Con que frecuencia adquiere materia prima o mercania para su negocio?",
    )

    x_clientes = fields.Integer(
        string="¿Cuántos clientes atiende diariamente (1-100)?",
        help="Ingrese un numero entre 1 y 100",
    )

    x_problema = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Dificultad en obtener creditos'),
            ('51', 'Competencia excesiva'),
            ('52', 'Problemas de comercializacion de productos'),
            ('53', 'Problemas con las autoridades'),
            ('54', 'No cuenta con las condiciones de bioseguridad que se requieren'),
            ('55', 'Aumento en el precio de los insumos'),
            ('56', 'Desconfianza de los clientes para adquirir productos de consumo'),
            ('57', 'Dificultad en la produccion del producto'),
            ('58', 'No se encuentra virtualizado'),


        ], "Si el negocio es ambulante - sitio al descubierto, ¿cómo hace para conservar diariamente el mismo sitio de trabajo?",
    )

    x_familia = fields.Integer(
        string="¿Cuantas personas de su familia trabajan actualmente con usted en el negocio?",
        help="Ingrese un numero entre 1 y 100",
    )

    x_reinvierte = fields.Integer(
        string="¿Qúé porcentaje de las ventas reinvierte nuevamente en mercancia (1-100)?",
        help="Ingrese un numero entre 1 y 100",
    )





    country_id = fields.Many2one('res.country', "Country")
    xcity = fields.Many2one('res.country.state.city', "Municipio de Residencia")
    city = fields.Char(related="xcity.name")

    x_state_id = fields.Many2one('res.country.state', 'Departamento del Micronegocio')
    x_city_id = fields.Many2one('res.country.state.city', 'Municipio del Micronegocio')

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




