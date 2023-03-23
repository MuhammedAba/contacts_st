# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PartnerSector(models.Model):
    _name = "partner.sector"

    name = fields.Char(string="Sector")