from openerp import models, fields, api

class Attandee(models.Model):
	_name = "openacademy.attandee"

	roll_no. = fields.Integer(string="Roll No.")
	name = fields.Char(string="Name of Student")
	age = fields.Integer(string="Student Age")
	gender = fields.Selection([('female',"Female"),('male',"Male")] required=True)
	dob = fields.Date()

class Marksheet(models.Model):
	_name = "openacademy.marksheet"

	
