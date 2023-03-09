# -*- coding: utf-8 -*-

from odoo import models,fields


class Partner(models.Model):#orjinalini yaz
    _description = 'Contact'
    _inherit = "res.partner"

    partner_member_types = fields.Many2one("partner.member.types", string="Member Types")
    partner_blood_groups = fields.Many2one("partner.blood.groups", string="Blood groups")
    partner_birth_place = fields.Char(string="Place Of Birth") 
    # YUKARIDA char da olabilir many2one da bu şekilde seçim eklenebşlir olacak
    partner_birth_certificate = fields.Char(string="Birth Certificate")
    partner_profession_workplace = fields.Char(string="Profession/Workplace")
    partner_sector = fields.Char(string="Sector")
    partner_languages = fields.Char(string="Languages")
    partner_family_ngo = fields.Char(string="Family Non-Governmental Organisation")
    partner_passport = fields.Char(string="Passport")
    partner_before_ngo = fields.Char(string="Do you have an NGO that you are a member of?")

