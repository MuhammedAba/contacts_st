# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PartnerBloodGroups(models.Model):
    _name = "partner.blood.gropus"

    name = fields.Char(string="Kan Grupları")