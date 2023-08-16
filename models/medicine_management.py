from odoo import models,fields

class MedicineManagement(models.Model):
    _name="medicine.management"
    _description="For managing the medicine"


    name_of_medicine=fields.Char(sting="Name_of_medicine",required=True)
    
    expire_date=fields.Date(string="Expire_Date",required=True)

    composition_of_medicine=fields.Char(string="Composition_of_medicine",required=True)

    selling_price=fields.Integer(string="Selling_Price",readonly=True)

    best_price=fields.Integer(string="Best_Price")



    seller=fields.Char(string="Seller")

    buyer=fields.Char(string="Buyer")



    total_medicine=fields.Integer(string="Total_Medicine",required=True)

    sold_out_medicine=fields.Integer(string="Sold_Out_Medcine",required=True)

    available_medicine=fields.Integer(string="Available_Medicine",readonly=True)



    # relation beetween the models

    symptoms_ids=fields.Many2many("medicine.symptoms",string="Symptoms")

    block_id=fields.Many2one("medicine.block",string="Blocks")

    offer_ids=fields.One2many("medicine.offer","customer_id",string="offer")

