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
    x_cont1_por = fields.Text(
        string="2. ¿Por qué no desea continuar con el proceso?",
    )

    x_datos3 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "DESEA CONTINUAR CON EL DIAGNOSTICO",
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
        string="continuar con el Formulario",
    )
    #preguntas nuevas modelo de negocio
    x_model21 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "21. ¿Tiene identificados y caracterizados los segmentos de mercado objetivo de su negocio?",
        oldname="model21"
    )
    x_model22 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "22. ¿Tiene definida con claridad y apropiadamente una propuesta de valor para  los segmentos de mercado objetivo de su negocio?",
        oldname="model22"
    )
    x_model23 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "23. ¿Cumple la propuesta de valor definida para  los segmentos de mercado objetivo?",
        oldname="model23"
    )
    x_model24 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "24. ¿Tiene identificados y en funcionamiento óptimo canales apropiados para comunicar la oferta a cada uno de sus segmentos de mercado objetivo?",
        oldname="model24"
    )
    x_model25 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "25. ¿Tiene identificados y en funcionamiento óptimo canales apropiados para que cada uno de sus segmentos de mercado objetivo realice la compra y estos son competitivos con lo ofrecido por la competencia?",
        oldname="model25"
    )
    x_model26 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "26. ¿Tiene identificados y en funcionamiento óptimo canales apropiados para realizar la entrega a cada uno de sus segmentos de mercado y estos son competitivos con lo ofrecido por la competencia?",
        oldname="model26"
    )
    x_model27 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "27. ¿El servicio posventa es competitivo y se enfoca en las necesidades de cada uno de los segmentos de mercado?",
        oldname="model27"
    )
    x_model28 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "28. ¿Los mecanismos de captación de clientes son apropiados desde la captación y el funcionamiento, y se enfocan en la caracteterísticas de cada segmento de mercado?",
        oldname="model28"
    )
    x_model29 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "29. ¿Los mecanismos de fidelización de clientes son apropiados desde la captación y el funcionamiento, y se enfocan en la caracteterísticas de cada segmento de mercado?",
        oldname="model29"
    )
    x_model30 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "30. ¿Los mecanismos de estimulación para el aumento de la compra en los clientes son apropiados desde la captación y el funcionamiento, y se enfocan en la caracteterísticas de cada segmento de mercado?",
        oldname="model30"
    )
    x_model31 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "31. ¿Son claras las fuentes de ingreso y estas están verdaderamente basadas y enfocadas en el valor esperado por los clientes?",
        oldname="model31"
    )
    x_model32 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "32. ¿El negocio tiene identificados los recursos requeridos para el perfecto funcionamiento del modelo de negocio y el cumplimiento de la propuesta de valor?",
        oldname="model32"
    )
    x_model33 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "33. ¿El negocio cuenta con todos los recursos requeridos para el perfecto funcionamiento del modelo de negocio y el cumplimiento de la propuesta de valor?",
        oldname="model33"
    )
    x_model34 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "34. ¿El negocio tiene identificadas las actividades claves para el perfecto funcionamiento del modelo de negocio y el cumplimiento de la propuesta de valor?",
        oldname="model34"
    )
    x_model35 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "35. ¿Las actividades claves del negocio hacen parte de procesos estandarizados y bien definidos?",
        oldname="model35"
    )
    x_model36 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "36. ¿El negocio cuenta con acuerdos con proveedores y estos son suficientes y apropiados?",
        oldname="model36"
    )
    x_model37 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "37. ¿El negocio cuenta con algún tipo de alianza para su desarrollo técnico?",
        oldname="model37"
    )
    prodl39 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "39. ¿Cuenta con un espacio adecuado para la produccion y almacenamiento del producto, teniendo en cuenta medidas de higiene y de seguridad??",
    )

    x_prodl42 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "42. ¿Se tiene en el negocio definidos los estándares de los procesos de producción de los productos/servicios que vende?",
        oldname="prodl42"
    )
    x_prodl43 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "43. ¿Tiene su negocio un sistema de control/ gestion de calidad adoptado e implementado?",
        oldname="prodl43"
    )
    x_prodl46 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "46. ¿Sabe lo que le cuesta a su negocio la produccion y comercializacion del producto o servicio?",
        oldname="prodl46"
    )
    x_prodl47 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
            ('en_proceso', 'En proceso'),
        ], "47. ¿sabe cuáles son los costos de cada etapa del proceso de producción?",
        oldname="prodl47"
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
        ], "44. ¿Ha representado retrasos en la entrega de su producto por falta de materia prima o mercancia?",
    )

    x_innova33 = fields.Selection(
        [('si', 'Si'),
         ('no', 'No'),
         ('en_proceso', 'En proceso'),
        ], "45. ¿Cuenta con un inventario donde registre las entradas y salidas del producto?",
    )

    x_innova36 = fields.Selection(
        [('si', 'Si'),
         ('no', 'No')
        ], "46. ¿Sabe lo qué le cuesta a su negocio la producción y comercialización del producto o servicio?",
    )

    x_innova39 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "48. ¿Sabe cual es el punto de equilibrio de su negocio?",
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

    x_cual_97 = fields.Char(
        string="97.1 Cual?",
        help="Escriba los detalles",
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