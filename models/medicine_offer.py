from odoo import models,fields

class MedicineOffer(models.Model):
    _name="medicine.offer"
    _description="Offer for the medicine"

    price=fields.Char(string="Price")

    name_of_customer=fields.Many2one("res.partner",string="Name_of_Customer")

    customer_id=fields.Many2one("medicine.management",string="Customer_id")

    status=[
        ('accepted','Accepted'),
        ('rejected','Rejected')
    ]

    status=fields.Selection(selection=[('accepted','Accepted'),('rejected','Rejected')],string="Status")


    validity=fields.Integer(default=7,string="Validity")

    date_deadline=fields.Date(string="Date_deadline")

    