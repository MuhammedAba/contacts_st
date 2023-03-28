# -*- coding: utf-8 -*-
# şehilerler buradan gelecek

from odoo import models, fields, api


class PartnerProvinces(models.Model):
    _name = "partner.provinces"

    name = fields.Char(string="Provinces")