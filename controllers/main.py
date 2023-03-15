from odoo import http
from odoo.http import request


class StkPage(http.Controller):

    @http.route('/volunteer_webform', type="http", auth='public', website=True)
    def volunteer_webform(self, **kw):
        return http.request.render('contacts_stk.create_volunteer', {})

    @http.route('/create/volunteer', type="http", auth="public", website=True)
    def create_volunteer(self, **kw):
        print("Data received...", kw)
        request.env['res.partner'].sudo().create(kw)
        return request.render("contacts_stk.volunteer_thanks", {})
