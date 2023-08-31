from odoo import models
from odoo import fields

class inherited(models.Model):
    _inherit="res.user"
    _order="id asc"
    _rec_name="name"

    name=fields.Char(string="Name")
    color=fields.Integer()