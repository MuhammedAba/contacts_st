from odoo import http
from odoo.http import request


class StkPage(http.Controller):

    @http.route('/volunteer_webform', type="http", auth='public', website=True)
    def volunteer_webform(self, **kw):
        member_rec = request.env["partner.member.types"].sudo().search([])  # Name of model
        blood_rec = request.env["partner.blood.groups"].sudo().search([])  # Name of model
        return http.request.render('contacts_stk.create_volunteer', {'blood_rec': blood_rec, 'member_rec':member_rec})  # ModuleName.TemplateId

    @http.route('/create/volunteer', type="http", auth="public", website=True)
    def create_volunteer(self, **kw):
        print("Data received...", kw)
        request.env['res.partner'].sudo().create(kw)
        return request.render("contacts_stk.volunteer_thanks", {})
