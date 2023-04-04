from odoo import http
from odoo.http import request


class StkPage(http.Controller):

    @http.route('/volunteer_webform', type="http", auth='public', website=True)
    def volunteer_webform(self, **kw): 
        member_rec = request.env["partner.member.types"].sudo().search([])  # Name of model
        member_rec = request.env["partner.member.types"].sudo().search([])  # Name of model
        education_rec = request.env["partner.education.status"].sudo().search([])  # Name of model
        return http.request.render('contacts_stk.create_volunteer', {'education_rec': education_rec, 'member_rec': member_rec})  # ModuleName.TemplateId

    @http.route('/create/volunteer', type="http", auth="public", website=True)
    def create_volunteer(self, **kw):
        print("Data received...", kw)
        request.env['res.partner'].sudo().create(kw)
        return request.render("contacts_stk.volunteer_thanks", {})
    
    # DONATE
    @http.route('/donate_webform', type="http", auth='public', website=True)
    def donate_webform(self, **kw):
        donate_rec = request.env["partner.donate.types"].sudo().search([])  # Name of model
        donate_rec = request.env["partner.donate.types"].sudo().search([])  # Name of model
        return http.request.render('contacts_stk.create_donate', { 'donate_rec': donate_rec})  # ModuleName.TemplateId

    @http.route('/create/donate', type="http", auth="public", website=True)
    def create_donate(self, **kw):
        print("Data received...", kw)
        request.env['res.partner'].sudo().create(kw)
        return request.render("contacts_stk.donate_thanks", {})
