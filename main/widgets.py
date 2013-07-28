from django.forms import Select
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class MajorsWidget(Select):

    def __init__(self, attrs=None, choices=()):
        super(MajorsWidget, self).__init__(attrs,choices)

    def render(self, name, value, attrs=None, choices=()):
        if not value:
            value = []

        if isinstance(value, basestring):
            value = [v for v in value.split(',') if v]

        html = []


        for v in value:
            option_attrs = dict(attrs)
            option_attrs['id'] += '_%s' % v
            html.append('<div>' + super(MajorsWidget, self).render('', v, option_attrs, choices) + '</div>')
        html = render_to_string('widgets/MajorsWidget.html', {
            'choices': self.choices,
            'name': name,
            'values': value,
            'value_string': ','.join([str(v) for v in value]),
            'id': attrs['id'],
        })
        return mark_safe(html)

    def value_from_datadict(self, data, files, name):
        value = data.get(name, None)

        if isinstance(value, basestring):
            return [v for v in value.split(',') if v]
        return value
