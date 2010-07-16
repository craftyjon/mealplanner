// dashboard.js

$(document).ready(dashboardInit);

function dashboardInit()
{
    $('#btn-refresh').click(function() {
        location.reload(true);
    });

    $('#btn-signup').click(function() {
        location.href = "/lates/signup/";
    });

    $('#btn-dashboard').click(function() {
        location.href = "/lates/dashboard/";
    });

    $('#btn-overview').click(function() {
        location.href = "/lates/";
    });

}
