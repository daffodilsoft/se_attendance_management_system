from odoo import models, fields


# Attendance creation model

class AttendanceSheet(models.Model):
    _name = 'se.sheet'
    _description = 'Track attendance with automated system'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    _inherit = 'se.attendance.management.system'
    attendance_date = fields.Date(string='Date:', comodel_name='se.attendance.management.system')
    semester_id = fields.Char(string="Semester:", comodel_name='se.attendance.management.system')