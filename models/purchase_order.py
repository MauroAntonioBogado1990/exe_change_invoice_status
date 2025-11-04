# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class PurchaseOrder(models.AbstractModel):
    _inherit = "purchase.order"

    def change_invoices_state(self):
        self.invoice_status = "invoiced"
