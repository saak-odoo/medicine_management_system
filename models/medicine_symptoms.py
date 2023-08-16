from odoo import models,fields

class MedicineSymptoms(models.Model):
    _name="medicine.symptoms"
    _description="medicine distributed according to symptoms"


    name_of_symptoms=fields.Char(string="Name_of_symptoms")

    