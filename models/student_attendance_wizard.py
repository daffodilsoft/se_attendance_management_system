from odoo import api, fields, models


class StudentAttendance(models.TransientModel):
    _name = "student.attendance.wizard"
    _description = "Student Attendance"

    def count_total_attendances(self):
        batch_id = self.env.context.get('batch_id')
        students = self.env['se.student'].sudo().search({
            'batch_id.id', '=', batch_id.id
        })
        student_list = []
        for student in students:
            student_list.append({
                'name': student.name,
                'student_id_string': student.student_id_string,
                'attendance': student.attendance,
            })
        self.env['student.attendance.line'].sudo().create(student_list)


class StudentAttendanceLine(models.Model):
    _name = 'student.attendance.line'
    _description = 'StudentAttendanceLine'

    name = fields.Char()
    student_id_string = fields.Char()
    attendance = fields.Boolean()
    # attendance_id = fields.Many2one(comodel_name='student.attendance.wizard')

    @api.model
    def create(self, vals):
        res = super(StudentAttendanceLine, self).create(vals)
        return res

