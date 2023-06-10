$(document).ready(function() {
    $('#get-env-variable').click(function() {
        $.get('/env_variable', function(response) {
            var envVariable = response.env_variable;
            var envVariableHtml = '<p>Value of the Environment Variable is : <span>' + envVariable + '</span></p>';
            $('#env-variable-container').html(envVariableHtml);
        });
    });
});