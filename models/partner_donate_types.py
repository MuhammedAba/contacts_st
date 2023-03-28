# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PartnerDonateTypes(models.Model):
    _name = "partner.donate.types"

    name = fields.Char(string="Donate Types")