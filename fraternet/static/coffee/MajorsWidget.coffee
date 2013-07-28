jQuery ->
  refreshHiddenValue = () ->
    values = []
    $('.majors_widget div.major select').each () ->
      values.push($(this).val())

    $('.majors_widget input[type="hidden"]').val(values.join(','))

  $(document).on 'change','div.major select', () ->
    refreshHiddenValue()

  $('.majors_widget #add_major').click () ->
    id = $(this).parents('div.majors_widget').attr('id')
    newMajor = $('select#' + id + '_hidden').parent().clone().removeClass('hide')
    newMajor.find('select').removeAttr('id')

    newMajor.appendTo('div#' + id + ' .majors')
    refreshHiddenValue()

  $(document).on 'click', '#remove_major', () ->
    $(this).parents('div.major').remove()
    refreshHiddenValue()