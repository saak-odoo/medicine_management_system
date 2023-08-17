from odoo import models,fields,api

from odoo.exceptions import ValidationError


class MedicineManagement(models.Model):
    _name="medicine.management"
    _description="For managing the medicine"
    _rec_name = 'name_of_medicine'

    name_of_medicine=fields.Char(sting="Name_of_medicine",required=True)
    
    expire_date=fields.Date(string="Expire_Date",required=True)

    composition_of_medicine=fields.Char(string="Composition_of_medicine",required=True)

    selling_price=fields.Integer(string="Selling_Price",readonly=True)

    best_price=fields.Integer(string="Best_Price",compute="_compute_best_price")


    seller=fields.Char(string="Seller")

    buyer=fields.Char(string="Buyer")

    color=fields.Integer()



    total_medicine=fields.Integer(string="Total_Medicine",required=True)

    sold_out_medicine=fields.Integer(string="Sold_Out_Medcine",required=True)

    available_medicine=fields.Integer(string="Available_Medicine",readonly=True,compute="_compute_available")


    # relation beetween the models

    symptoms_ids=fields.Many2many("medicine.symptoms",string="Symptoms")

    block_id=fields.Many2one("medicine.block",string="Blocks")

    offer_price_ids=fields.One2many("medicine.offer","customer_id",string="offer")




#    Adding compute for cal of total_medicine,sold_out_medicine,available_medicine
    
    @api.depends("sold_out_medicine","total_medicine")
    def _compute_available(self):
        for record in self:
            val=record.total_medicine-record.sold_out_medicine
            if val<0:
                raise ValidationError("You have not enough Stock")
            else:
                record.available_medicine=val


    @api.depends("offer_price_ids.price")
    def _compute_best_price(self):
        for record in self:
            val=0
            for i in record.offer_price_ids:
                print(i.price)
                # val=max(val,i.price)
            record.best_price=10















    # Adding sql constraints

    _sql_constraints = [
        ('check_selling_price', 'CHECK(selling_price >= 0 AND selling_price <= 100)',
         'The Price must be Positive.'),
        ('check_total_medicine', 'CHECK(total_medicine >= 0 AND total_medicine <= 100)',
         'The total_medicine must be Positive.'),
        ('check_sold_out_medicine', 'CHECK(sold_out_medicine >= 0 AND sold_out_medicine <= 100)',
         'The sold_out_medicine must be Positive.'),
        ('check_available_medicine', 'CHECK(available_medicine >= 0 AND available_medicine <= 100)',
         'The available_medicine must be Positive.'),
        ('check_best_price', 'CHECK(best_price >= 0 AND best_price <= 100)',
         'The best_price must be Positive.'),
    ]

    _sql_constraints = [
        ('name_of_medicine_unique', 'unique(name_of_medicine)',
        'Field name_of_medicine must be unique')
    ]

