# -*- coding: utf-8 -*-
# sandıklar burada


from odoo import models, fields, api


class PartnerBoxes(models.Model):
    _name = "partner.boxes"

    name = fields.Char(string="Boxes")