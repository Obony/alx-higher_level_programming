#!/usr/bin/node

$('document').ready(function () {
    $('DIV#toggle_header').click(function () {
        if ($('header').hasClass('green')) {
            $('header').removeClass('green').addClass('red');
        } else {
            $('header').removeClass('red').addClass('green');
        }
    });    
});

//alternatively;
//$(document).ready(function () {
//    $('#toggle_header').click(function () {
//       $('header').toggleClass('red green');
//    });
//});