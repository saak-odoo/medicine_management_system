from odoo import models
from odoo import fields

class MedicineBlock(models.Model):
    _name="medicine.block"
    _description="for managing the medicine according to block"
    _order="name_of_block asc"
    _rec_name = 'name_of_block'

    name_of_block=fields.Selection(
        selection=[('block_a','Block_A'),('block_b','Block_B'),('block_c','Block_C'),('block_d','Block_D')],
        string="Name_of_block",
        options="{'no_create': True, 'no_create_edit':True}"
        )

    name_of_block_element=fields.Char(string="Name_of_block_element")


    