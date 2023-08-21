from odoo import models,fields

class medicineIherit(models.Model):
    _inherit="res.users"
    _description="This for the medicine inherite to the user"

    medicine_type_ids=fields.One2many("medicine.management","sellesperson_id",string="Medicne_Type")