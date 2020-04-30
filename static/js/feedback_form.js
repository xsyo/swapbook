$(document).ready(function(){

    $('#FeedBackForm').on('submit', function(e){
        e.preventDefault();

        var $that = $(this);
        formData = new FormData($that.get(0));
        $.ajax({
            url: '/users/feedback/',
            type: "POST",
            contentType: false,
            processData: false,
            data: formData,
            success: function(data){
                $('#successModal').modal('show');
            }
        })
    });

    $('#modalButton').on('click', function(){
        window.history.back();
    });

});