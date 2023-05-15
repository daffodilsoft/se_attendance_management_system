from odoo import models, api, fields, _


class SeStudent(models.Model):
    _inherit = 'se.student'

    attendance_create_id = fields.Many2one(comodel_name='se.attendance.management.system')
