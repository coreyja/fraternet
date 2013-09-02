jQuery ->
  refreshHiddenValue = () ->
    values = []
    $('.majors_widget div.major select').each () ->
      values.push($(this).val())

    $('.majors_widget input[type="hidden"]').val(values.join(','))

  $(document).on 'change','.major select', () ->
    refreshHiddenValue()

  $('.majors_widget #add_major').click () ->
    console.log('Test')
    id = $(this).parents('div.majors_widget').attr('id')
    newMajor = $('li#' + id + '_hidden').clone().removeClass('hide').addClass('major')
    newMajor.removeAttr('id')

    newMajor.appendTo('#' + id + ' .majors')
    refreshHiddenValue()

  $(document).on 'click', 'button.remove_major', () ->
    $(this).parents('.major').remove()
    refreshHiddenValue()