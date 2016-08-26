from openerp import models, fields, api, _

class Course(models.Model):
	_name = "openacademy.course"

	name = fields.Char(string="Course Name")
	duration = fields.Integer(string="Duration in months")
	session = fields.One2many("openacademy.session", "course")
