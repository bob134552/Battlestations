$(document).ready(function () {
    $('.update-form').submit(function (e) {
        e.preventDefault();
        var body = $(this).children('textarea[name=body]').val();
        var csrfmiddlewaretoken = $(this).children('input[name=csrfmiddlewaretoken]').val();
        var commentId = $(this).attr('id').split('comment_')[1];
        var form = $(this).parent();
        var comment = form.prev('.comment');
        var commentBody = comment.children('.comment-body');

        $.ajax({
            // Post data to update view in product views.
            type: 'POST',
            url: `/products/update_comment/${commentId}`,
            data: {
                body: body,
                csrfmiddlewaretoken: csrfmiddlewaretoken
            },
            success: function (data) {
                // Change the body to match the editted comment and hide form.
                commentBody.text(body)
                form.hide();
                comment.show();
                console.log(data)
            },
            error: function (data) {
                console.log(data)
            }
        });
    });
});