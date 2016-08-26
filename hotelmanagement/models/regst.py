from openerp import models, fields, api

class Registor(models.Model):
    _name="hotelmanagement.regst"

    customer = fields.Many2one("res.partner")
    room = fields.Many2one("hotelmanagement.room")
    name = fields.Char(related="customer.name")
    checkin_date = fields.Datetime(default=fields.Date.today)
    checkout_date = fields.Datetime()
    active = fields.Boolean(default=True)

    state = fields.Selection([('registor',"Registor"), ('checkin',"Check in"),('checkout',"Check out")], required=True, default='registor')
    
    @api.multi
    def action_check_in(self):
        self.state = "checkin"

    # @api.multi
    # def action_stay(self):
    #     self.state = "stay"

    @api.multi
    def action_checkout(self):
        self.checkout_date = fields.Datetime.now()
        self.state = "checkout"