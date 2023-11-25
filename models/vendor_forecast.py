from odoo import models, fields, api, _
from odoo.exceptions import UserError


class VendorForecast(models.Model):
    """Create new model for vendor request"""

    _name = 'vendor.forecast'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    product_id = fields.Many2one('product.product', "Product", tracking=True)
    expected_quantity = fields.Integer("Expected Quantity", tracking=True)
    forecast_date = fields.Date('Forecast Date', tracking=True)
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed')], default='draft', tracking=True)

    def name_get(self):
        """Set display name"""

        result = []
        for forecast in self:
            name = str(forecast.product_id.name) + "--" + str(forecast.forecast_date)
            result.append((forecast.id, name))
        return result

    def reset_to_draft(self):
        """Reset to draft"""
        if self.env.user.has_group('vendor_self_service_portal.vendor_user_group'):
            raise UserError(_("You Can't Perform Operation."))
        self.write({
            'state': 'draft'
        })

    def action_confirm(self):
        """confirm Button State Changed to confirm"""
        if self.env.user.has_group('vendor_self_service_portal.vendor_user_group'):
            raise UserError(_("You Can't Perform Operation."))

        self.write({
            'state': 'confirmed'
        })
