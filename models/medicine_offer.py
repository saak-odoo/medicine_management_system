from odoo import models,fields

class MedicineOffer(models.Model):
    _name="medicine.offer"
    _description="Offer for the medicine"

    price=fields.Char(string="Price")