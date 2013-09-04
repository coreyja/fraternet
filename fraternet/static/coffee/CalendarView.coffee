jQuery ->
  $('#calendar').fullCalendar({
    events: {
      url: '/events/events/',
      type: 'GET',
    }
  })