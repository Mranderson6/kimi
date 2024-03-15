// JavaScript Document
$(document).ready(function() {

    "use strict";

    /*----------------------------------------------------*/
    /*  Comment Form Send Function
    /*----------------------------------------------------*/

    

    $("#reset").on('click', function() {
        $(".form-control").removeClass("success").removeClass("error");
    });

    /*----------------------------------------------------*/
    /*  Comment Form Validation
    /*----------------------------------------------------*/
    
    $(".comment-form").validate({
        rules:{ 
                name:{
                    required: true,
                    minlength: 1,
                    maxlength: 16,
                },
                email:{
                    required: true,
                    email: true,
                },              
                message:{
                    required: true,
                    minlength: 2,
                    }
                },
                messages:{
                        name:{
                            required: "Please enter no less than (1) characters"
                        }, 
                        email:{
                            required: "We need your email address to contact you",
                            email: "Your email address must be in the format of name@domain.com"
                        }, 
                        message:{
                            required: "Please enter no less than (2) characters"
                        }, 
                    }
    });
    
})



