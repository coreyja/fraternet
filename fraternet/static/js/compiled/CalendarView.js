// Generated by CoffeeScript 1.6.3
(function() {
  jQuery(function() {
    return $('#calendar').fullCalendar({
      events: {
        url: '/events/events/',
        type: 'GET'
      }
    });
  });

}).call(this);
