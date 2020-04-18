$(document).ready(function(){

    $('#offering_form').on('submit', function(e){
        e.preventDefault();

        var $that = $(this);
        formData = new FormData($that.get(0));

        $.ajax({
            url: 'http://localhost:8000/sentence/offering/',
            type: "POST",
            contentType: false,
            processData: false,
            data: formData,
            success: function(data) {
                $('#header').after($('<div>', {
                    class: 'alert alert-success',
                    role: 'alert',
                    text: 'Предложение отправлено'
                }));
            },
            error: function(data){
                $('#header').after($('<div>', {
                    class: 'alert alert-danger',
                    role: 'alert',
                    text: 'Ошибка! Не правильно заполнена форма!'
                }));
            }
        })
    });


    $('#offering_form_submit_button').on('click', function(){
        $('#offering_form').submit();
        $('#myModal').modal('hide');
    });

})