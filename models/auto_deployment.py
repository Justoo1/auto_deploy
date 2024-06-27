from odoo import models, fields, api


class AutoDeployment(models.Model):
    _name = "auto.deployment"
    _description = "Automatic Deployment"

    name = fields.Char()
    address = fields.Text()