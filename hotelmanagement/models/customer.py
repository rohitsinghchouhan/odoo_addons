from openerp import models, fields, api

class Invoice(models.Model):
	_name = "hotelmanagement.invoice"

	tax = fields.Float(string="Sales Tax")

class Partner(models.Model):
	
	_inherit = 'res.partner',
	gender = fields.Selection([('male',"Male"),('female',"Female"),],required=True, default='male')



class Customer(models.Model):
	_name = "hotelmanagement.customer"

	name = fields.Char(string="Customer Name")
	address = fields.Text(string="Address")
	mobile_number = fields.Char(string="Mobile Number", required=True)
	gender = fields.Selection([('male',"Male"),('female',"Female"),],required=True, default='male')

class Room(models.Model):
	_name = "hotelmanagement.room"
	_rec_name = "room_no"

	room_no = fields.Integer()
	room_type = fields.Selection([('delux',"Delux without A/C"),('super_delux',"Super Delux with A/C"),('villa',"Villa with A/C")],required=True, default='delux')
	room_price = fields.Float(required=True, default=1001)
	room_capacity = fields.Integer()


