# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SaleOrder(models.AbstractModel):
    _inherit = "sale.order"

    def change_invoices_state(self):
            self.invoice_status = "invoiced"


    def change_invoices_state_masive(self):
            for record in self:
                record.change_invoices_state()
       
