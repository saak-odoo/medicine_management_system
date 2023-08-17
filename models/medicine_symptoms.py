from odoo import models,fields

class MedicineSymptoms(models.Model):
    _name="medicine.symptoms"
    _description="medicine distributed according to symptoms"
    _rec_name="name_of_symptoms"


    name_of_symptoms=fields.Char(string="Name_of_symptoms")


    # _sql_constraints = [
    #     ('name_of_medicine_unique', 'unique(name_of_medicine)',
    #     'Field name_of_medicine must be unique')
    # ]