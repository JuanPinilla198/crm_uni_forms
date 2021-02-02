# Copyright 2015 Antiun Ingeniería, S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, exceptions
from odoo.exceptions import ValidationError

class CountryStateCity(models.Model):
    """
    Model added to manipulate separately the cities on Partner address.
    """
    _description = 'Model to manipulate Cities'
    _name = 'res.country.state.city'

    code = fields.Char('City Code', size=5, help='Code DANE - 5 digits-',)
    name = fields.Char('City Name', size=64, )
    state_id = fields.Many2one('res.country.state', 'State')
    country_id = fields.Many2one('res.country', 'Country', default='Colombia')
    _order = 'code'

class SeveralFields(models.Model):
    _description = 'Modelo para Manipular Many2many'
    _name = 'model.manipulate.many2many'

    name = fields.Char('Beneficios')

class modelo69form(models.Model):
    _description = 'Modelo para Manipular Many2many'
    _name = 'model.form.many2many'

    name = fields.Char('69form')

class modelo72inf(models.Model):
    _description = 'Modelo para Manipular Many2many'
    _name = 'model.inf.many2many'

    name = fields.Char('72inform')

class modelo72form(models.Model):
    _description = 'Modelo para Manipular Many2many72'
    _name = 'model.many2many72'

    name = fields.Char('72form')

class modelo73form(models.Model):
    _description = 'Modelo para Manipular Many2many73'
    _name = 'model.many2many73'

    name = fields.Char('73form')

class modelo75inf(models.Model):
    _description = 'Modelo para Manipular Many2many75'
    _name = 'model.many2many75'

    name = fields.Char('75form')

class modelo76inf(models.Model):
    _description = 'Modelo para Manipular Many2many76'
    _name = 'model.many2many76'

    name = fields.Char('76form')

class modelo102inf(models.Model):
    _description = 'Modelo para Manipular Many2many102'
    _name = 'model.many2many102'

    name = fields.Char('102form')

class modelo176form(models.Model):
    _description = 'Modelo para Manipular Many2many176'
    _name = 'model.many2many176'

    name = fields.Char('176form')

class modelo176form(models.Model):
    _description = 'Modelo para Manipular Many2many177'
    _name = 'model.many2many177'

    name = fields.Char('177form')

