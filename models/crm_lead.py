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

    x_datos1 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),

        ], "SELECCIONE SI PARA COMENZAR",
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
        ], "¿Cuál es la actividad comercial de su negocio?",
        help="Escriba la actividad comercial de su negocio",
    )

    x_cont1 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "1. Una vez comprendido el programa de acompañamiento, ¿usted desea continuar?",
    )

    x_datos3 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "DESEA CONTINUAR CON EL DIAGNOSTICO",
    )
    
    #MÓDULO planear diagnostico
    x_dcont1 = fields.Boolean(
        string="Continuar con el Formulario",
    )

    x_proto1 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "1. ¿ Su empresa afilia a todos sus empleados a la Seguridad Social (pensiones, salud y ARL)?",
    )

    x_proto2 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "2. ¿Ha definido una Política de Seguridad y Salud en el trabajo?",
    )

    x_proto3 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "3. ¿Ha creado un Documento del Sistema de Gestión de Seguridad y Salud SGSST en el Trabajo?",
    )

    x_proto4 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "4. ¿Están definidos los objetivos del SG-SST, son medibles, coherentes con el Plan de trabajo Anual en SST, se encuentran documentados, comunicados a los trabajadores y son evaluados periódicamente y actualizados de ser necesario?",
    )

    x_proto5 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "5. ¿Cuenta con un documento “deberes y responsabilidades del Empleador y del trabajador”; está divulgado a sus trabajadores y se le hace seguimiento?",
    )

    x_proto6 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "6. ¿Sus empleados conocen sus responsabilidades en cuanto al Sistema de Seguridad y Salud en el Trabajo?",
    )

    x_proto7 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "7. ¿La empresa ha diseñado una herramienta de comunicación en doble dirección del (empleador con el empleado ), se encuentra documentada en algún documento especificando su procedimiento?",
    )

    x_proto8 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "8. ¿La empresa cuenta con Indicadores del sistema de gestión de seguridad y salud en el trabajo?",
    )

    x_proto9 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "9. ¿Su empresa Cuenta con el Vigía Ocupacional o con el Comité Paritario de Seguridad y salud en el Trabajo (COPASST)?",
    )

    x_proto10 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "10. ¿Su empresa Cuenta con el Reglamento interno de trabajo y lo divulga entre los trabajadores?",
    )

    x_proto11 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "11. ¿Cuenta con el Reglamento de Higiene y seguridad industrial y lo divulga?",
    )

    x_proto12 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "12. ¿Identifica sus Peligros, Evalua y Valora los Riesgos?",
    )

    x_proto13 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "13. ¿Cuenta con Programa anual de capacitación y lo divulga?",
    )

 

   
    #hacer
    x_dcont2 = fields.Boolean(
        string="continuar con el Formulario",
    )
    x_proto14 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "14. Realiza Inspecciones planeadas y Realiza correctivos?",
    )

    x_proto15 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "15. Cuenta con Fichas de seguridad de las sustancias quimicas que utiliza?",
    )

    x_proto16 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "16. Cuenta con Procedimientos, instructivos y normas de seguridad para riesgos prioritarios?",
    )
    
    x_model21 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "17. Cuenta con un Programa de Elementos de Protección Personal, donde se identifique cuales necesita, como se utilizan, se capacite al personal y se tenga un plan de reposición?",
        oldname="model21"
    )
    x_model22 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "18. Realiza Exámenes médicos de ingreso, periódicos y de retiro a sus trabajadores?",
        oldname="model22"
    )
    x_model23 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "19. Cuenta con Programas de Vigilancia Epidemiológica específicos de sus riesgos prioritarios que puedan generar una enfermedad laboral?",
        oldname="model23"
    )
    x_model24 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "20. Cuenta con un Plan de prevención, preparación y respuesta ante emergencias",
        oldname="model24"
    )
    x_model25 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),     
        ], "21. Cuenta con una Brigada de emergencias capacitada?",
        oldname="model25"
    )
    x_model26 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),    
        ], "22. Cuenta con un Plan de evacuación y sus responsables?",
        oldname="model26"
    )
    x_model27 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "23. Realiza Simulacros por lo menos una vez al año?",
        oldname="model27"
    )
    x_model28 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "24. Realiza la Investigación de los Accidentes de Trabajo en los tiempos establecidos por la legislación Nal?",
        oldname="model28"
    )
    x_model29 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "25. Cumple con el desarrollo del programa de Capacitación?",
        oldname="model29"
    )

    ##validar
    x_model30 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "26. Valida la gerencia el cumplimiento del sistema de gestión de seguridad y salud en el trabajo?",
        oldname="model30"
    )
    x_model31 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "27. Gestiona los Correctivos generadados por la investigación de accidentes de trabajo?",
        oldname="model31"
    )
    x_model32 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "28. Cuenta con indicadores para medir la gestión en seguridad y salud en el trabajo?",
        oldname="model32"
    )

    ##actuar
    x_model33 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "29. Genera y gestiona Acciones preventivas y correctivas? (Una acción correctiva es aquella que llevamos a cabo para eliminar la causa de un problema. Las correcciones atacan los problemas, las acciones correctivas sus causas. Las acciones preventivas se anticipan a la causa, y pretenden eliminarla antes de su existencia. Evitan los problemas identificando los riesgos. Cualquier acción que disminuya un riesgo es una acción preventiva)?",
        oldname="model33"
    )
    x_model34 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "30. Mejora continua: Da las directrices y otorgar los recursos necesarios PARA mejorar la eficacia de sus actividades en el sistema de gestión de seguridad y salud en el trabajo?",
        oldname="model34"
    )
    
    #gavii
#FORMALIZACION SECCION 3: ADMINISTRACION
    x_dcont3 = fields.Boolean(
        string="Continuar con el Formulario",
    )
 
    x_dcont4 = fields.Boolean(
        string="Continuar con el Formulario",
    )
   
    x_dcont5 = fields.Boolean(
        string="Continuar con el Formulario",
    )
 
    x_dcont6 = fields.Boolean(string="Continuar con el Formulario")
    
    x_dcont7 = fields.Boolean(string="Continuar con el Formulario")
   
    x_dcont8 = fields.Boolean(string="Continuar con el Formulario")
    

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
        #