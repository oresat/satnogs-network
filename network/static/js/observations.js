$(document).ready(function() {
    'use strict';

    $(function () {
        $('#datetimepicker-start').datetimepicker({
            useCurrent: false //https://github.com/Eonasdan/bootstrap-datetimepicker/issues/1075
        });
        $('#datetimepicker-end').datetimepicker({
            useCurrent: false //https://github.com/Eonasdan/bootstrap-datetimepicker/issues/1075
        });
        $('#datetimepicker-start').on('dp.change', function (e) {
            $('#datetimepicker-end').data('DateTimePicker').minDate(e.date);
        });
        $('#datetimepicker-end').on('dp.change', function (e) {
            $('#datetimepicker-start').data('DateTimePicker').maxDate(e.date);
        });
    });
    $('.selectpicker').selectpicker();


    $('.filter-section #status-selector label').click(function() {
        var checkbox = $(this);
        var input = checkbox.find('input[type="checkbox"]');

        if (input.prop('checked')) {
            checkbox.removeClass('btn-inactive');
        } else {
            checkbox.addClass('btn-inactive');
        }
    });

    $('.filter-section #results-selector label').click(function() {
        var checkbox = $(this);
        var input = checkbox.find('input[type="checkbox"]');

        if (input.prop('checked')) {
            checkbox.addClass('btn-inactive');
        } else {
            checkbox.removeClass('btn-inactive');
        }
    });

    // Check if filters should be displayed
    if (window.location.hash == '#collapseFilters') {
        $('#collapseFilters').hide();
    } else if ($('#collapseFilters').data('filtered') == 'True') {
        $('#collapseFilters').show();
    }

    // Open all observations in new tabs
    $('#open-all').click(function() {
        $('a.obs-link').each(function() {
            window.open($(this).attr('href'));
        });
    });
});
