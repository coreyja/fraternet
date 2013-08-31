from crispy_forms.helper import FormHelper
from django import forms
from crispy_forms.layout import Submit

from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from .models import Rushie
from main.widgets import MajorsWidget

from fraternet.settings import FRATERNET_EMAIL_DOMAIN

class RushieEditForm(forms.ModelForm):

    class Meta:
        model = Rushie

        exclude = (
            'last_login',
            'is_superuser',
            'groups',
            'user_permissions',
            'email',
            'is_staff',
            'is_active',
            'date_joined',
            'password',
        )

        widgets = {
            'majors': MajorsWidget
        }

    def __init__(self, *args, **kwargs):
        super(RushieEditForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = 'Use the same username used in your school email address.'

        self.fields['phone'].label = 'Phone Number'
        self.fields['grad_year'].label = 'Expected Graduation Year'

        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit', css_class="btn btn-primary btn-large"))

        self.helper['username'].wrap(AppendedText, "@%s" % FRATERNET_EMAIL_DOMAIN)


class RushieCreateForm(RushieEditForm):

    class Meta:
        model = Rushie

        exclude = (
            'last_login',
            'is_superuser',
            'groups',
            'user_permissions',
            'email',
            'is_staff',
            'is_active',
            'date_joined',
        )

        widgets = {
            'majors': MajorsWidget
        }

    def __init__(self, *args, **kwargs):
        super(RushieCreateForm, self).__init__(*args, **kwargs)

        self.fields['password'].help_text = 'Remember the password you are supplying. It can\'t be retrieved later.'