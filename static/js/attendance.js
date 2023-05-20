odoo.define('smartedu_attendance_management_system.attendance', function (require) {
    "use strict";

    var rpc = require('web.rpc');
    var core = require('web.core');

    function onAttendanceChange(recordId, attendanceValue) {
        rpc.query({
            model: 'se.student',
            method: 'write',
            args: [[recordId], { 'attendance': attendanceValue }]
        }).then(function () {
            // Optional: Add any additional actions after saving the record
            // For example, refreshing the tree view or showing a success message.
            core.bus.trigger('reload_tree_view');
        });
    }

    return {
        onAttendanceChange: onAttendanceChange,
    };
});
