jQuery ->

  $('div#create-comment form button.submit').click () ->
    $(this).parents('form').ajaxSubmit( (data) ->
      if data.success
        comment = $(data.comment_html)

        comment.hide()

        comment.appendTo('div#comments-container')

        comment.slideDown()
    )