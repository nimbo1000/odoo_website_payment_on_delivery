from odoo import models, fields

class PaymentAcquirerCOD(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('cod', 'Cash on Delivery')],
        ondelete={'cod': 'set default'}
    )

    def cod_get_form_action_url(self):
        return '/payment/cod/process'
