$(document).ready(function(){

    $('.proposal_confirmation_button').on('click', function(e){

        sentence_id = $(this).val();
        $('#proposal_confirmation_form_submit_button').attr('value',sentence_id);
        
        $.ajax({
            url: '/sentence/proposal_confirmation/' + sentence_id + '/',
            type: "GET",
            success: function(data) {
                $('#pc_modal_body').html(data);
                
                $('#proposal_confirmation_modal').modal('show');
            },
        });
    });

    $('.rejection_of_offer_button').on('click', function(){

        sentence_id = $(this).val();
        $('#rejection_of_offer_form_submit_button').attr('value', sentence_id);

        $.ajax({
            url: '/sentence/rejection_of_offer/' + sentence_id + '/',
            type: "GET",
            success: function(data) {
                $('#rejection_of_offer_modal_body').html(data);
                
                $('#rejection_of_offer_modal').modal('show');
            },
        });

    });

})