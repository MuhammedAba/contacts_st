# -*- coding: utf-8 -*-

from odoo import models,fields


class Partner(models.Model):#orjinalini yaz
    _description = 'Contact'
    _inherit = "res.partner"

    partner_member_types = fields.Many2one("partner.member.types", string="Üyelik Tipleri")
