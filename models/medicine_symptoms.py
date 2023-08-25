from odoo import models
from odoo import fields

class MedicineSymptoms(models.Model):
    _name="medicine.symptoms"
    _description="medicine distributed according to symptoms"
    _order="name_of_symptoms asc"
    _rec_name="name_of_symptoms"

    name_of_symptoms=fields.Char(string="Name_of_symptoms")

