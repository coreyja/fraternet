jQuery ->
  refreshHiddenValue = () ->
    values = []
    $('.majors_widget li.major select').each () ->
      values.push($(this).val())

    $('.majors_widget input[type="hidden"]').val(values.join(','))

  $(document).on 'change','.major select', () ->
    refreshHiddenValue()

  $('.majors_widget #add_major').click () ->
    id = $(this).parents('div.majors_widget').attr('id')
    newMajor = $('li#' + id + '_hidden').clone().removeClass('hide').addClass('major')
    newMajor.removeAttr('id')

    newMajor.appendTo('#' + id + ' .majors')
    refreshHiddenValue()

  $(document).on 'click', 'button.remove_major', () ->
    $(this).parents('.major').remove()
    refreshHiddenValue()

  $('.majors').sortable({
    update: refreshHiddenValue(),
  });