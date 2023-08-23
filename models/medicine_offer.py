from odoo import models,fields,api
from odoo.exceptions import ValidationError
from odoo.tools import float_compare

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


    @api.model
    def create(self, vals):
        if vals.get("customer_id") and vals.get("price"):
            prop = self.env["medicine.management"].browse(vals["customer_id"])

            # We check if the offer is higher than the existing offers

            if prop.offer_ids:
                max_offer = max(prop.mapped("offer_ids.price"))
                if float_compare(vals["price"], max_offer, precision_rounding=0.01) <= 0:
                    raise ValidationError("The offer must be higher than %.2f" % max_offer)
            prop.state = "Offer_received"

        return super().create(vals)
    
