$(document).ready(function(){

    $('.proposal_confirmation_button').on('click', function(e){

        sentence_id = $(this).val();

        $.ajax({
            url: 'http://localhost:8000/sentence/proposal_confirmation/' + sentence_id + '/',
            type: "GET",
            success: function(data) {
                $('#pc_modal_body').html(data);
                $('#proposal_confirmation_form_submit_button').attr('value', $('.proposal_confirmation_button').val())
                $('#proposal_confirmation_modal').modal('show');
            },
        });
    });

    
})