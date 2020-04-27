$('.delete_book').hide();
$('.delete_desired_book').hide();

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


    $(".delete_book").on('click', function(e){
        var book_id = $(this).attr("value");
        var append = "false";
        var csrftoken = getCookie('csrftoken');

        $(this).parent().parent().parent().attr("id", "delete-item");
        
        $.ajax({
            url: '/my_books/add/',
            type: "POST",
           
            data: {
                csrfmiddlewaretoken: csrftoken,
                book_id: book_id,
                append_in_list: append,
            },
            success: function(data){
                $('#delete-item').remove();
            }
        });
    });

    $(".delete_desired_book").on('click', function(e){
        var book_id = $(this).attr("value");
        var append = 'False';
        var csrftoken = getCookie('csrftoken');

        $(this).parent().parent().parent().attr("id", "delete-item");
        
        $.ajax({
            url: '/desired_books/add/',
            type: "POST",
            data: {
                csrfmiddlewaretoken: csrftoken,
                book_name_id: book_id,
                add_to_desired: append,
            },
            success: function(data){
                $('#delete-item').remove();
            }
        });
    });


    $('#my_book_btn').on('click', function(){
        var value = $(this).val();
        if (value == 'off') {
            $('.delete_book').show();
            $(this).val('on');
        }else if (value == 'on') {
            $('.delete_book').hide();
            $(this).val('off');
        }
    });

    $('#desired_book_btn').on('click', function(){
        var value = $(this).val();
        if (value == 'off') {
            $('.delete_desired_book').show();
            $(this).val('on');
        }else if (value == 'on') {
            $('.delete_desired_book').hide();
            $(this).val('off');
        }
    });

})