jQuery ->

  $('div#create-comment form').ajaxForm( (data) ->
    if data.success
      comment = $(data.comment_html)

      comment.hide()

      comment.appendTo('div#comments-container')

      comment.slideDown()
  )