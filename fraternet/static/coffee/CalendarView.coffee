jQuery ->
  $('#calendar').fullCalendar({
    eventSources: [
      {
        url: '/rush/rush-events/',
        type: 'GET',
      },
      {
        url: '/rush/closedrush/',
        type: 'GET',
        color: 'red',
      },
    ]

    ignoreTimezone: false,
  })