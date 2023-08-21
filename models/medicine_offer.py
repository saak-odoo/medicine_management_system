from odoo import models,fields,api

class MedicineOffer(models.Model):
    _name="medicine.offer"
    _description="Offer for the medicine"
    _order="price asc"
    _rec_name="name_of_customer"

    price=fields.Integer(string="Price")

    name_of_customer=fields.Many2one("res.partner",string="Name_of_Customer")

    customer_id=fields.Many2one("medicine.management",string="Customer_id")

    status=[
        ('accepted','Accepted'),
        ('rejected','Rejected')
    ]

    status=fields.Selection(selection=[('accepted','Accepted'),('rejected','Rejected')],string="Status")


    validity=fields.Integer(default=7,string="Validity")

    date_deadline=fields.Date(string="Date_deadline")
    




    @api.depends("customer_id.state")
    def action_confirm(self):
        for record in self:
            record.status="accepted"
            p_id=record.name_of_customer.id
            val=record.name_of_customer.search_read([('id','=',p_id)])
            for i in record.customer_id:
                i.state="Offer_accepted"
                i.buyer=val[0]['display_name']
                i.seller="Aman Kumar Sah"
    

    @api.depends("customer_id.state")
    def action_cancel(self):
        for record in self:
            record.status="rejected"
            for i in record.customer_id:
                i.state="canceled"
                

    _sql_constraints = [
        ('check_price', 'CHECK(price >= 0)',
            'The Price must be Positive.'),
    ]