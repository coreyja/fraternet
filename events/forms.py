from crispy_forms.helper import FormHelper
from django import forms
from crispy_forms.layout import Submit
from django.contrib.auth.forms import AuthenticationForm

from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from .models import Event
from .widgets import DateTimeWidget


class EventForm(forms.ModelForm):
    class Meta:
        model = Event


    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.add_input(Submit('submit', 'Submit', css_class="btn btn-primary btn-large"))