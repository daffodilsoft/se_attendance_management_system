from odoo import models, fields


# Attendance creation model

class Attendance(models.Model):
    _name = 'se.attendance.management.system'
    _description = 'Track attendance with automated system'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    attendance_date = fields.Date(string='Date:', default=fields.Date.today())
    # name = fields.Char(string='Name:')
    name = fields.Many2one(comodel_name='se.subject', string="Course Name:")
    program_id = fields.Many2one(comodel_name='se.program')
    semester_id = fields.Many2one(comodel_name='se.semester')
    semester = fields.Char(string="Semester:")
    section = fields.Char(string="Section:")
    classroom = fields.Char(string="Class Room:")
    student_name = fields.Char(string="Student Name:")
    batch_id = fields.Many2one(comodel_name='se.batch')
    # remark = fields.Boolean(string="Remark")
    student_ids = fields.One2many(comodel_name="se.student",
                                  related='batch_id.student_ids')
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
