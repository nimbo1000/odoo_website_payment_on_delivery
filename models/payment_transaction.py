from odoo import models, api
from odoo.addons.cash_on_delivery.controllers.payment_controller import PaymentCODController

class PaymentTransactionCOD(models.Model):
    _inherit = 'payment.transaction'

    def _get_specific_rendering_values(self, processing_values):
        res = super()._get_specific_rendering_values(processing_values)
        if self.provider_code != 'cod':
            return res

        return {
            'api_url': PaymentCODController._process_url,
            'reference': self.reference,
        }


    @api.model
    def _get_tx_from_notification_data(self, provider_code, notification_data):
        if provider_code != 'cod':
            return super()._get_tx_from_notification_data(provider_code, notification_data)
        reference = notification_data.get('reference')
        tx = self.search([('reference', '=', reference), ('provider_code', '=', 'cod')])
        return tx

    def _process_notification_data(self, notification_data):
        super()._process_notification_data(notification_data)
        if self.provider_code != 'cod':
            return
        self._set_done()
