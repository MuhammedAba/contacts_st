# -*- coding: utf-8 -*-
# okullar burada


from odoo import models, fields, api


class PartnerSchools(models.Model):
    _name = "partner.schools"

    name = fields.Char(string="Schools")