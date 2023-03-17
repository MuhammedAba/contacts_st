# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PartnerLanguages(models.Model):
    _name = "partner.languages"

    name = fields.Char(string="Languages")