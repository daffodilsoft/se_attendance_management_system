# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Student Attendance',
    'version': '16.0',
    'summary': 'Track attendance with automated system.',
    'sequence': 15,
    'description': """ An attendance system is a digital tool that allows organizations, schools, or institutions to 
    track the attendance of their employees, students, or members in a virtual setting. Attendance systems typically use
     software or web-based applications to allow users to log in and mark their attendance.
     """,
    'category': 'Student Attendance Management System',
    'website': 'https://www.google.com',
    'images': [],
    'depends': [
        'smartedu_core',
        'base',
        'mail',
        'website',
    ],
    'data': [
        # Security
        'security/ir.model.access.csv',
        # Data

        # Wizards
        # views
        'views/attendance_create_view.xml',
        'views/se_student_view.xml',
        'views/menus.xml',
        'views/attendance_create_view.xml',
    ],
    'demo': [

    ],
    'qweb': [

    ],
    # 'assets': {
    #     'web.assets_backend':[
    #         'smartedu_attendance_management_system/static/src/js/attendance.js',
    #     ],
    # },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
