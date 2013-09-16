jQuery ->

  $('#carousel').jcarousel({
    'vertical': true,
    'wrap': 'circular',
  }).jcarouselAutoscroll({
    'interval': 3000,
    'autostart': true,
  })