# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PartnerEducationStatus(models.Model):
    _name = "partner.education.status"

    name = fields.Char(string="Education Status")
