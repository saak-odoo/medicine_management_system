from odoo import models,fields,api

from odoo.exceptions import ValidationError

class MedicineManagement(models.Model):
    _name="medicine.management"
    _description="For managing the medicine"
    _order="name_of_medicine asc"
    _rec_name = 'name_of_medicine'

    name_of_medicine=fields.Char(sting="Name_of_medicine",required=True)
    
    expire_date=fields.Date(string="Expire_Date",required=True)

    composition_of_medicine=fields.Char(string="Composition_of_medicine",required=True)

    selling_price=fields.Integer(string="Selling_Price",readonly=True,compute="_compute_selling_price")

    best_price=fields.Integer(string="Best_Price",compute="_compute_best_price")

    seller=fields.Char(string="Seller")

    sellesperson_id=fields.Many2one("res.user",string="SellesMan")

    buyer=fields.Char(string="Buyer")
    

    delivery=fields.Boolean(string="Delivery")

    delivery_charge=fields.Integer(string="Delivery_charge",compute="_compute_delivery_chrarge")

    distance=fields.Integer(string="Distance shop-location(km)")


    color=fields.Integer()

    offer=[
        ('new','New'),
        ('Offer_received','Offer_Received'),
        ('Offer_accepted','Offer_Accepted'),
        ('canceled','Canceled'),
        ('sold','Sold'),
    ]

    state=fields.Selection(selection=offer,string="Status",default='new')

   

    total_medicine=fields.Integer(string="Total_Medicine",required=True)

    sold_out_medicine=fields.Integer(string="Sold_Out_Medcine",required=True)

    available_medicine=fields.Integer(string="Available_Medicine",readonly=True,compute="_compute_available")

    symptoms_ids=fields.Many2many("medicine.symptoms",string="Symptoms")

    block_id=fields.Many2one("medicine.block",string="Blocks")

    offer_price_ids=fields.One2many("medicine.offer","customer_id",string="offer")

    @api.depends("sold_out_medicine","total_medicine")
    def _compute_available(self):
        for record in self:
            val=record.total_medicine-record.sold_out_medicine
            if val<0:
                record.sold_out_medicine=''
                record.available_medicine=record.total_medicine
            else:
                record.available_medicine=val
    


    @api.depends("offer_price_ids.price")
    def _compute_best_price(self):
        val=0
        for record in self:
            for i in record.offer_price_ids:
                val=max(val,i.price)
            record.best_price=val



    @api.depends("distance")
    def _compute_delivery_chrarge(self):
        for record in self:
            record.delivery_charge=record.distance*50



    def action_For_Sold(self):
        for record in self:
            if record.state=="canceled":
                raise ValidationError("The Product is already Sold so you cannot Cancelled it")
            else:
                record.state="sold"


    def action_For_Cancel(self):
        for record in self:
            if record.state=="sold":
                raise ValidationError("The Product is already Cancelled so you cannot sold it") 
            else:
                record.state="canceled"


    @api.depends("delivery_charge","best_price")
    def _compute_selling_price(self):
        for record in self:
            record.selling_price=record.delivery_charge + record.best_price
    

    @api.onchange("delivery")
    def onchange_delivery(self):
        for record in self:
            if record.delivery==False:
                record.selling_price=record.best_price
            else:
                record.selling_price=record.best_price+record.delivery_charge




    _sql_constraints = [
        ('check_selling_price', 'CHECK(selling_price >= 0 )',
         'The selling_Price must be Positive.'),

        ('check_total_medicine', 'CHECK(total_medicine >= 0 )',
         'The total_medicine must be Positive.'),

        ('check_sold_out_medicine', 'CHECK(sold_out_medicine >= 0 )',
         'The sold_out_medicine must be Positive.'),

        ('check_available_medicine', 'CHECK(available_medicine >= 0)',
         'The available_medicine must be Positive.'),

        ('check_best_price', 'CHECK(best_price >= 0 AND best_price <= 100)',
         'The best_price must be Positive.'),
    ]



    _sql_constraints = [
        ('name_of_medicine_unique', 'unique(name_of_medicine)',
        'Field name_of_medicine must be unique')
    ]


    @api.constrains("sold_out_medicine")
    def sold_medicine(self):
        for record in self:
            val=record.sold_out_medicine
            if val<2:
                raise ValidationError("You must purchase atleast 2 medicine or more")

    @api.model
    def create(self,vals):
        for record in self:
            record.state="Offer_received"
        return super().create(vals)
    
