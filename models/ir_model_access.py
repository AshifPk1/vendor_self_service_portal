from odoo import api, models


class IrModelAccess(models.Model):
    """Inherits the ir model access for restricting
     the user from accessing data."""
    _inherit = 'ir.model.access'

    @api.model
    def check(self, model, mode, raise_exception=True):
        """Overrides the default check method to allow
         only read access to the user."""
        res = super().check(model, mode, raise_exception=raise_exception)
        if self.env.user.has_group('vendor_self_service_portal.vendor_user_group') \
                and mode in ('write', 'create', 'unlink'):
            if model in ['vendor.forecast']:
                return False
            else:
                return res
        return res
