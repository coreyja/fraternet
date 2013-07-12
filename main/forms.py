from crispy_forms.helper import FormHelper
from django import forms
from crispy_forms.layout import Submit
from django.contrib.auth.forms import AuthenticationForm

from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class LoginForm(AuthenticationForm):

    helper = FormHelper()
    helper.form_tag = True
    helper.layout = Layout(
        Field('username', css_class='input-xlarge'),
        Field('password', css_class='input-xlarge'),
        FormActions(
            Submit('submit', 'Submit', css_class="btn btn-primary btn-large"),
        )
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)