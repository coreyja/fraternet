from crispy_forms.helper import FormHelper
from django import forms
from crispy_forms.layout import Submit
from django.contrib.auth.forms import AuthenticationForm

from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions\

from main.models import Brother


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
        )

    helper = FormHelper()
    helper.layout = Layout (
        Field('username', css_class='input-xlarge'),
        Field('password', css_class='input-xlarge'),
        Field('first_name', css_class='input-xlarge'),
        Field('last_name', css_class='input-xlarge'),
        Field('phone', css_class='input-xlarge'),
        Field('grad_year', css_class='input-xlarge'),
        Field('majors', css_class='input-xlarge'),
        FormActions(
            Submit('submit', 'Submit', css_class="btn btn-primary btn-large"),
        )
    )

    def __init__(self, *args, **kwargs):
        super(BrotherForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = 'Use the same username used in the Brothers school email address.'
        self.fields['password'].help_text = 'Remember the password you are supplying. It can\'t be retrieved later.'

        self.fields['phone'].label = 'Phone Number'
        self.fields['grad_year'].label = 'Expected Graduation Year'