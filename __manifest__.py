# Copyright 2015 Antiun Ingeniería, S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Formulario Uniminuto-CRM",
    "summary": "Adiciona campos en el CRM",
    "version": "13.0.1.0.0",
    "category": "Customer Relationship Management",
    "website": "https://github.com/agavariat",
    "author": "Intresco_SAS",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["crm"],
    "data": [
        'security/ir.model.access.csv',
        "views/crm_lead_views.xml",
        "views/crm_team_views.xml",
        "views/many2many_models_fields_modulo1.xml",
        "views/many2many_models_fields_modulo3.xml",
        'data/l10n_cities_co_data.xml',
        'data/severalfields.xml',
        'data/modelo_negocios_model_data.xml',
        'data/modelo_conseguir_nuevos_clientes_data.xml',
        'data/modelo_herramientas_tecnologicas_data.xml',
        'data/modelo_metodos_venta_data.xml',
        'data/modelo_porque_compran_clientes.xml',
        'data/modelo_promocion_productos_data.xml',
        'data/modelo_temas_para_asesorarse_data.xml',
    ],
}