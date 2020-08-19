# Copyright 2015 Antiun Ingeniería, S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class Lead(models.Model):
    _inherit = "crm.lead"

    x_vereda = fields.Char(
        string="Vereda",
        help="Tax Identification Number. The first 2 characters are the "
        "country code.",
    )

    def _create_lead_partner(self):
        """Add VAT to partner."""
        return super(
            Lead, self.with_context(default_x_vereda=self.x_vereda)
        )._create_lead_partner()

    def _onchange_partner_id_values(self, partner_id):
        """Recover VAT from partner if available."""
        result = super(Lead, self)._onchange_partner_id_values(partner_id)
        if not partner_id:
            return result
        partner = self.env["res.partner"].browse(partner_id)
        if partner.x_pvereda:
            result["x_vereda"] = partner.x_pvereda
        return result
