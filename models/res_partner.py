# -*- coding: utf-8 -*-

from odoo import models,fields


class Partner(models.Model):#orjinalini yaz
    _description = 'Contact'
    _inherit = "res.partner"

    partner_member_types = fields.Many2one("partner.member.types", string="Üyelik Tipleri")
    partner_blood_groups = fields.Many2one("partner.blood.groups", string="Kan Grupları")
    partner_identity = fields.Char(String="Identification Number")
    partner_gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender")
    partner_birth_year = fields.Date(string="Birth Year")
    partner_education_status = fields.Many2one("partner.education.status", string="Education Status")
    partner_driving_license = fields.Many2many("partner.driving.license", string="Driving License")
