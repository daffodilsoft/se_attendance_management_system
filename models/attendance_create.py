from odoo import models, fields


# Attendance creation model

class Attendance(models.Model):
    _name = 'se.attendance.management.system'
    _description = 'Track attendance with automated system'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    attendance_date = fields.Date(string='Date:', default=fields.Date.today())
    name = fields.Char(string='Name:')
    attendance_course = fields.Char(string="Course Name:")
    program_id = fields.Many2one(comodel_name='se.program')
    semester_id = fields.Many2one(comodel_name='se.semester')
    # notice_type = fields.Char(related='semester_id.name')
    semester = fields.Char(string="Semester:")
    section = fields.Char(string="Section:")
    classroom = fields.Char(string="Class Room:")
    active = fields.Boolean(string='Active:', default=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Attendance Start'),
        ('done', 'Attendance Confirm'),
        ('cancel', 'Cancelled'),
    ], default='draft', string='Status')

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'
