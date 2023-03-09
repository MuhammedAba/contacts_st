# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PartnerBloodGroups(models.Model):
    _name = "partner.blood.groups"

    name = fields.Char(string="Blood Group")
