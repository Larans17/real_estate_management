$(document).ready(function () {
    var url  = window.location.href;
   
    });
    
    
    
    function validateLogin() {
        if ($("#txtusername").val() == '' || $("#txtpassword").val() == ''){
    
            if ( $("#txtusername").val() == ''){
                
                $('#txtusername').addClass('error')
                $("#spanEmail").text("This field should not be empty") 
            }
    
            if ( $("#txtpassword").val() == ''){
                $('#txtpassword').addClass('error')
                $("#spanpassword").text("This field should not be empty")    
            }
            
            return false;
        }
    
    
    
        else {
    
            $('#loginform').submit()
        };
    
    };
    $('#txtusername').bind('keyup', function() {
        $('#txtusername').removeClass('error');
        $('#spanEmail').text('');
    });
    
    
    $('#txtpassword').bind('keyup', () => {
        $('#txtpassword').removeClass('error')
        $('#spanPassword').text('')
        })
    
    $("#txtpassword").on("keypress", function (e) {
        var key = e.which || e.keyCode;
        if (key === 13) {
            postMessage();
            e.preventDefault();
        }
        });