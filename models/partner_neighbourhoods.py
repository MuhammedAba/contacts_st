# -*- coding: utf-8 -*-
# mahalleler burada

from odoo import models, fields, api


class PartnerNeighbourhoods(models.Model):
    _name = "partner.neighbourhoods"

    name = fields.Char(string="Neighbourhood")