class Lead(models.Model):
    _inherit = "crm.lead"

    x_nombre = fields.Char(
    	related ="name",
        string="2. Nombre del Propietario",
        help="Ingrese el nombre del propietario",
        readonly=False
    )

    x_nombre_negocio = fields.Char(
        string="1. Nombre del Negocio",
        help="Ingrese el nombre del negocio",
        readonly=False
    )

    x_vereda = fields.Char(
        string="10. Barrio/Vereda",
        help="Tax Identification Number. The first 2 characters are the "
        "country code.",
    )

    x_datos1 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),

        ], "ACEPTA ENTREGARLE A UNIMINUTO LOS DATOS GENERALES SUYOS Y DEL MICRONEGOCIO CON FINES ACADÉMICOS",
    )

    doctype = fields.Selection(
        [
            ('sin_identificacion', 'Sin identificación'),
            ('cedula', 'Cédula'),
            ('cedula_de_extranjeria', 'Cédula de extranjería'),
            ('pasaporte', 'Pasaporte'),
            ('permiso_especial_de_permanencia_pep', 'Permiso especial de permanencia (PEP)'),

        ], "3. Tipo de identificación", default='cedula'
    )

    x_identification = fields.Integer(
        string="4. Número de identificación",
        help="Ingrese el tipo de identificación ",
        store=True,
    )

    _sql_constraints = [
        ('x_identification',
         'UNIQUE (x_identification)',
         "El número de documento debe ser único!"),
    ]

    x_sexo = fields.Selection(
        [
            ('masculino', 'Masculino'),
            ('femenino', 'Femenino'),
        ], "5. Sexo", 
    )

    x_etnia = fields.Selection(
        [
            ('narp', 'NARP'),
            ('gitano_rom', 'Gitano ROM'),
            ('indigena', 'Indígena'),
            ('no_pertenezco', 'No pertenezco'),

        ], "6. ¿Pertenece a algún tipo de etnia?", 
    )

    x_edad = fields.Integer(
        string="7. Edad",
        help="Escriba su edad", 
    )

    x_limitacion = fields.Char(
        string="13. ¿Usted tiene algún tipo de diversidad funcional?",
        help="Describa sus limitaciones físicas", 
    )

    x_escolaridad = fields.Selection(
        [
            ('primaria_incompleta', 'Primaria incompleta'),
            ('primaria_completa', 'Primaria completa'),
            ('secundaria_incompleta', 'Secundaria incompleta'),
            ('secundaria_completa', 'Secundaria completa'),
            ('tecnico', 'Técnico'),
            ('tecnologo', 'Tecnólogo'),
            ('educacion_no_formal_Cursos_libres_diplomados_seminarios', 'Educación No formal: Cursos libres, diplomados,seminarios'),
            ('tecnologo', 'Tecnólogo'),
            ('pregrado', 'Pregrado'),
            ('especializacion', 'Especialización'),
            ('maestria', 'Maestría'),
            ('ninguno', 'Ninguno'),
        ], "14. Último año de escolaridad", 
    )

    x_grupos = fields.Selection(
    	[
            ('si', 'Si'),
            ('no', 'No'),
        ], "15. ¿Pertenece a alguna organización:  asociación, corporación, cooperativa, grupo?",
        help="Escriba el tipo de organización a la cual pertenece",
    )

    x_grupos_cual = fields.Char(
        string="¿Cuál?",
        help="16. ¿A qué tipo de organización, asociación, corporación, cooperativa, grupo pertenece?",
    )

    x_estrato = fields.Selection(
        [
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
        ], "17. Estrato socioeconómico de residencia ",
    )

    x_situacion = fields.Selection(
        [
            ('cuenta_propia', 'Cuenta propia'),
            ('empleador', 'Empleador'),
        ], "18. Actualmente usted es"
    )

    x_actcomer = fields.Selection(
    	[
            ('peluqueria_salon_de_belleza_barberia_arreglo_de_unas', 'Peluquería, salón de belleza, barbería, arreglo de uñas'),
            ('cafeteria_o _salon_de_onces', 'Cafetería o  salón de onces'),
            ('elaboracion_de_productos_de_panaderia_tortas_pasteles_pudin_ponques', 'Elaboración de productos de panadería, tortas, pasteles, pudin, ponques'),
            ('comidas_rapidas', 'Comidas rápidas'),
            ('bar_taberna_estanco_licorera_discoteca_rumbeadero', 'Bar, taberna, estanco, licorera, discoteca, rumbeadero'),
            ('tienda', 'Tienda'),
            ('billares_juegos_de_mesa_rana_gallera', 'Billares, juegos de mesa, rana, gallera'),
            ('comercio_de_colchones_muebles', 'Comercio  de colchones, muebles'),
            ('comercio_de_elementos_deportivos_implementos_balones_tienda_de_bicicletas', 'Comercio de elementos deportivos, implementos, balones, tienda de bicicletas'),
            ('veterinaria_venta_de_alimento_o_enseres_para_mascotas_o_animales_perros_gatos_peces', 'Veterinaria, venta de alimento o enseres para mascotas o animales, perros, gatos, peces'),
            ('comercio_de_productos_de_tecnologia_celulares_computadores', 'Comercio de productos de tecnología, celulares, computadores'),
            ('productos_asociados_al_arte_cuadros_pintura_joyeria_relojeria_actividades_de_fotografia', 'Productos asociados al arte, cuadros, pintura, joyería, relojería, actividades de fotografía'),
            ('comercio_de_regalos_variedades_adornos_tajetas_articulos_diversos', 'Comercio de regalos, variedades, adornos, tajetas, articulos diversos.'),
            ('heladeria_o_fruteria', 'Heladería o frutería'),
            ('carniceria_pescaderia_charcuteria_quesos_lacteos_salsamentaria', 'Carnicería, pescadería, charcutería, quesos, lácteos, salsamentaria'),
            ('cerrajeria_ferreteria_ferrelectricos_vidrieria', 'Cerrajería, ferretería, ferreléctricos, vidriería'),
            ('servicios_de_salud_optica_odontologia_consultorio_medico_ortodoncia_tienda_naturista', 'Servicios de salud, óptica, odontología, consultorio médico, ortodoncia, tienda naturista'),
            ('drogueria', 'Droguería'),
            ('envios_giros_recargas_chance_apuestas_servicios_financieros_banco_corresponsal', 'Envíos, giros, recargas, chance, apuestas, servicios financieros, banco, corresponsal'),
            ('cafe_internet_telecomunicaciones_videojuegos_venta_de_peliculas_mantenimiento_computadores_telefonia_informatica', 'Café internet, telecomunicaciones, videojuegos, venta de películas, mantenimiento computadores, telefonía, informática'),
            ('floristeria_abono_venta_de_gallinas_actividad_pecuaria', 'Floristería, abono, venta de gallinas, actividad pecuaria'),
            ('restaurante_fondo_paisa_corrientazo_asadero', 'Restaurante, fondo paisa, corrientazo, asadero'),
            ('papeleria_fotocopias_impresiones_miscelanea', 'Papelería, fotocopias, impresiones, miscelanea'),
            ('casa_comercial_monte_de_piedad_compraventa_prestamista', 'Casa comercial, monte de piedad, compraventa, prestamista'),
            ('eventos_refrigerios_casa_de_banquetes', 'Eventos, refrigerios, casa de banquetes'),
            ('gimnasio_academia_de_baile_establecimiento_para_deportes', 'Gimnasio, academia de baile, establecimiento para deportes'),
            ('academia_de_idiomas_lectura_rapida', 'Academia de idiomas, lectura rápida'),
            ('inmobiliaria', 'Inmobiliaria'),
            ('asesora_comercial_publicidad_mercadeo_imagen_corporativa_asesoría_juridica_tributaria', 'Asesoría comercial, publicidad, mercadeo imagen corporativa, asesoría jurídica, tributaria'),
            ('mantenimiento_de_bicicletas_automoviles_despinche_vulcanizadora_taller_automotriz_mecanica_general', 'Mantenimiento de bicicletas, automóviles, despinche, vulcanizadora, taller automotriz, mecánica general'),
            ('lavanderia', 'Lavandería'),
            ('supermercado_minimercado_mercado_venta_de_elementos_de_aseo_venta_de_frutas_y_verduras', 'Supermercado, minimercado, mercado, venta de elementos de aseo, venta de frutas y verduras'),
            ('venta_de_ropa_zapatos_calzado_modesteria_uniformes_accesorios_prendas_y_elementos_de_vestir_remontadora_de_calzado', 'Venta de ropa, zapatos, calzado, modestería, uniformes, accesorios, prendas y elementos de vestir, remontadora de calzado'),
            ('parqueadero_de_carros_motos_bicicletas', 'Parqueadero de carros, motos, bicicletas'),
            ('productos_de_belleza_spa_tatuajes', 'Productos de belleza, spa, tatuajes'),
            ('fabrica_de_manufacturas_textiles_ropa_calzado_balones_deportivos_cueros_marroquineria', 'Fábrica de manufacturas textiles ropa calzado balones deportivos cueros marroquinería'),
            ('venta_y_comercio_de_autopartes_carros_vehículos_motos_partes_de_motocicleta_cascos_automotores', 'Venta y comercio de autopartes, carros, vehículos, motos, partes de motocicleta, cascos, automotores'),
            ('fabrica_y_venta_de_productos_metalicos_hierro_acero_maquinaria_y_otras_aplicaciones_industriales', 'Fábrica y venta de productos metálicos hierro acero maquinaria y otras aplicaciones industriales'),
            ('jardin_infantil_salacuna_educacion', 'Jardín infantil, salacuna, educación'),
            ('transporte_de_pasajeros', 'Transporte de pasajeros'),
        ], "20. ¿Cuál es la actividad comercial de su negocio?",
        help="Escriba la actividad comercial de su negocio",
    )

    x_sector = fields.Selection(
        [
            ('agropecuario', 'Agropecuario'),
            ('comercio', 'Comercio'),
            ('servicios', 'Servicios'),
            ('industrial', 'Industrial'),
        ], "19. ¿En qué sector económico se encuentra su negocio?",
        help="Escriba el sector económico de su negocio ",
    )

    x_ubic = fields.Selection(
        [
            ('zona_Urbana', 'Zona Urbana'),
            ('zona_rural', 'Zona rural'),
        ], "23. Ubicación del negocio",
    )
    #campo actulizado
    x_com_cuenta = fields.Selection(
        [
           ('establecimiento', 'Establecimiento'),
           ('sin_establecimiento', 'Sin establecimiento'),
    
        ], "25. Su actividad comercial cuenta con",
    )
    x_dir_neg = fields.Char(
        string="24. Direccion del negocio",
        help="24. Direccion del negocio",
    )
    x_que_por_ren = fields.Selection(
        [
           ('1', '1%'),
           ('2', '2%'),
           ('3', '3%'),
           ('4', '4%'),
           ('5', '5%'),
           ('6', '6%'),
           ('7', '7%'),
           ('8', '8%'),
           ('9', '9%'),
           ('10', '10%'),
           ('11', '11%'),
           ('12', '12%'),
           ('13', '13%'),
           ('14', '14%'),
           ('15', '15%'),
           ('16', '16%'),
           ('17', '17%'),
           ('18', '18%'),
           ('19', '19%'),
           ('20', '20%'),
           ('21', '21%'),
           ('22', '22%'),
           ('23', '23%'),
           ('24', '24%'),
           ('25', '25%'),
           ('26', '26%'),
           ('27', '27%'),
           ('28', '28%'),
           ('29', '29%'),
           ('30', '30%'),
           ('31', '31%'),
           ('32', '32%'),
           ('33', '33%'),
           ('34', '34%'),
           ('35', '35%'),
           ('36', '36%'),
           ('37', '37%'),
           ('38', '38%'),
           ('39', '38%'),
           ('40', '40%'),
           ('41', '41%'),
           ('42', '42%'),
           ('43', '43%'),
           ('44', '44%'),
           ('45', '45%'),
           ('46', '46%'),
           ('47', '47%'),
           ('48', '48%'),
           ('49', '49%'),
           ('50', '50%'),
           ('51', '51%'),
           ('52', '52%'),
           ('53', '53%'),
           ('54', '54%'),
           ('55', '55%'),
           ('56', '56%'),
           ('57', '57%'),
           ('58', '58%'),
           ('59', '59%'),
           ('60', '60%'),
           ('61', '61%'),
           ('62', '62%'),
           ('63', '63%'),
           ('64', '64%'),
           ('65', '65%'),
           ('66', '66%'),
           ('67', '67%'),
           ('68', '68%'),
           ('69', '69%'),
           ('70', '70%'),
           ('71', '71%'),
           ('72', '72%'),
           ('73', '73%'),
           ('74', '74%'),
           ('75', '75%'),
           ('76', '76%'),
           ('77', '77%'),
           ('78', '78%'),
           ('79', '79%'),
           ('80', '80%'),
           ('81', '81%'),
           ('82', '82%'),
           ('83', '83%'),
           ('84', '84%'),
           ('85', '85%'),
           ('86', '86%'),
           ('87', '87%'),
           ('88', '88%'),
           ('89', '89%'),
           ('90', '90%'),
           ('91', '91%'),
           ('92', '92%'),
           ('93', '93%'),
           ('94', '94%'),
           ('95', '95%'),
           ('96', '96%'),
           ('97', '97%'),
           ('98', '98%'),
           ('99', '99%'),
           ('100', '100%')
        ], "30. ¿Que porcentaje de rentabilidad le dejo su negocio durante de la pandemia COVID-19?",
    )
    x_que_por_ren_ant = fields.Selection(
        [
           ('1', '1%'),
           ('2', '2%'),
           ('3', '3%'),
           ('4', '4%'),
           ('5', '5%'),
           ('6', '6%'),
           ('7', '7%'),
           ('8', '8%'),
           ('9', '9%'),
           ('10', '10%'),
           ('11', '11%'),
           ('12', '12%'),
           ('13', '13%'),
           ('14', '14%'),
           ('15', '15%'),
           ('16', '16%'),
           ('17', '17%'),
           ('18', '18%'),
           ('19', '19%'),
           ('20', '20%'),
           ('21', '21%'),
           ('22', '22%'),
           ('23', '23%'),
           ('24', '24%'),
           ('25', '25%'),
           ('26', '26%'),
           ('27', '27%'),
           ('28', '28%'),
           ('29', '29%'),
           ('30', '30%'),
           ('31', '31%'),
           ('32', '32%'),
           ('33', '33%'),
           ('34', '34%'),
           ('35', '35%'),
           ('36', '36%'),
           ('37', '37%'),
           ('38', '38%'),
           ('39', '38%'),
           ('40', '40%'),
           ('41', '41%'),
           ('42', '42%'),
           ('43', '43%'),
           ('44', '44%'),
           ('45', '45%'),
           ('46', '46%'),
           ('47', '47%'),
           ('48', '48%'),
           ('49', '49%'),
           ('50', '50%'),
           ('51', '51%'),
           ('52', '52%'),
           ('53', '53%'),
           ('54', '54%'),
           ('55', '55%'),
           ('56', '56%'),
           ('57', '57%'),
           ('58', '58%'),
           ('59', '59%'),
           ('60', '60%'),
           ('61', '61%'),
           ('62', '62%'),
           ('63', '63%'),
           ('64', '64%'),
           ('65', '65%'),
           ('66', '66%'),
           ('67', '67%'),
           ('68', '68%'),
           ('69', '69%'),
           ('70', '70%'),
           ('71', '71%'),
           ('72', '72%'),
           ('73', '73%'),
           ('74', '74%'),
           ('75', '75%'),
           ('76', '76%'),
           ('77', '77%'),
           ('78', '78%'),
           ('79', '79%'),
           ('80', '80%'),
           ('81', '81%'),
           ('82', '82%'),
           ('83', '83%'),
           ('84', '84%'),
           ('85', '85%'),
           ('86', '86%'),
           ('87', '87%'),
           ('88', '88%'),
           ('89', '89%'),
           ('90', '90%'),
           ('91', '91%'),
           ('92', '92%'),
           ('93', '93%'),
           ('94', '94%'),
           ('95', '95%'),
           ('96', '96%'),
           ('97', '97%'),
           ('98', '98%'),
           ('99', '99%'),
           ('100', '100%')
        ], "31. ¿Que porcentaje de rentabilidad le dejo su negocio antes de la pandemia COVID-19?",
    )

    x_tien_dur = fields.Selection(
        [('de_1_a_3', 'De 1 mes a 3 meses'),
         ('de_4_a_6', 'De 4 meses a 6 meses'),
         ('de_7_a_11', 'De 7 meses a 11 meses'),
         ('mas_de_1_ano', 'Mas de 1 año'),
         ('no_pienso_continuar_con_el_negocio', 'No pienso continuar con el negocio'),
        ], "32. Tiene usted proyectado continuar con su micronegocio durante:",
    )
    tie_us_cre = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "33. ¿Tiene usted proyectado crecer en puntos de venta?",
    )
    tie_ca_ide = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "34. ¿Tiene proyectado cambiar de idea de negocio?",
    )
    x_cual_34 = fields.Char(
        string="35. ¿Cual?",
        help="",
    )
    x_por_34 = fields.Char(
        string="36. ¿Por que?",
    )

    x_cont1 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "1. Una vez comprendido el programa de acompañamiento, ¿usted desea continuar?",
    )
    x_cont1_por = fields.Char(
        string="2. ¿Por qué no desea continuar con el proceso?",
    )

    x_datos3 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "ACEPTA ENTREGARLE A UNIMINUTO LOS DATOS GENERALES SUYOS Y DEL MICRONEGOCIO CON FINES ACADÉMICOS",
    )
    in_empleo = fields.Selection(
        [
            ('si','Si'),
            ('no','No')
        ], "1. ¿Está interesado en la búsqueda de un empleo?"
    )
    #eliminado
    x_microneg = fields.Selection(
        [
            ('si', 'Formalizado'),
            ('no', 'Informal'),
        ], "25. ¿Su micronegocio está?",
    )

    x_sisben = fields.Selection(
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "26. ¿Usted pertenece al Sisben?",
    )

    x_tsisben = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Urbano'),
            ('51', 'Rural'),

        ], "27. ¿Su Sisben es?",
    )

    x_nsisben = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Nivel 1 '),
            ('51', 'Nivel 2 '),
            ('52', 'Nivel 3 '),

        ], "28. ¿Cuál es el nivel de Sisben que usted tiene?",
    )

    x_estrato_neg = fields.Selection(
        [
            ('40', '1'),
            ('41', '2'),
            ('42', '3'),
            ('43', '4'),
            ('44', '5'),
            ('45', '6'),
        ], "29. Estrato socioeconómico de donde se encuentra el negocio ",
    )

    x_tactiv = fields.Integer(
    	string="30. ¿Cuánto tiempo lleva su negocio en funcionamiento? (Meses)",
    )

    x_dias_sem_inf = fields.Integer(
        string="31. ¿Cuantos días a la semana opera su  negocio?",
    )

    x_dias_sem_for = fields.Integer(
        string="31. ¿Cuántos días a la semana opera su negocio? ",
    )

    x_dias_sem_for2 = fields.Integer(
        string="32. ¿Cuantos días a la semana dedica a su  negocio?",
    )

    x_horas_trab_inf = fields.Integer(
        string="32. ¿Cuántas horas de trabajo diario dedicaa su negocio?",
    )

    x_horas_trab_form = fields.Integer(
        string="33. ¿Cuántas horas de trabajo diario dedica a su negocio?",
    )

    x_trabajadores_inf = fields.Integer(
        string="33. ¿Cuántos trabajadores tiene su negocio?",
    )

    x_trabajadores_form = fields.Integer(
        string="34. ¿Cuántos trabajadores tiene su negocio?",
    )

    x_cotiza_form = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Salud'),
            ('51', 'Pensión'),
            ('52', 'ARL'),
            ('53', 'Caja de compensación'),
            ('54', 'ICBF'),
            ('55', 'SENA'),
            ('56', 'Todas'),
            ('57', 'Ninguno'),

        ], "35. ¿Cuáles son los aportes que realiza para sus trabajadores?",
    )

    x_cotiza_inf = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Salud'),
            ('51', 'Pensión'),
            ('52', 'ARL'),
            ('53', 'Ninguna'),
            ('54', 'ICBF'),
            ('55', 'SENA'),
            ('56', 'Todas'),

        ], "34. ¿Cuáles son los aportes que realiza su negocio para sus trabajadores?",
    )

    x_motivo_inf = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Por necesidad de generar ingresos'),
            ('51', 'Oportunidad de negocio en el mercado'),
            ('52', 'Por tradición familiar o herencia'),
            ('53', 'Complementar el ingreso familiar o mejorar el ingreso'),
            ('54', 'Para ejercer su oficio, carrera o profesión'),
            ('55', 'Pocas oportunidades de empleo'),
            ('56', 'Administrar horario'),
            ('57', 'Busqueda de independencia'),
            ('58', 'Facilidad de desplazamiento'),
            ('59', 'Otros'),

        ], "37. ¿Cuál fue el motivo principal para la creación del negocio?",
    )

    x_motivo_form = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Por necesidad de generar ingresos'),
            ('51', 'Oportunidad de negocio en el mercado'),
            ('52', 'Por tradición familiar o herencia '),
            ('53', 'Complementar el ingreso familiar o mejorar el ingreso'),
            ('54', 'Para ejercer su oficio, carrera o profesión'),
            ('55', 'Pocas oportunidades de empleo'),
            ('56', 'Para generar oportunidad de empleo'),
            ('57', 'Otro'),

        ], "38. ¿Cuál fue el motivo principal para la creación del negocio?",
    )

    x_motivo_cual_inf = fields.Char('38. ¿Cuál?')

    x_motivo_cual_form = fields.Char('39. ¿Cuál?')

    x_recursos_inf = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Ahorros personales'),
            ('51', 'Prestamos familiares '),
            ('52', 'Prestamos bancarios'),
            ('53', 'Prestamistas '),
            ('54', 'Capital semilla'),
            ('55', 'Programas del Gobierno'),
            ('56', 'Otras'),

        ], "35. ¿Cuál fue la principal fuente de recursos para la creación o constitución del negocio?",
    )


    x_recursos_form = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Ahorros personales'),
            ('51', 'Prestamos familiares '),
            ('52', 'Prestamos bancarios'),
            ('53', 'Prestamistas '),
            ('54', 'Capital semilla'),
            ('55', 'Programas del Gobierno'),
            ('56', 'Otras'),

        ], "36. ¿Cuál fue la principal fuente de recursos para la creación o constitución del negocio?",
    )

    x_recursos_cual_inf = fields.Char('36. ¿Cuál?')

    x_recursos_cual_form = fields.Char('37. ¿Cuál?')

    x_sitio_ubi_inf = fields.Selection(
        #string="Sexo",
        [
            ('50', 'En la vivienda'),
            ('51', 'Local, tienda, taller, fábrica, oficina, consultorio'),
            ('52', 'De puerta a puerta o a domicilio'),
            ('53', 'Ambulante - sitio al descubierto'),
            ('54', 'Vehículo con o sin motor'),
            ('55', 'Obra o construcción'),
            ('56', 'Finca'),
            ('57', 'Otro'),

        ], "39. ¿Cuál es el sitio o ubicación del negocio?",
    )

    x_sitio_ubi_form = fields.Selection(
        #string="Sexo",
        [
            ('50', 'En la vivienda'),
            ('51', 'Local, tienda, taller, fábrica, oficina, consultorio'),
            ('52', 'Obra o construcción'),
            ('53', 'Finca'),
            ('54', 'Otro'),

        ], "40. ¿Cuál es el sitio, lugar o ubicación del negocio?",
    )

    x_sitio_ubi_cual_form = fields.Char('41. ¿Cuál?')
    x_sitio_ubi_cual_inf = fields.Char('40. ¿Cuál?')

    x_desc_act_form = fields.Char('42. Describa la actividad comercial de su negocio' )
    x_desc_act_inf = fields.Char('41. Describa la actividad comercial de su negocio' )

    x_desc_act_sec_form = fields.Char('43. ¿Cuál es la actividad secundaria de su negocio? (si la tiene)')
    x_desc_act_sec_inf = fields.Char('42. ¿Cuál es la actividad secundaria de su negocio? (si la tiene)')

    x_merca = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "¿Adquiere mercancía y comercializa con ella?",
    )

    x_ambula_inf = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Móvil'),
            ('51', 'Estacionario'),
            ('52', 'No aplica'),

        ], "43. Si el negocio es ambulante - sitio al descubierto, ¿cuál es su forma de funcionamiento? ",
    )

    x_ambula_2_inf = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Llega muy temprano'),
            ('51', 'Paga vigilancia'),
            ('52', 'Paga una cuota'),
            ('53', 'Le respetan el puesto'),
            ('54', 'Agrupado con otros vendedores'),
            ('55', 'Tiene carné'),
            ('56', 'No aplica'),
            ('57', 'Otro'),

        ], "44. Si el negocio es ambulante - sitio al descubierto, ¿cómo hace para conservar diariamente el mismo sitio de trabajo?",
    )

    x_ambula_2_cual = fields.Char('44.1. ¿Cuál?')

    x_mprima_inf = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Diariamente'),
            ('51', 'Semanalmente'),
            ('52', 'Quincenalmente'),
            ('53', 'Mensualmente'),

        ], "45. ¿Con qué frecuencia adquiere materia prima o mercancía para su negocio?",
    )

    x_mprima_form = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Diariamente'),
            ('51', 'Semanalmente'),
            ('52', 'Quincenalmente'),
            ('53', 'Mensualmente'),

        ], "44. ¿Con qué frecuencia adquiere materia prima o mercancía para su negocio?",
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
            ('50', 'Artículos de uso doméstico'),
            ('51', 'Ropa y calzado'),
            ('52', 'Artículos para empresas u oficinas'),
            ('53', 'Artículos para uso industrial'),
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

    x_clientes_form = fields.Integer(
        string="45. ¿Cuántos clientes atiende diariamente?",
        help="Ingrese un número entre 1 y 100",
    )

    x_clientes_inf = fields.Integer(
        string="46. ¿Cuántos clientes atiende diariamente?",
        help="Ingrese un número entre 1 y 100",
    )

    x_problema_inf = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Dificultad en obtener créditos'),
            ('51', 'Competencia excesiva'),
            ('52', 'Problemas de comercialización de productos'),
            ('53', 'Problemas con las autoridades'),
            ('54', 'No cuenta con las condiciones de bioseguridad que se requieren'),
            ('55', 'Aumento en el precio de los insumos'),
            ('56', 'Desconfianza de los clientes para adquirir productos de consumo'),
            ('57', 'Dificultad en la producción del producto'),
            ('58', 'No se encuentra virtualizado'),
            ('59', 'Falta de capacitación'),
            ('60', 'Falta de tecnología y conexión'),
            ('61', 'Normatividad, acreditación o certificación de su producto o servicio'),
            ('62', 'Otro'),

        ], "47. Seleccione el principal problema que usted tiene actualmente con su negocio?",
    )

    x_problema_inf_cual = fields.Char('47. ¿Cuál?')

    x_problema_form = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Dificultad en obtener creditos'),
            ('51', 'Competencia excesiva'),
            ('52', 'Problemas de comercialización de productos'),
            ('53', 'Problemas con las autoridades'),
            ('54', 'No cuenta con las condiciones de bioseguridad que se requieren'),
            ('55', 'Aumento en el precio de los insumos'),
            ('56', 'Desconfianza de los clientes para adquirir productos de consumo'),
            ('57', 'Dificultad en la producción del producto'),
            ('58', 'No se encuentra virtualizado'),
            ('59', 'Falta de capacitación'),
            ('60', 'Falta de tecnología y conexión'),
            ('61', 'Normatividad, acreditación o certificación de su producto o servicio'),
            ('62', 'Otro'),

        ], "46. Seleccione el principal problema que usted tiene actualmente con su negocio",
    )

    x_problema_otro_inf = fields.Char('47.1. ¿Cuál?')

    x_problema_otro_form = fields.Char('46.1. ¿Cuál?')

    x_prob_desc_form = fields.Char(
        string="47. Una vez seleccionado el principal problema del micronegocio, descríbalo en una frase",
    )

    x_prob_desc_inf = fields.Char(
        string="48. Una vez seleccionado el principal problema del micronegocio, descríbalo en una frase",
    )

    x_reinvierte_inf = fields.Integer(
        string="49. ¿Qúé porcentaje de las ventas reinvierte nuevamente en mercancía (1-100)?",
        help="Ingrese un número entre 1 y 100",
    )

    x_reinvierte_form = fields.Integer(
        string="48. ¿Qúé porcentaje de las ventas reinvierte nuevamente en mercancía (1-100)?",
        help="Ingrese un número entre 1 y 100",
    )

    #MÓDULO 3-PROTOCOLOS DE BIOSEGURIDAD(seccion 1 bioseguridad)
    x_dcont1 = fields.Boolean(
        string="Continuar con el Formulario",
    )

    x_proto1 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),

        ], "6. ¿Usted conoce los protocolos de bioseguridad para su negocio??",
    )

    x_proto2 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "7. ¿En su negocio implementa los protocolos de bioseguridad?",
    )

    x_proto3 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),

        ], "8. ¿Dispone de puntos de alcohol con una concentración no inferior al 70% para la higiene de las manos de los clientes y los trabajadores del negocio?",
    )

    x_proto4 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),

        ], "9. Dispone de la adecuada provision de tapabocas y elementos de protección para quienes laboran en el negocio?",
    )

    x_proto5 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),

        ], "5. ¿Se realiza cambio de tapabocas durante la jornada laboral?",
    )

    x_proto6 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('no_aplica', 'No Aplica'),

        ], "10. ¿Atiende a un cliente a la vez y mantiene el distanciamiento social?",
    )

    x_proto7 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('no_aplica', 'No Aplica'),

        ], "11. ¿Atiende de manera prioritaria a la población con riesgo del COVID19, para disminuir el tiempo que permenecen en el lugar?",
    )

    x_proto8 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('no_aplica', 'No Aplica'),

        ], "12. ¿Realiza la protección permanente de los alimentos en exhibición, con el uso de películas plásticas, tapas, vitrinas, etc?",
    )

    x_proto9 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),

        ], "13. ¿Dispone de superficies fáciles de limpiar y desinfectar para ubicar los productos?",
    )

    x_proto10 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),

        ], "14. ¿Desinfecta los objetos del local cuando son prestados a los clientes o proveedores (esferos, grapadora, etc.), antes y después de su uso?",
    )

    x_proto11 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),

        ], "15. ¿Coloca avisos o alertas para mantener las medidas de prevención?",
    )

    x_proto12 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('no_aplica', 'No Aplica'),

        ], "16. ¿Realiza la entrega de productos para llevar o consumir fuera del establecimiento?",
    )

    x_proto13 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),

        ], "17. ¿Limpia y desinfecta las herramientas de trabajo una vez finalice la jornada?",
    )

    x_proto14 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),

        ], "18. ¿Asegura que los colaboradores y los clientes usen tapabocas?",
    )

    x_proto15 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),

        ], "19. Realiza la limpieza del espacio de trabajo al menos dos vez al día?",
    )

    x_proto16 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),

        ], "20. ¿Entrega los productos sobre una superficie, sin tener contacto con el cliente?",
    )

    x_proto17 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),

        ], "17. ¿Ha recibido o recibe algun apoyo o beneficio económico por parte del Gobierno en la emergencia para usted?",
    )

    x_proto18 = fields.Many2many('model.manipulate.many2many', string="18. ¿Que tipo de beneficios?")

    #INNOVACION DEL MODELO DE NEGOCIO
    x_dcont2 = fields.Boolean(
        string="¿Desea continuar con el Formulario?",
    )
    #preguntas nuevas modelo de negocio
    model21 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "21. ¿Tiene identificados y caracterizados los segmentos de mercado objetivo de su negocio?",
    )
    model22 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "22. ¿Tiene definida con claridad y apropiadamente una propuesta de valor para  los segmentos de mercado objetivo de su negocio?",
    )
    model23 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "23. ¿Cumple la propuesta de valor definida para  los segmentos de mercado objetivo?",
    )
    model24 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "24. ¿Tiene identificados y en funcionamiento óptimo canales apropiados para comunicar la oferta a cada uno de sus segmentos de mercado objetivo?",
    )
    model25 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "25. ¿Tiene identificados y en funcionamiento óptimo canales apropiados para que cada uno de sus segmentos de mercado objetivo realice la compra y estos son competitivos con lo ofrecido por la competencia?",
    )
    model26 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "26. ¿Tiene identificados y en funcionamiento óptimo canales apropiados para realizar la entrega a cada uno de sus segmentos de mercado y estos son competitivos con lo ofrecido por la competencia??",
    )
    model27 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "27. ¿El servicio posventa es competitivo y se enfoca en las necesidades de cada uno de los segmentos de mercado?",
    )
    model28 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "28. ¿Los mecanismos de captación de clientes son apropiados desde la captación y el funcionamiento, y se enfocan en la caracteterísticas de cada segmento de mercado?",
    )
    model29 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "29. ¿Los mecanismos de fidelización de clientes son apropiados desde la captación y el funcionamiento, y se enfocan en la caracteterísticas de cada segmento de mercado?",
    )
    model30 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "30. ¿Los mecanismos de estimulación para el aumento de la compra en los clientes son apropiados desde la captación y el funcionamiento, y se enfocan en la caracteterísticas de cada segmento de mercado?",
    )
    model31 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "31. ¿Son claras las fuentes de ingreso y estas están verdaderamente basadas y enfocadas en el valor esperado por los clientes?",
    )
    model32 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "32. ¿El negocio tiene identificados los recursos requeridos para el perfecto funcionamiento del modelo de negocio y el cumplimiento de la propuesta de valor?",
    )
    model33 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "33. ¿El negocio cuenta con todos los recursos requeridos para el perfecto funcionamiento del modelo de negocio y el cumplimiento de la propuesta de valor?",
    )
    model34 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "34. ¿El negocio tiene identificadas las actividades claves para el perfecto funcionamiento del modelo de negocio y el cumplimiento de la propuesta de valor?",
    )
    model35 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "35. ¿Las actividades claves de la negocio hacen parte de procesos estandarizados y bien definidos?",
    )
    model36 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "36. ¿La negocio cuenta con acuerdos con proveedores y estos son suficientes y apropiados?",
    )
    model37 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "37. ¿El negocio cuenta con algún tipo de alianza para su desarrollo técnico?",
    )
    prodl39 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "39. ¿Cuenta con un espacio adecuado para la produccion y almacenamiento del producto, teniendo en cuenta medidas de higiene y de seguridad??",
    )

    prodl42 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "42. ¿Se tiene en el negocio definidos los estándares de los procesos de producción de los productos/servicios que vende?",
    )
    prodl43 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "43. ¿Tiene su negocio un sistema de control/ gestion de calidad adoptado e implementado?",
    )
    prodl46 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "46. ¿Sabe lo que le cuesta a su negocio la produccion y comercializacion del producto o servicio?",
    )
    prodl47 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "47. ¿sabe cuáles son los costos de cada etapa del proceso de producción?",
    )
    x_innova19 = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "19. ¿Conoce usted que es un  modelo de negocio?",
    )

    x_innova20 = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "20. ¿Se ha capacitado en la formación de modelos de negocio?",
    )

    x_innova21 = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "21. ¿Conoce los canales de distribución para su producto?",
    )

    x_innova22 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Canal Directo: Productor-Consumidor'),
            ('51', 'Canal Detallista: Productor-Minorista-Consumidor'),
            ('52', 'Canal Distribuidor:  Productor-Distribuidor-Minorista-Consumidor'),
            ('53', 'Canal Broker: Productor-Mayorista-Distribuidor-Minorista-Consumidor'),

        ], "22. ¿Cuál es el canal de distribución  que utiliza para su negocio?",
    )

    x_innova23 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Totalmente de acuerdo'),
            ('51', 'De acuerdo'),
            ('52', 'Ni de acuerdo, ni en desacuerdo'),
            ('53', 'En desacuerdo'),
            ('54', 'Totalmente en desacuerdo'),

        ], "23. ¿Considera que para la producción o manipulación del producto debe contar con personal capacitado?",
    )

    x_innova24 = fields.Selection(
        [('si', 'Si'),
         ('no', 'No'),
         ('en_proceso', 'En proceso'),
        ], "38. ¿Cuenta con personal capacitado para la producción o manipulación del producto?",
    )

    x_innova25 = fields.Selection(
        [('si', 'Si'),
         ('no', 'No'),
        ], "39. ¿Cuenta con un espacio adecuado para la producción y almacenamiento del producto, teniendo en cuenta medidas de higiene y de seguridad?",
    )

    x_innova26 = fields.Selection(
        [
          ('si', 'Si'),
          ('no', 'No'),
          ('en_proceso', 'En proceso'),
        ], "40. ¿Tiene implementado un proceso de buenas practicas de manipulacion y produccion ?",
    )

    x_innova27 = fields.Selection(
        [('si', 'Si'),
         ('no', 'No'),
        ], "41. ¿Para la obtención de la materia prima o mercancía depende de un solo proveedor?",
    )

    x_innova28 = fields.Selection(
        [('50', 'De contado'),
         ('51', 'A crédito'),
         ('52', 'A plazos'),

        ], "28. El pago de la materia prima la realiza ",
    )

    x_innova29 = fields.Selection(
        [('si', 'Si'),
          ('no', 'No'),
          ('en_proceso', 'En proceso'),
        ], "44. ¿Ha representado retrasos en la entrega de su producto por falta de materia prima o mercancia?",
    )
    x_innova30 = fields.Selection(
        #string="Sexo",
        [('50', 'Totalmente de acuerdo'),
         ('51', 'De acuerdo'),
         ('52', 'Ni de acuerdo, ni en desacuerdo'),
         ('53', 'En desacuerdo'),
         ('54', 'Totalmente en desacuerdo'),

        ], "30. ¿Considera que la estandarización de procesos para la producción ó manipulación del producto permiten agilizar los tiempos de entrega?",
    )

    x_innova31 = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "31. ¿Cuenta con un proceso estandarizado para la producción o manipulación del producto?",
    )

    x_innova32 = fields.Selection(
        #string="Sexo",
        [('50', 'Totalmente de acuerdo'),
         ('51', 'De acuerdo'),
         ('52', 'Ni de acuerdo, ni en desacuerdo'),
         ('53', 'En desacuerdo'),
         ('54', 'Totalmente en desacuerdo'),

        ], "32. ¿Considera qué en el inventario se llevan los registros de las entradas y salidas del producto?",
    )

    x_innova33 = fields.Selection(
        [('si', 'Si'),
         ('no', 'No'),
         ('en_proceso', 'En proceso'),
        ], "45. ¿Cuenta con un inventario donde registre las entradas y salidas del producto?",
    )

    x_innova34 = fields.Integer(
        string="34. ¿Cuántas líneas de producto tiene su negocio?",
    )

    x_innova35 = fields.Char(
        string="35. Describa las líneas de producto que tiene su negocio",
    )

    x_innova36 = fields.Selection(
        [('si', 'Si'),
         ('no', 'No')
        ], "46. ¿Sabe lo qué le cuesta a su negocio la producción y comercialización del producto o servicio?",
    )

    x_innova37 = fields.Selection(
        #string="Sexo",
        [('50', 'Por el mercado'),
         ('51', 'Por el punto de equilibrio'),
         ('52', 'Costos fijos + variables + costos de utilidad'),

        ], "37. ¿Como define el  precio de venta de su producto o servicio? ",
    )

    x_innova38 = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "38. ¿Conoce qué es el punto de equilibrio?",
    )

    x_innova39 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "48. ¿Sabe cual es el punto de equilibrio de su negocio?",
    )
    x_innova40 = fields.Selection(
        [('si', 'Si'),
         ('no', 'No'),
        ], "50. ¿En el último año ha realizado actividades de innovación para su negocio?",
    )
    ninova50 = fields.Selection(
        [('si', 'Si'),
         ('no', 'No')
        ], "46. ¿se generan espacios para  fomentar la Creatividad y la generación de ideas  innovadoras?",
    )
    ninova52 = fields.Selection(
        [('si', 'Si'),
         ('no', 'No'),
         ('en_proceso', 'En proceso'),
        ], "52. ¿El negocio ha recibido transferencias de tecnologias o de conocimientos para mejorar sus procesos, productos o servicios?",
    )
    ninova53 = fields.Text( string="53. ¿Cuales?",readonly=False)
    ninova54 = fields.Selection(
        [('si', 'Si'),
         ('no', 'No'),
         ('en_proceso', 'En proceso'),
        ], "54. ¿La negocio ha desarrollado nuevos servicios o productos en los ultimos 2 años?",
    )
    x_innova41_inf = fields.Selection(
        [('si', 'Si'),
         ('no', 'No'),
        ], "41. ¿Realiza actividades con los trabajadores para crear innovaciones en su negocio?",
    )

    x_innova41_form = fields.Selection(
        #string="Sexo",
        [('50', 'Totalmente de acuerdo'),
         ('51', 'De acuerdo'),
         ('52', 'Ni de acuerdo, ni en desacuerdo'),
         ('53', 'En desacuerdo'),
         ('54', 'Totalmente en desacuerdo'),

        ], "41. ¿Cree qué capacitar a sus trabajadores puede aumentar los resultados de su negocio?",
    )

    x_innova42_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "42. ¿Ha recibido formación en creatividad e innovación? ",
    )

    x_innova42_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "42. ¿Realiza actividades con los trabajadores para crear innovaciones en su negocio?",
    )

    x_innova43_inf = fields.Selection(
        [('si', 'Si'),
         ('no', 'No'),
        ], "51. ¿Ofrece con frecuencia productos o servicios nuevos a partir de sugerencias de sus clientes?",
    )

    x_innova43_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "43. ¿Ha recibido formación en creatividad e innovación? ",
    )

    x_innova44_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "44. ¿Desarrolla o paga para innovar la forma en la que vende sus producto o servicios? (diseño, envase, promoción, forma de cotizar, etc.)",
    )

    x_innova44_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "44. ¿Ofrece con frecuencia productos o servicios nuevos a partir de sugerencias de sus clientes?",
    )

    x_innova45_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "45. ¿Desarrolla o paga para innovar la forma en la que vende sus producto o servicios? (diseño, envase, promoción, forma de cotizar, etc.)",
    )
    #gavii
