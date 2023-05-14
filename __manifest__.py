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
        'base',
        'mail',
        'website',
    ],
    'data': [
    # Security
    # Data
    # views
        'views/attendance_create_view.xml',
        'views/menus.xml',
    ],
    'demo': [
    
    ],
    'qweb': [
    
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
