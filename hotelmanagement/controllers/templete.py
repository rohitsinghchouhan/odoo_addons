from openerp import http

class Temp_demo(http.Controller):

    @http.route('/hotelmanagement/', auth='public')
    def index(self, **kw):
        return http.request.render('hotelmanagement.index',{ 'customer': http.request.env["hotelmanagement.customer"].search([])})

    @http.route('/hotelmanagement/home', auth='public', methods=['post'])
    def index_post(self, **kw):
        name = kw.get('name')
        if name:
            # record = http.request.env['hotelmanagement.customer'].sudo().create(dict(name=name))
            # if record:
            #     return "Record return"
            Created http.request.render('hotelmanagement.home',{'customer': [name]})