#FORMALIZACION SECCION 3: ADMINISTRACION
    x_dcont3 = fields.Boolean(
        string="Continuar con el Formulario",
    )
    for55 = fields.Selection(
        [('si', 'Si'),
         ('no', 'No'),
         ('en_proceso', 'En proceso'),
        ], "55. ¿Su negocio está legalmente constituido?",
    )
    x_forma45_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "45. ¿Considera que al realizar un análisis interno y externo de su negocio, permitirá la identificación de debilidades, oportunidades,fortalezas y amenazas?",
    )

    x_forma46_form = fields.Selection(
        #string="Sexo",
        [('1', 'Totalmente de acuerdo'),
         ('2', 'De  acuerdo'),
         ('3', 'Ni de acuerdo, ni en desacuerdo'),
         ('4', 'En desacuerdo'),
         ('5', 'Totalmente en desacuerdo'),

        ], "46. ¿Considera que al realizar un análisis interno y externo de su negocio, permitirá la identificación de debilidades, oportunidades,fortalezas y amenazas?",
    )

    x_forma46_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "46. ¿Sabe cómo realizar un análisis interno de su negocio?",
    )

    x_forma47_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "47. ¿Sabe cómo realizar un análisis interno de su negocio?",
    )

    x_forma47_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "47. ¿Sabe cómo realizar un análisis externo de su negocio?",
    )

    x_forma48_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "48. ¿Sabe como realizar un análisis externo de su negocio?",
    )

    x_forma48_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "48. ¿Ha pensado en formalizar su negocio?",
    )

    x_forma49_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "49. ¿Tiene claro la proyección de su negocio a corto, mediano y largo plazo?",
    )

    x_forma49_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "49. ¿Para usted es importante la formalización de su negocio?",
    )

    x_forma50_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "50. ¿Toma medidas para desarrollar una cultura de la organización?",
    )

    x_forma50_inf = fields.Selection(
        [('si', 'Si'),
         ('no', 'No'),
         ('en_proceso','En proceso')
        ], "56. ¿Tiene su negocio un registro mercantil?",
    )

    x_forma51_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "51. ¿Conoce las normas y estándares de calidad para productos y servicios?",
    )

    x_forma51_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "51. ¿se encuentra actualizado?",
    )

    x_forma52_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "52. ¿Cuenta con alguna norma o estandar que certifique la calidad del producto o servicio que usted ofrece?",
    )

    x_forma52_inf = fields.Selection(
        [('si', 'Si'),
         ('no', 'No'),
         ('en_proceso','En proceso')
        ], "57. ¿Tiene este negocio RUT (Registro Único Tributario)?",
    )

    x_forma53_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "53. ¿Expedir factura permite que los clientes tengan mayor confianza y seguridad al momento de comprar sus productos o servicios?",
    )

    x_forma53_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "53. ¿Se encuentra actualizado?",
    )

    x_forma54_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "54. ¿Expide factura?",
    )

    x_forma54_inf = fields.Selection(
        [('si', 'Si'),
         ('no', 'No'),
         ('en_proceso','En proceso')
        ], "58. ¿Tiene este negocio NIT (Número de Identificación Tributaria?",
    )

    x_forma55_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "55. ¿Expide facturación electrónica?",
    )

    x_forma55_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "55. ¿Se encuentra actualizado?",
    )

    x_forma56_form = fields.Selection(
        #string="Sexo",
        [('1', 'Totalmente de acuerdo'),
         ('2', 'De  acuerdo'),
         ('3', 'Ni de acuerdo, ni en desacuerdo'),
         ('4', 'En desacuerdo'),
         ('5', 'Totalmente en desacuerdo'),

        ], "56. ¿Considera que se debe tener claridad de los impuestos presentados por su actividad económica y las frecuencias en que debe pagar?",
    )

    x_forma56_inf = fields.Selection(
        [('si', 'Si'),
         ('no', 'No'),
         ('en_proceso','En proceso')
        ], "59. Para el funcionamiento del negocio: ¿Requiere algún permiso municipal/distrital adicional para funcionar?",
    )
    n_los_empl = fields.Selection(
        [('si', 'Si'),
         ('no', 'No'),
         ('en_proceso','En proceso')
        ], "60. ¿Los empleados reciben beneficios laborales de conformidad a la Ley? ",
    )

    x_forma57_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "57. ¿Ha tenido que reducir la cantidad de sus trabajadores por consecuencias de la pandemia?",
    )

    x_forma57_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "57. ¿Cuenta actualmente con el permiso municipal/distrital adicional para funcionar?",
    )

    x_forma58_form = fields.Selection(
        [  ('1', '1'),
           ('2', '2'),
           ('3', '3'),
           ('4', '4'),
           ('5', '5'),
           ('6', '6'),
           ('7', '7'),
           ('8', '8'),
           ('9', '9'),
        ], "2. Antes de la pandemia COVID-19 ¿Cuántas personas de su familia trabajaban con usted en el negocio?",
    )
    x_forma58_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "58. ¿Expedir factura permite que los clientes tengan mayor confianza y seguridad al momento de comprar sus productos o servicios?",
    )

    x_forma59_form = fields.Integer(
        string="59. Antes de la pandemia COVID-19 ¿Cuántas personas QUE NO SON de su familia trabajaban con usted en el negocio?",
    )

    x_forma59_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "59. ¿Expide factura?",
    )

    x_forma60_form = fields.Selection(
        [  ('1', '1'),
           ('2', '2'),
           ('3', '3'),
           ('4', '4'),
           ('5', '5'),
           ('6', '6'),
           ('7', '7'),
           ('8', '8'),
           ('9', '9'),
        ], "4. ¿Cuántas personas de su familia trabajan actualmente con usted en el negocio?",
    )

    x_forma60_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "60. ¿Considera que se debe tener claridad de los impuestos presentados por su actividad económica y las frecuencias en que debe pagar?",
    )

    x_forma61_form = fields.Selection(
        [  ('1', '1'),
           ('2', '2'),
           ('3', '3'),
           ('4', '4'),
           ('5', '5'),
           ('6', '6'),
           ('7', '7'),
           ('8', '8'),
           ('9', '9'),
        ],"3. Antes de la pandemia COVID-19 ¿Cuántas personas QUE NO SON de su familia trabajan actualmente con usted en el negocio?",
    )

    x_forma61_inf = fields.Selection(
        #string="Sexo",
        [('60', 'Si'),
         ('61', 'No'),

        ], "61. ¿Ha tenido que reducir la cantidad de sus trabajadores por consecuencias de la pandemia?",
    )

    x_forma62_form = fields.Selection(
        #string="Sexo",
        [('60', 'Contrato a término fijo'),
         ('61', 'Contrato a término indefinido'),
         ('62', 'Contrato por obra o labor'),

        ], "62. ¿Qué tipo de contrato aplica más para los trabajadores de su negocio?",
    )

    x_forma62_inf = fields.Integer(
        string="62. Antes de la pandemia COVID-19 ¿Cuántas personas de su familia trabajaban con usted en el negocio?",
    )

    x_forma63_form = fields.Selection(
        #string="Sexo",
        [('50', 'Pago por hora'),
         ('51', 'Pago diario'),
         ('52', 'Pago semanal'),
         ('53', 'Pago quincenal'),
         ('54', 'Pago mensual'),

        ], "63. ¿Si tiene trabajadores como es el sistema de remuneración?  ",
    )

    x_forma63_inf = fields.Integer(
        string="63. Antes de la pandemia COVID-19 ¿Cuántas personas QUE NO SON de su familia trabajaban con usted en el negocio?",
    )

    x_forma64_form = fields.Selection(
        #string="Sexo",
        [('1', 'Totalmente de acuerdo'),
         ('2', 'De  acuerdo'),
         ('3', 'Ni de acuerdo, ni en desacuerdo'),
         ('4', 'En desacuerdo'),
         ('5', 'Totalmente en desacuerdo'),

        ], "64. ¿Considera importante para su negocio conocer y aplicar las obligaciones correspondientes para los trabajadores que laboran en su negocio?",
    )

    x_forma64_inf = fields.Integer(
        string="64. ¿Cuántas personas de su familia trabajan actualmente con usted en el negocio?",
    )

    x_forma65_inf = fields.Selection(
        [  ('1', '1'),
           ('2', '2'),
           ('3', '3'),
           ('4', '4'),
           ('5', '5'),
           ('6', '6'),
           ('7', '7'),
           ('8', '8'),
           ('9', '9'),
        ], "5. ¿Cuántas personas QUE NO SON de su familia trabajan actualmente con usted en el negocio?",
    )
    
    x_forma66_inf = fields.Selection(
        [('50', 'Pago por hora'),
         ('51', 'Pago diario'),
         ('52', 'Pago semanal'),
         ('53', 'Pago quincenal'),
         ('54', 'Pago mensual'),
         ('55', 'Labor o pieza'),
         ('55', 'Sin remuneracion'),

        ], "66. ¿Si tiene trabajadores como es el sistema de remuneración?  ",
    )

    x_forma67_inf = fields.Selection(
        #string="Sexo",
        [('1', 'Totalmente de acuerdo'),
         ('2', 'De  acuerdo'),
         ('3', 'Ni de acuerdo, ni en desacuerdo'),
         ('4', 'En desacuerdo'),
         ('5', 'Totalmente en desacuerdo'),

        ], "67. ¿Considera importante para su negocio conocer y aplicar las obligaciones correspondientes para los trabajadores que laboran en su negocio?",
    )

    x_dcont4 = fields.Boolean(
        string="Continuar con el Formulario",
    )

    x_merc65_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "65. ¿Utiliza alguna estrategia para comercializar sus productos?",
    )

    x_merc68_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "68. ¿Utiliza alguna estrategia para comercializar sus productos?",
    )

    x_merc66_form = fields.Char(
        string="66. ¿Cuál es la estrategia que utiliza para comercializar sus productos o servicios?",
        help="Escriba su estrategia", 
    )

    x_merc69_inf = fields.Char(
        string="69. ¿Cuál es la estrategia que utiliza para comercializar sus productos o servicios?",
        help="Escriba su estrategia", 
    )

    x_merc67_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "67. ¿Utiliza alguna estrategia para la visibilización de sus productos?",
    )

    x_merc70_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "70. ¿Utiliza alguna estrategia para la visibilización de sus productos?",
    )

    x_merc68_form = fields.Char(
        string="68. ¿Cuál es la estrategia que utiliza para la visibilización de sus productos o servicios?",
        help="Escriba su respuesta", 
    )

    x_merc71_inf = fields.Char(
        string="71. ¿Cuál es la estrategia que utiliza para la visibilización de sus productos o servicios?",
        help="Escriba su respuesta", 
    )

    x_merc69_form = fields.Many2many('model.form.many2many', string = "69. ¿Que medios electrónicos utiliza?")

    x_merc72_inf = fields.Many2many('model.inf.many2many', string = "72. ¿Que medios electrónicos utiliza?")
    
    x_merc70_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "70. Para realizar las actividades propias de su negocio, ¿utiliza Internet?",
    )

    x_merc73_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "73. Para realizar las actividades propias de su negocio, ¿utiliza Internet?",
    )

    x_merc71_form = fields.Selection(
        #string="Sexo",
        [('1', 'Totalmente de acuerdo'),
         ('2', 'De  acuerdo'),
         ('3', 'Ni de acuerdo, ni en desacuerdo'),
         ('4', 'En desacuerdo'),
         ('5', 'Totalmente en desacuerdo'),

        ], "71. ¿Considera que las redes sociales permite mejorar la competitividad de su negocio? ",
    )

    x_merc74_inf = fields.Selection(
        #string="Sexo",
        [('1', 'Totalmente de acuerdo'),
         ('2', 'De  acuerdo'),
         ('3', 'Ni de acuerdo, ni en desacuerdo'),
         ('4', 'En desacuerdo'),
         ('5', 'Totalmente en desacuerdo'),

        ], "74. ¿Considera que las redes sociales permite mejorar la competitividad de su negocio? ",
    )

    x_merc72_form = fields.Many2many('model.many2many72', string="72. ¿Qué redes sociales utiliza para su negocio?")

    x_merc75_inf = fields.Many2many('model.many2many75', string="75. ¿Qué redes sociales utiliza para su negocio? ")

    x_merc76_inf = fields.Many2many('model.many2many76', string="76. ¿Qué actividades propias de su negocio realiza a través de internet?")

    #x_merc75_inf = fields.Selection(
        #string="Sexo",
     #   [('1', 'WhatsApp'),
        # ('2', 'Facebook'),
      #   ('3', 'Twitter'),
       #  ('4', 'Instagram'),
        # ('5', 'Youtube'),
        # ('6', 'Todas las anteriores'),
        # ('7', 'Ninguna de las anteriores'),

        #], "75. ¿Qué redes sociales utiliza para su negocio? ",
    #)
    
    x_merc73_form = fields.Many2many('model.many2many73', string="73. ¿Qué actividades propias de su negocio realiza a través de internet?")

    #x_merc76_inf = fields.Selection(
        #string="Sexo",
     #   [('1', 'Pago a proveedores'),
      #   ('2', 'Recaudo de ventas'),
       #  ('3', 'Consignaciones a terceros'),
       #  ('4', 'Transferencias'),
        # ('5', 'Todas las anteriores'),

     #   ], "76. ¿Qué actividades propias de su negocio realiza a través de internet? ",
    #)#

    x_merc74_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "74. ¿Realiza procesos de seguimiento y fidelización de clientes (Servicio Post-venta)?",
    )

    x_merc77_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "77. ¿Realiza procesos de seguimiento y fidelización de clientes (Servicio Post-venta)?",
    )

    x_merc75_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "75. ¿Sus productos o servicios cuentan con una marca que los diferencie?",
    )

    x_merc78_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "78. ¿Sus productos o servicios cuentan con una marca que los diferencie?",
    )

    x_merc76_form = fields.Many2many('model.many2many176', string="76. ¿Cuál es la forma de pago que más utilizan los clientes en su negocio?")

    #x_merc76_form = fields.Selection(
     #   #string="Sexo",
      #  [('50', 'De contado'),
       #  ('51', 'A crédito o a plazos'),
       #  ('52', 'Transferencia'),
       #  ('53', 'Tarjeta de débito o crédito'),
       #  ('54', 'Cheque'),

        #], "76. ¿Cuál es la forma de pago que más utilizan los clientes en su negocio? ",
    #)

    x_merc79_inf = fields.Selection(
        #string="Sexo",
        [('50', 'De contado'),
         ('51', 'A crédito o a plazos'),
         ('52', 'Transferencia'),
         ('53', 'Tarjeta de débito o crédito'),
         ('54', 'Cheque'),

        ], "79. ¿Cuál es la forma de pago que más utilizan los clientes en su negocio? ",
    )

    x_merc77_form = fields.Many2many('model.many2many177', string="77. ¿Cuál es la forma de pago que más utiliza para comprar insumo, materia prima o pagar obligaciones? ")

    #x_merc77_form = fields.Selection(
        #string="Sexo",
     #   [('50', 'De contado'),
      #   ('51', 'A crédito o a plazos'),
       #  ('52', 'Transferencia'),
        # ('53', 'Tarjeta de débito o crédito'),
       #  ('54', 'Cheque'),

        #3], "77. ¿Cuál es la forma de pago que más utiliza para comprar insumo, materia prima o pagar obligaciones? ",
    #)

    x_merc80_inf = fields.Selection(
        [('50', 'De contado'),
         ('51', 'A crédito o a plazos'),
         ('52', 'Transferencia'),
         ('53', 'Tarjeta de débito o crédito'),
         ('54', 'Cheque'),

        ], "80. ¿Cuál es la forma de pago que más utiliza para comprar insumo, materia prima o pagar obligaciones? ",
    )
    #actualizacion y cambio de vista
    x_merc78_form = fields.Selection(
        [('de_0_a_500', 'De $0 a $500.000'),
         ('de_500_a_1000', 'De $500.000 a $1´000.000'),
         ('de_1000_a_3000', 'De $1´000.000 a $3´000.000'),
         ('de_3000_a_6000', 'De $3´000.000 a $6´000.000'),
         ('de_6000_a_10000', 'De $6´000.000 a $10´000.000'),
         ('mas_de_10000','Mas de $10´000.000')
        ], "26. Durante la pandemia COVID-19, en una semana buena ¿donde se ubica sus ventas dentro de los siguientes rangos?",
    )

    x_merc81_inf = fields.Integer(
        string="81. ¿Cuál es su promedio de ventas ACTUAL en una semana BUENA?",
        help="", 
    )

    x_merc79_form = fields.Selection(
        [('de_0_a_500', 'De $0 a $500.000'),
         ('de_500_a_1000', 'De $500.000 a $1´000.000'),
         ('de_1000_a_3000', 'De $1´000.000 a $3´000.000'),
         ('de_3000_a_6000', 'De $3´000.000 a $6´000.000'),
         ('de_6000_a_10000', 'De $6´000.000 a $10´000.000'),
         ('mas_de_10000','Mas de $10´000.000')
        ], "28. Durante la pandemia COVID-19, en una semana normal ¿donde se ubica sus ventas dentro de los siguientes rangos?",
    )

    x_merc82_inf = fields.Integer(
        string="82. ¿Cuál es su promedio de ventas ACTUAL en una semana NORMAL?",
        help="", 
    )

    x_merc80_form = fields.Selection(
        [('de_0_a_500', 'De $0 a $500.000'),
         ('de_500_a_1000', 'De $500.000 a $1´000.000'),
         ('de_1000_a_3000', 'De $1´000.000 a $3´000.000'),
         ('de_3000_a_6000', 'De $3´000.000 a $6´000.000'),
         ('de_6000_a_10000', 'De $6´000.000 a $10´000.000'),
         ('mas_de_10000','Mas de $10´000.000')
        ], "27. Antes de la pandemia COVID-19, en una semana buena ¿donde se ubica sus ventas dentro de los siguientes rangos?",
    )

    x_merc83_inf = fields.Integer(
        string="83. Antes de la pandemia COVID-19 ¿Cuál era su promedio de ventas en una semana BUENA?",
        help="", 
    )

    x_merc81_form = fields.Selection(
        [('de_0_a_500', 'De $0 a $500.000'),
         ('de_500_a_1000', 'De $500.000 a $1´000.000'),
         ('de_1000_a_3000', 'De $1´000.000 a $3´000.000'),
         ('de_3000_a_6000', 'De $3´000.000 a $6´000.000'),
         ('de_6000_a_10000', 'De $6´000.000 a $10´000.000'),
         ('mas_de_10000','Mas de $10´000.000')
        ], "29. Antes de la pandemia COVID-19, en una semana normal ¿donde se ubica sus ventas dentro de los siguientes rangos?",
    )

    x_merc84_inf = fields.Integer(
        string="84. Antes de la pandemia COVID-19 ¿Cuál era su promedio de ventas en una semana NORMAL?",
        help="", 
    )

    x_merc82_form = fields.Selection(
        [('1', 'Totalmente de acuerdo'),
         ('2', 'De  acuerdo'),
         ('3', 'Ni de acuerdo, ni en desacuerdo'),
         ('4', 'En desacuerdo'),
         ('5', 'Totalmente en desacuerdo'),

        ], "82. ¿El grado de satisfacción de sus clientes con el producto o servicio que usted ofrece le ha permitido mejorar sus ventas?",
    )

    x_merc85_inf = fields.Selection(
        #string="Sexo",
        [('1', 'Totalmente de acuerdo'),
         ('2', 'De  acuerdo'),
         ('3', 'Ni de acuerdo, ni en desacuerdo'),
         ('4', 'En desacuerdo'),
         ('5', 'Totalmente en desacuerdo'),

        ], "85. ¿El grado de satisfacción de sus clientes con el producto o servicio que usted ofrece le ha permitido mejorar sus ventas? ",
    )

    x_merc83_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "83. ¿Ha realizado actividades para detectar y vincular nuevos clientes a su negocio?",
    )

    x_merc86_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "86. ¿Ha realizado actividades para detectar y vincular nuevos clientes a su negocio?",
    )

    x_merc84_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "84. ¿Ha realizado actividades para promocionar las ventas de los productos o servicios que ofrece en su negocio?",
    )

    x_merc87_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "87. ¿Ha realizado actividades para promocionar las ventas de los productos o servicios que ofrece en su negocio?",
    )

    x_merc85_form = fields.Selection(
        #string="Sexo",
        [('1', 'Totalmente de acuerdo'),
         ('2', 'De  acuerdo'),
         ('3', 'Ni de acuerdo, ni en desacuerdo'),
         ('4', 'En desacuerdo'),
         ('5', 'Totalmente en desacuerdo'),

        ], "85. ¿Considera importante realizar descuentos a los clientes para cerrar las ventas?",
    )

    x_merc88_inf = fields.Selection(
        #string="Sexo",
        [('1', 'Totalmente de acuerdo'),
         ('2', 'De  acuerdo'),
         ('3', 'Ni de acuerdo, ni en desacuerdo'),
         ('4', 'En desacuerdo'),
         ('5', 'Totalmente en desacuerdo'),

        ], "88. ¿Considera importante realizar descuentos a los clientes para cerrar las ventas?",
    )

    x_merc86_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "86. ¿Su negocio depende de ventas de temporada?",
    )

    x_merc89_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "89. ¿Su negocio depende de ventas de temporada?",
    )

    x_merc87_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "87. ¿Vende mas o menos lo mismo durante la mayoría del año?",
    )

    x_merc90_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "90. ¿Vende mas o menos lo mismo durante la mayoría del año?",
    )

    #FINANZAS

    x_dcont5 = fields.Boolean(
        string="Continuar con el Formulario",
    )

    x_finan88_form = fields.Selection(
        [('50', 'Si'),
         ('51', 'No'),

        ], "88. Lleva los registros contables del negocio",
    )

    x_finan91_inf = fields.Selection(
        [('50', 'Si'),
         ('51', 'No'),

        ], "91. Lleva los registros contables del negocio",
    )

    x_finan92_inf = fields.Selection(
        [('50', 'Totalmente de acuerdo'),
         ('51', 'De acuerdo'),
         ('52', 'Ni de acuerdo, ni en desacuerdo'),
         ('53', 'En desacuerdo'),
         ('54', 'Totalmente en desacuerdo'),

        ], "92. ¿Considera que debe mejorar la manera en la que lleva el registro contable del negocio?",
    )

    x_finan89_form = fields.Selection(
        [('50', 'Contabilidad formal (libro de compras y venta,estados de resultados, etc.)'),
         ('51', 'Registros personales'),
         ('52', 'Contabilidad electrónica'),

        ], "89. ¿De qué manera lleva los registros contables del negocio?",
    )

    x_finan90_form = fields.Selection(
        [('50', 'Cuento con los servicios remunerados de un contador'),
         ('51', 'Cuento con la ayuda de un contador amigo o familiar (no remunerado)'),
         ('52', 'Me ayuda un consultorio empresarial u otra institución'),
         ('53', 'Me ayuda un familiar, amigo o asesor con experiencia'),
         ('54', 'Ninguna')


        ], "90. ¿Cuenta usted con asesoría para llevar las cuentas?",
    )

    x_finan91_form = fields.Selection(
        [('50', 'Si'),
         ('51', 'No'),

        ], "91. ¿Tiene claridad el margen de utilidad que genera su negocio?",
    )

    x_finan92_form = fields.Selection(
        [('50', 'Si'),
         ('51', 'No'),

        ], "92. ¿Tiene la cultura de ahorrar o invertir las ganancias de su negocio? ",
    )

    x_finan93_form = fields.Selection(
        #string="Sexo",
        [('50', 'Totalmente de acuerdo'),
         ('51', 'De acuerdo'),
         ('52', 'Ni de acuerdo, ni en desacuerdo'),
         ('53', 'En desacuerdo'),
         ('54', 'Totalmente en desacuerdo'),

        ], "93. ¿Considera qué a través de la contabilidad puede diferenciar los gastos de su negocio de los gastos de su hogar?",
    )

    x_finan94_form = fields.Selection(
        [('50', 'Si'),
         ('51', 'No'),

        ], "94. ¿Usted ha tenido acceso durante los últimos 12 meses algún tipo de crédito para invertirlo en su negocio?",
    )

    x_finan95_form = fields.Selection(
        #string="Sexo",
        [('50', 'Capital de trabajo '),
         ('51', 'Remodelaciones o adecuaciones'),
         ('52', 'Pago de nómina'),
         ('53', 'Compra o arriendo de maquinaria '),
         ('54', 'Otro'),

        ], "95. ¿A qué destino el crédito solicitado?",
    )

    x_finan96_form = fields.Selection(
        #string="Sexo",
        [('50', 'No lo necesita/No le gusta pedir prestamos'),
         ('51', 'No sabe dónde acudir'),
         ('52', 'Desconoce el procedimiento para solicitarlo'),
         ('53', 'No se lo otorgarían (no cree cumplir con los requerimientos: garantías, codeudores, avales, fiadores)'),
         ('54', 'No confía en las instituciones financieras'),
         ('55', 'No entiende las condiciones asociadas a un crédito (tasa de interés, plazos, cuotas, etc.)'),
         ('56', 'Está reportado en Centrales de Riesgo'),

        ], "96. ¿Cuál es la razón principal de que no haya solicitado un crédito?",
    )

    x_finan97_form = fields.Selection(
        #string="Sexo",
        [('50', 'No lo necesita/No le gusta pedir prestamos'),
         ('51', 'No sabe dónde acudir'),
         ('52', 'Desconoce el procedimiento para solicitarlo'),
         ('53', 'No se lo otorgarían (no cree cumplir con los requerimientos: garantías, codeudores, avales, fiadores)'),
         ('54', 'No confía en las instituciones financieras'),
         ('55', 'No entiende las condiciones asociadas a un crédito (tasa de interés, plazos, cuotas, etc.)'),
         ('56', 'Está reportado en Centrales de Riesgo'),

        ], "97. ¿Cuál es la razón secundaria de que no haya solicitado un crédito?",
    )

    x_finan98_form = fields.Selection(
        [('50', 'Si'),
         ('51', 'No'),

        ], "98. ¿Acude al fenómeno gota gota para financiar su negocio?",
    )

    x_finan99_form = fields.Selection(
        #string="Sexo",
        [('50', 'Totalmente de acuerdo'),
         ('51', 'De acuerdo'),
         ('52', 'Ni de acuerdo, ni en desacuerdo'),
         ('53', 'En desacuerdo'),
         ('54', 'Totalmente en desacuerdo'),

        ], "99. ¿Considera qué los ingresos del negocio son suficientes para cubrir los gastos y costos en que incurrre el negocio?",
    )

    x_finan100_form = fields.Selection(
        #string="Sexo",
        [('50', 'Cuenta de ahorros'),
         ('51', 'Cuenta corriente'),
         ('52', 'Tarjetas de Crédito'),
         ('53', 'Billeteras electrónicas'),
         ('54', 'Créditos'),
         ('55', 'Seguros'),
         ('56', 'Ninguna de las anteriores'),

        ], "100. Seleccione los productos financieros que utiliza su negocio",
    )

    x_finan101_form = fields.Selection(
        [('50', 'Si'),
         ('51', 'No'),

        ], "101. ¿Necesita acceder a servicios y productos financieros para cubrir los gastos de materia prima, salarios, entre otros?",
    )

    x_finan102_form = fields.Selection(
        #string="Sexo",
        [('50', 'Totalmente de acuerdo'),
         ('51', 'De acuerdo'),
         ('52', 'Ni de acuerdo, ni en desacuerdo'),
         ('53', 'En desacuerdo'),
         ('54', 'Totalmente en desacuerdo'),

        ], "102. ¿Considera qué los gastos fijos y los gastos financieros consumen las ganancias de su negocio?",
    )

    x_finan103_form = fields.Selection(
        #string="Sexo",
        [('50', 'Totalmente de acuerdo'),
         ('51', 'De acuerdo'),
         ('52', 'Ni de acuerdo, ni en desacuerdo'),
         ('53', 'En desacuerdo'),
         ('54', 'Totalmente en desacuerdo'),

        ], "103. ¿Considera importante tener los ahorros del negocio en cuentas bancarias?",
    )

    x_finan104_form = fields.Selection(
        [('50', 'Si'),
         ('51', 'No'),

        ], "104. ¿Tiene cuentas bancarias del negocio?",
    )

    x_finan105_form = fields.Selection(
        #string="Sexo",
        [('50', 'No la necesita/ No le interesa'),
         ('51', 'No sabe'),
         ('52', 'Desconoce el procedimiento para solicitar una cuenta bancaria'),
         ('53', 'Los intereses y comisiones son muy altos'),
         ('54', 'No cumple con los requerimientos'),
         ('55', 'Está reportado en Centrales de Riesgo'),

        ], "105. ¿Cuál es la razón para que no tenga una cuenta de ahorros o una cuenta corriente para su negocio?",
    )

    x_finan106_form = fields.Selection(
        [('50', 'Si'),
         ('51', 'No'),

        ], "106. ¿Sabe qué son las billeteras electrónicas?",
    )

    x_finan107_form = fields.Selection(
        #string="Sexo",
        [('50', 'Totalmente de acuerdo'),
         ('51', 'De acuerdo'),
         ('52', 'Ni de acuerdo, ni en desacuerdo'),
         ('53', 'En desacuerdo'),
         ('54', 'Totalmente en desacuerdo'),

        ], "107. ¿Considera importante el uso de las billeteras electrónicas para el negocio?",
    )

    x_finan108_form = fields.Selection(
        [('50', 'Si'),
         ('51', 'No'),

        ], "108. ¿En su negocio utiliza billeteras electrónicas?",
    )

    x_finan93_inf = fields.Selection(
        [('50', 'Si'),
         ('51', 'No'),

        ], "93. ¿Tiene claridad el margen de utilidad que genera su negocio?",
    )

    x_finan94_inf = fields.Selection(
        [('50', 'Si'),
         ('51', 'No'),

        ], "94. ¿Tiene la cultura de ahorrar o invertir las ganancias de su negocio? ",
    )

    x_finan95_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Totalmente de acuerdo'),
         ('51', 'De acuerdo'),
         ('52', 'Ni de acuerdo, ni en desacuerdo'),
         ('53', 'En desacuerdo'),
         ('54', 'Totalmente en desacuerdo'),

        ], "95. ¿Considera que a través de la contabilidad puede diferenciar los gastos de su negocio de los gastos de su hogar?",
    )

    x_finan96_inf = fields.Selection(
        [('50', 'Si'),
         ('51', 'No'),

        ], "96. ¿Usted ha tenido acceso durante los últimos 12 meses algún tipo de crédito para invertirlo en su negocio?",
    )

    x_finan97_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Capital de trabajo '),
         ('51', 'Remodelaciones o adecuaciones'),
         ('52', 'Pago de nómina'),
         ('53', 'Compra o arriendo de maquinaria '),
         ('54', 'Otro'),

        ], "97. ¿A qué destino el crédito solicitado?",
    )

    x_cual_97 = fields.Char(
        string="97.1 Cual?",
        help="Escriba los detalles",
    )

    x_finan98_inf = fields.Selection(
        #string="Sexo",
        [('50', 'No lo necesita/No le gusta pedir prestamos'),
         ('51', 'No sabe dónde acudir'),
         ('52', 'Desconoce el procedimiento para solicitarlo'),
         ('53', 'No se lo otorgarían (no cree cumplir con los requerimientos: garantías, codeudores, avales, fiadores)'),
         ('54', 'No confía en las instituciones financieras'),
         ('55', 'No entiende las condiciones asociadas a un crédito (tasa de interés, plazos, cuotas, etc.)'),
         ('56', 'Está reportado en Centrales de Riesgo'),

        ], "98. ¿Cuál es la razón principal de que no haya solicitado un crédito?",
    )

    x_finan99_inf = fields.Selection(
        #string="Sexo",
        [('50', 'No lo necesita/No le gusta pedir prestamos'),
         ('51', 'No sabe dónde acudir'),
         ('52', 'Desconoce el procedimiento para solicitarlo'),
         ('53', 'No se lo otorgarían (no cree cumplir con los requerimientos: garantías, codeudores, avales, fiadores)'),
         ('54', 'No confía en las instituciones financieras'),
         ('55', 'No entiende las condiciones asociadas a un crédito (tasa de interés, plazos, cuotas, etc.)'),
         ('56', 'Está reportado en Centrales de Riesgo'),

        ], "99. ¿Cuál es la razón secundaria de que no haya solicitado un crédito?",
    )

    x_finan100_inf = fields.Selection(
        [('50', 'Si'),
         ('51', 'No'),

        ], "100. ¿Acude al fenómeno gota gota para financiar su negocio?",
    )

    x_finan101_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Totalmente de acuerdo'),
         ('51', 'De acuerdo'),
         ('52', 'Ni de acuerdo, ni en desacuerdo'),
         ('53', 'En desacuerdo'),
         ('54', 'Totalmente en desacuerdo'),

        ], "101. ¿Considera que los ingresos del negocio son suficientes para cubrir los gastos y costos en que incurrre el negocio?",
    )

    x_finan102_inf = fields.Many2many('model.many2many102', string="102. Seleccione los productos financieros que utiliza su negocio")

    #x_finan102_inf = fields.Selection(
        #string="Sexo",
   #     [('50', 'Cuenta de ahorros'),
    #     ('51', 'Cuenta corriente'),
     #    ('52', 'Tarjetas de Crédito'),
      #   ('53', 'Billeteras electrónicas'),
       #  ('54', 'Créditos'),
        # ('55', 'Seguros'),
        #3 ('56', 'Ninguna de las anteriores'),

        #], "102. Seleccione los productos financieros que utiliza su negocio",
    #)



    x_finan103_inf = fields.Selection(
        [('50', 'Si'),
         ('51', 'No'),

        ], "103. ¿Necesita acceder a servicios y productos financieros para cubrir los gastos de materia prima, salarios, entre otros?",
    )

    x_finan104_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Totalmente de acuerdo'),
         ('51', 'De acuerdo'),
         ('52', 'Ni de acuerdo, ni en desacuerdo'),
         ('53', 'En desacuerdo'),
         ('54', 'Totalmente en desacuerdo'),

        ], "104. ¿Considera qué los gastos fijos y los gastos financieros consumen las ganancias de su negocio?",
    )

    x_finan105_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Totalmente de acuerdo'),
         ('51', 'De acuerdo'),
         ('52', 'Ni de acuerdo, ni en desacuerdo'),
         ('53', 'En desacuerdo'),
         ('54', 'Totalmente en desacuerdo'),

        ], "105. ¿Considera importante tener los ahorros del negocio en cuentas bacarias?",
    )

    x_finan106_inf = fields.Selection(
        [('50', 'Si'),
         ('51', 'No'),

        ], "106. ¿Tiene cuentas bancarias del negocio?",
    )

    x_finan107_inf = fields.Selection(
        #string="Sexo",
        [('50', 'No la necesita/ No le interesa'),
         ('51', 'No sabe'),
         ('52', 'Desconoce el procedimiento para solicitar una cuenta bancaria'),
         ('53', 'Los intereses y comisiones son muy altos'),
         ('54', 'No cumple con los requerimientos'),
         ('55', 'Está reportado en Centrales de Riesgo'),

        ], "107. ¿Cuál es la razón para qué no tenga una cuenta de ahorros o una cuenta corriente para su negocio?",
    )

    x_finan108_inf = fields.Selection(
        [('50', 'Si'),
         ('51', 'No'),

        ], "108. ¿Sabe qué son las billeteras electrónicas?",
    )

    x_finan109_inf = fields.Selection(
        #strng="Sexo",
        [('50', 'Totalmente de acuerdo'),
         ('51', 'De acuerdo'),
         ('52', 'Ni de acuerdo, ni en desacuerdo'),
         ('53', 'En desacuerdo'),
         ('54', 'Totalmente en desacuerdo'),

        ], "109. ¿Considera importante el uso de las billeteras electrónicas para el negocio?",
    )

    x_finan110_inf = fields.Selection(
        [('50', 'Si'),
         ('51', 'No'),

        ], "110. ¿En su negocio utiliza billeteras electrónicas?",
    )



    country_id = fields.Many2one('res.country', "Country")
    xcity = fields.Many2one('res.country.state.city', "9. Municipio de Residencia")
    city = fields.Char(related="xcity.name")


    x_state_id = fields.Many2one('res.country.state', '21. Departamento donde se ubica su negocio')
    x_city_id = fields.Many2one('res.country.state.city', '22. Municipio donde se ubica su negocio')

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

    @api.constrains('x_dias_sem_inf','x_dias_sem_for','x_dias_sem_for2','x_horas_trab_inf',
                    'x_trabajadores_form','x_innova34','x_forma59_form','x_forma58_form',
                    'x_forma60_form','x_forma61_form','x_trabajadores_inf','x_reinvierte_form',
                    'x_clientes_form','x_clientes_inf','x_reinvierte_inf','x_forma62_inf','x_forma63_inf','x_forma64_inf','x_forma65_inf')
    def _check_value_1(self):
        if self.x_dias_sem_inf > 7 or self.x_dias_sem_inf < 0:
            raise ValidationError("Ingrese un valor entre 0 y 7. (Pregunta 31)")
        if self.x_dias_sem_for > 7 or self.x_dias_sem_for < 0:
            raise ValidationError("Ingrese un valor entre 0 y 7. (Pregunta 31)")
        if self.x_dias_sem_for2 > 7 or self.x_dias_sem_for2 < 0:
            raise ValidationError("Ingrese un valor entre 0 y 7. (Pregunta 32)")
        if self.x_horas_trab_inf > 24 or self.x_horas_trab_inf < 0:
            raise ValidationError("Ingrese un valor entre 0 y 24. (Pregunta 32)")
        if self.x_trabajadores_form > 9 or self.x_trabajadores_form < 0:
            raise ValidationError("Ingrese un valor entre 0 y 9. (Pregunta 34)")
        if self.x_innova34 > 42 or self.x_innova34 < 0:
            raise ValidationError("Ingrese un valor entre 0 y 42. (Pregunta 34)")
        if self.x_forma58_form > 9 or self.x_forma58_form < 0:
            raise ValidationError("Ingrese un valor entre 0 y 9. (Pregunta 58)")
        if self.x_forma59_form > 9 or self.x_forma59_form < 0:
            raise ValidationError("Ingrese un valor entre 0 y 9. (Pregunta 59)")
        if self.x_forma60_form > 9 or self.x_forma60_form < 0:
            raise ValidationError("Ingrese un valor entre 0 y 9. (Pregunta 60)")
        if self.x_forma61_form > 9 or self.x_forma61_form < 0:
            raise ValidationError("Ingrese un valor entre 0 y 9. (Pregunta 61)")
        if self.x_trabajadores_inf > 9 or self.x_trabajadores_inf < 0:
            raise ValidationError("Ingrese un valor entre 0 y 9. (Pregunta 33)")
        if self.x_reinvierte_form > 100 or self.x_reinvierte_form < 0:
            raise ValidationError("Ingrese un valor entre 1 y 100. (Pregunta 48)")
        if self.x_reinvierte_inf > 100 or self.x_reinvierte_inf < 0:
            raise ValidationError("Ingrese un valor entre 1 y 100. (Pregunta 49)")
        if self.x_forma62_inf > 9 or self.x_forma62_inf < 0:
            raise ValidationError("Ingrese un valor entre 1 y 9. (Pregunta 62)")
        if self.x_forma63_inf > 9 or self.x_forma63_inf < 0:
            raise ValidationError("Ingrese un valor entre 1 y 9. (Pregunta 63)")
        if self.x_forma64_inf > 9 or self.x_forma64_inf < 0:
            raise ValidationError("Ingrese un valor entre 1 y 9. (Pregunta 64)")
        if self.x_forma65_inf > 9 or self.x_forma65_inf < 0:
            raise ValidationError("Ingrese un valor entre 1 y 9. (Pregunta 65)")    


