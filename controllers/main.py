from odoo import http
from odoo.http import request


class StkPage(http.Controller):

    @http.route('/volunteer_webform', type="http", auth='public', website=True)
    def volunteer_webform(self, **kw):
        return http.request.render('contacts_stk.create_volunteer', {})

