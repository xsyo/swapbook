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


    $("#book_list").on('click', '.append_list', function(e){
        var book_id = $(this).attr("value");
        var append = $(this).attr("data-append");
        var csrftoken = getCookie('csrftoken');

        $(this).attr('id', 'this-button');
        
        $.ajax({
            url: '/my_books/add/',
            type: "POST",
           
            data: {
                csrfmiddlewaretoken: csrftoken,
                book_id: book_id,
                append_in_list: append,
            },
            success: function(data){
                var btn = $('#this-button');
                btn.toggleClass('btn-danger btn-primary');
                if (append == 'true'){
                    btn.attr("data-append", "false");
                    btn.html('Удалить из моего списка');
                }
                else if (append == 'false') {
                    btn.attr("data-append", "true");
                    btn.html('Добавить в мой список');
                }
                btn.removeAttr('id');
                
            }
        });
    });

    $("#book_list").on('click', '.append_desired', function(e){
        var book_id = $(this).attr("value");
        var append = $(this).attr("data-append");
        var csrftoken = getCookie('csrftoken');

        $('.append_desired[value="'+book_id+'"]').toggleClass('this-button-desired');
        
        $.ajax({
            url: '/desired_books/add/',
            type: "POST", 
 
            data: {
                csrfmiddlewaretoken: csrftoken,
                book_name_id: book_id,
                add_to_desired: append,
            },
            success: function(data){
                var btn = $('.this-button-desired');
                btn.toggleClass('btn-danger btn-primary');
                if (append == 'True'){
                    btn.attr("data-append", "False");
                    btn.html('Удалить из желаемых');
                }
                else if (append == 'False') {
                    btn.attr("data-append", "True");
                    btn.html('Добавить в желаемые');
                }
                btn.toggleClass('this-button-desired');
                
            }
        });
    });
})