$( document ).ready(function() {
    console.log( "ready!" );
    $('#login_form').keydown(function(e) {
        var key = e.which;
        if (key == 13) {
        // As ASCII code for ENTER key is "13"
            $('#login_form').submit(); // Submit form code
        }
    });
});

