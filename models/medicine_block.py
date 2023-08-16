from odoo import models,fields

class MedicineBlock(models.Model):
    _name="medicine.block"
    _description="for managing the medicine according to block"

    block=[
        ('block_a','Block_A'),
        ('block_b','Block_B'),
        ('block_c','Block_C'),
        ('block_d','Block_D'),  
    ]


    name_of_block=fields.Selection(selection=block,string="Name_of_block",required=True)

    name_of_block_element=fields.Char(string="Name_of_block_element")
