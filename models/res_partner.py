# -*- coding: utf-8 -*-

from odoo import models,fields


class Partner(models.Model):#orjinalini yaz
    _description = 'Contact'
    _inherit = "res.partner"

<<<<<<< HEAD
=======
    partner_job = fields.Char(String="Job")
>>>>>>> basak_development
    partner_member_types = fields.Many2one("partner.member.types", string="Member types")
    partner_blood_groups = fields.Many2one("partner.blood.groups", string="Blood Groups")
    partner_gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender")
    partner_birth_date = fields.Date(string="Birth Date")
    partner_city = fields.Char(string="City")
    partner_contact_choice_control = fields.Selection([("email", "E-mail"), ("phone", "Phone")], string="How can we contact?")

<<<<<<< HEAD
    #TAB1 Extra Information
    partner_languages = fields.Many2many("partner.languages", string="Languages")
    partner_driving_license = fields.Many2many("partner.driving.license", string="Driving License")
    partner_education_status = fields.Many2one("partner.education.status", string="Education Status")
    partner_driving_license_control = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="Do you have driving license?")
=======
    #TAB1 Extra İnformation
    
    # partner_birth_place = fields.Char( string="Place Of Birth")
    # partner_birth_certificate = fields.Char(string="Birth Certificate")
    partner_driving_license_control = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="Do you have driving license?")
    partner_driving_license = fields.Many2many("partner.driving.license", string="Driving License")
    # partner_education_status = fields.Many2one("partner.education.status", string="Education Status")
    # partner_profession = fields.Many2one("partner.profession", string="Profession")
    partner_sector = fields.Many2one("partner.sector",string="Sector")
    partner_languages = fields.Many2many("partner.languages", string="Languages")
>>>>>>> basak_development
    partner_passport = fields.Selection([('yes', 'Yes'), ('no', 'No')], string='Do you have a passport?')
    partner_before_ngo_control = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="Do you have an NGO that you are a member of?")
    partner_before_ngo = fields.Selection([('yes', 'Yes'), ('no', 'No')], string='Please enter Ngo name.')
    partner_family_ngo = fields.Selection([('yes', 'Yes'), ('no', 'No')], string='Is there anyone in the family with an NGO?')
    partner_profession_workplace = fields.Char(string="Profession/Workplace")
    partner_sector = fields.Char(string="Sector")
    partner_extra_info = fields.Char(string="Additional Notes")
