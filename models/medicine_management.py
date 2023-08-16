from odoo import models,fields

class MedicineManagement(models.Model):
    _name="medicine.management"
    _description="For managing the medicine"


    name_of_medicine=fields.Char(sting="Name_of_medicine")
