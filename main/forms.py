from crispy_forms.helper import FormHelper
from django import forms
from crispy_forms.layout import Submit
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):

    helper = FormHelper()
    helper.form_tag = True

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper.add_input(Submit('submit', 'Submit'))