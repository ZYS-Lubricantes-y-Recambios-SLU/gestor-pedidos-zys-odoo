# -*- coding: utf-8 -*-
from odoo import models, fields


class ZysPedido(models.Model):
    _name = 'zys.pedido'
    _description = 'Pedido de Recambio ZYS'
    _inherit = ['mail.thread']

    fecha = fields.Date(string='Fecha', default=fields.Date.context_today, required=True)
    matricula = fields.Char(string='Matrícula', required=True)
    marca = fields.Char(string='Marca')
    cliente_id = fields.Many2one('res.partner', string='Cliente', required=True)
    product_id = fields.Many2one('product.product', string='Producto', required=True)
    descripcion = fields.Char(string='Descripción')
    referencia = fields.Char(string='Referencia')
    cantidad = fields.Float(string='Cantidad', default=1.0, required=True)
    precio = fields.Float(string='Precio', default=0.0, required=True)
    dependiente_id = fields.Many2one('res.users', string='Atendido por', default=lambda self: self.env.user)
    situacion = fields.Text(string='Notas')
    status = fields.Selection([
        ('PENDIENTE', 'Pendiente de Pedir'),
        ('PEDIDO', 'Pedido'),
        ('RECIBIDO', 'Recibido'),
        ('RETIRADO', 'Retirado'),
        ('PAGADO', 'Pagado'),
    ], string='Estado', default='PENDIENTE', required=True, tracking=True)
