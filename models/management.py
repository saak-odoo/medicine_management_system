from odoo import models,fields

class Management(models.Model):
    _name="medicine.management.system"
    _description="This is helpfull for the medical shop for finding the medicine and check the avalibilty of medicine... etc"

    name_of_medicine=fields.Char(sting="Name_of_medicine")
