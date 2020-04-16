$(document).ready(function(){

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }


    $(".append_list").on('click', function(e){
        var book_id = $(this).attr("value");
        var append = $(this).attr("data-append");
        var csrftoken = getCookie('csrftoken');

        $(this).attr('id', 'this-button');
        
        $.ajax({
            url: 'http://localhost:8000/my_books/add/',
            type: "POST",
           
            data: {
                csrfmiddlewaretoken: csrftoken,
                book_id: book_id,
                append_in_list: append,
            },
            success: function(data){
                $('#this-button').toggleClass('btn-danger btn-primary');
                if (append == 'true'){
                    $('#this-button').attr("data-append", "false");
                    $('#this-button').html('Удалить из моего списка');
                }
                else if (append == 'false') {
                    $('#this-button').attr("data-append", "true");
                    $('#this-button').html('Добавить в мой список');
                }
                $('#this-button').removeAttr('id');
                
            }
        });
    });

    $(".append_desired").on('click', function(e){
        var book_id = $(this).attr("value");
        var append = $(this).attr("data-append");
        var csrftoken = getCookie('csrftoken');

        $(this).attr('id', 'this-button-desired');
        
        $.ajax({
            url: 'http://localhost:8000/desired_books/add/',
            type: "POST", 
 
            data: {
                csrfmiddlewaretoken: csrftoken,
                book_name_id: book_id,
                add_to_desired: append,
            },
            success: function(data){
                $('#this-button-desired').toggleClass('btn-danger btn-primary');
                if (append == 'True'){
                    $('#this-button-desired').attr("data-append", "False");
                    $('#this-button-desired').html('Удалить из желаемых');
                }
                else if (append == 'False') {
                    $('#this-button-desired').attr("data-append", "True");
                    $('#this-button-desired').html('Добавить в желаемые');
                }
                $('#this-button-desired').removeAttr('id');
                
            }
        });
    });
})