from openerp import models, fields, api

class Session(models.Model):
	_name = "openacademy.session"

	name = fields.Char(string="Session Type")
	state = fields.Selection([('draft',"Draft"),('inprogess',"In Progress"),('done',"Done")],required=True, default='draft')
	duration = fields.Float(string="Duration of Session")
	seats = fields.Integer(string="Seat left")
	date = fields.Datetime(default=fields.Date.today)
	active = fields.Boolean(default=True)
	description = fields.Text()
	course = fields.Many2one("openacademy.course")
	instructor = fields.Many2one("openacademy.instructor")

class Instructor(models.Model):
	_name = "openacademy.instructor"

	name = fields.Char()
	description = fields.Text()
	year = fields.Integer()


