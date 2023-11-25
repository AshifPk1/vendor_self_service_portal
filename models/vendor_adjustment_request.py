from odoo import models, fields


class VendorAdjustmentRequest(models.Model):
    """Create model for vendor adjustment request form"""

    _name = 'vendor.adjustment.request'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'order_id'

    order_id = fields.Many2one('sale.order', 'Sale Order', tracking=True)
    adjustment_detail = fields.Text("Adjustment Details", tracking=True)
    comment = fields.Text('Comment')
    state = fields.Selection([('draft', 'Draft'), ('submitted', 'Submitted')], default='draft', tracking=True)

    def reset_to_draft(self):
        """
        Reset to draft
        sending mail to teams
        """

        self.write({
            'state': 'draft'
        })

    def submit_request(self):
        """change state to submitted"""

        self.write({
            'state': 'submitted'
        })

        template = self.env.ref(
            'vendor_self_service_portal.email_template_order_adjustment_submission')

        template.send_mail(self.id, force_send=True)
