from crispy_forms.helper import FormHelper
from django import forms
from crispy_forms.layout import Submit
from django.contrib.auth.forms import AuthenticationForm

from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from main.models import Brother
from .widgets import MajorsWidget

from fraternet.settings import FRATERNET_EMAIL_DOMAIN


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit', css_class="btn btn-primary btn-large"))


class BrotherForm(forms.ModelForm):
    class Meta:
        model = Brother

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
        super(BrotherForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = 'Use the same username used in the Brothers school email address.'

        self.fields['phone'].label = 'Phone Number'
        self.fields['grad_year'].label = 'Expected Graduation Year'

        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit', css_class="btn btn-primary btn-large"))

        self.helper['username'].wrap(AppendedText, "@%s" % FRATERNET_EMAIL_DOMAIN)


class BrotherCreateForm(BrotherForm):
    class Meta:
        model = Brother

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
        super(BrotherCreateForm, self).__init__(*args, **kwargs)

        self.fields['password'].help_text = 'Remember the password you are supplying. It can\'t be retrieved later.'