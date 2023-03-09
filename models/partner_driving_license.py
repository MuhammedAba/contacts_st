# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PartnerDrivingLicense(models.Model):
    _name = "partner.driving.license"

    name = fields.Char(string="Driving License")
