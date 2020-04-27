$(document).ready(function(){

    $('#addBookInUserListForm').on('submit', function(e){
        e.preventDefault();

        var $that = $(this);
        formData = new FormData($that.get(0));
        $.ajax({
            url: 'http://localhost:8000/my_books/add/',
            type: "POST",
            contentType: false,
            processData: false,
            data: formData,
            success: function(data){
                append_in_list = $("input[name='append_in_list']").val();
                if (append_in_list == 'true') {
                    $("input[name='append_in_list']").val('false');
                    $('#addBookInUserListBtn').html('Удалить из моего списка');               
                }
                else if (append_in_list == 'false') {
                    $("input[name='append_in_list']").val('true');
                    $('#addBookInUserListBtn').html('Добавить в мой список');
                }
                
                $('#addBookInUserListBtn').toggleClass('btn-danger btn-primary');
                
            }
        })
    });

    $('#AddToDesiredForm').on('submit', function(e){
        e.preventDefault();

        var $that = $(this);
        formData = new FormData($that.get(0));
        $.ajax({
            url: '/desired_books/add/',
            type: "POST",
            contentType: false,
            processData: false,
            data: formData,
            success: function(data){
                add_to_desired = $("input[name='add_to_desired']").val();
                if (add_to_desired == 'True') {
                    $("input[name='add_to_desired']").val('False');
                    $('#AddToDesiredBtn').html('Удалить из желаемых');               
                }
                else if (add_to_desired == 'False') {
                    $("input[name='add_to_desired']").val('True');
                    $('#AddToDesiredBtn').html('Добавить в желаемые');
                }
                
                $('#AddToDesiredBtn').toggleClass('btn-danger btn-primary');
                
            }
        })
    });
})