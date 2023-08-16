from odoo import models,fields

class MedicineStore(models.Model):
    _name="medicine.store"
    _description="storage of medicine"

    total_medicine=fields.Integer(string="Total_Medicine")

    sold_out_medicine=fields.Integer(string="Sold_Out_Medcine")

    available_medicine=fields.Integer(string="Available_Medicine")

