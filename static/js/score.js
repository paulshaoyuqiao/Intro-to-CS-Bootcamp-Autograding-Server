$(document).ready(function() {
    $('.ui.dropdown').dropdown();
    $('#default').show();
    const assignments = ['hw1', 'lab1', 'hw2', 'lab2', 'hw3', 'lab3'];
    for (var i = 0; i < assignments.length; i++) {
        $('#' + assignments[i]).hide();
    }
    $('.ui.dropdown').dropdown({
        onChange: function (val) {
            $('#default').hide();
            for (var i = 0; i < assignments.length; i++) {
                curr_name = assignments[i]
                if (curr_name == val) {
                    $('#' + curr_name).show();
                } else {
                    $('#' + curr_name).hide();
                }
            }
        }
    });
});
