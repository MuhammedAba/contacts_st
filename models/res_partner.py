# -*- coding: utf-8 -*-

from odoo import models,fields


class Partner(models.Model):#orjinalini yaz
    _description = 'Contact'
    _inherit = "res.partner"

    partner_member_types = fields.Many2one("partner.member.types", string="Üyelik Tipleri")
    partner_blood_groups = fields.Many2one("partner.blood.groups", string="Kan Grupları")

