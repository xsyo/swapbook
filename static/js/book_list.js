$(document).ready(function(){

    var url = new URL(window.location.href);
    var page_num = 2;

    $('.sections').on('click', function(){
        
        var section_id = $(this).attr('value');
        url.searchParams.set('section', section_id);

        $('#section_button').text($(this).text());
        $('#section_button').trigger('click');
        $.ajax({
            type: "GET",
            data: {
                section: section_id,
            },
            success: function(data){
                $('#book_list').html(data);
                page_num = 2;
            }
        });
    });

    $('#book_add_button').on('click', function(){

        $.ajax({
            url: url.toString(),
            type: "GET",
            data: {
                page: page_num,
            },
            success: function(data){
                page_num++;
                $('#book_list').append(data);
            }
        });

    });

});