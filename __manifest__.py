# -*- coding: utf-8 -*-
{
    'name': "Gestor de Pedidos ZYS",
    'summary': "Gestión integral de pedidos ZYS con presupuestos e impresión de tickets",
    'description': """
        Módulo para la gestión de pedidos de recambios de ZYS.
        - Registro de pedidos por matrícula, cliente y producto
        - Creación automática de presupuesto de ventas
        - Impresión de ticket de pedido
    """,
    'author': "ZYS",
    'category': 'Sales',
    'version': '1.0',
    'depends': ['base', 'mail', 'product', 'sale_management', 'base_automation'],
    'data': [
        'data/zys_pedido_model.xml',
        'security/zys_pedido_security.xml',
        'data/zys_presupuesto_action.xml',
        'data/zys_automation.xml',
        'report/zys_ticket.xml',
        'views/zys_pedido_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
