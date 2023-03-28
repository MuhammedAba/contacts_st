# -*- coding: utf-8 -*-
# ilçeler burada


from odoo import models, fields, api


class PartnerDistricts(models.Model): 
    _name = "partner.districts"

    name = fields.Char(string="Districts")
    
