import logging
from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)

class PaymentCODController(http.Controller):
    _process_url = '/payment/cod/process'

    @http.route(_process_url, type='http', auth='public', methods=['POST'], csrf=False, website=True)
    def cod_feedback(self, **kwargs):
        _logger.info("Handling custom processing with cash on delivery")
        tx = request.env['payment.transaction'].sudo()._get_tx_from_notification_data('cod', kwargs)
        tx._process_notification_data(kwargs)
        return request.redirect('/shop/confirmation')