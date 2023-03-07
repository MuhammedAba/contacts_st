# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PartnerMemberTypes(models.Model):
    _name = "partner.member.types"

    name = fields.Char(string="Üyelik Tipleri")