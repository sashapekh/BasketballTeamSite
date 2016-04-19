from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *


class SimpleForm(forms.Form):
    username = forms.CharField(
            label=" Your username", required=False)
    password = forms.CharField(
            label=" Enter password", required=True, widget=forms.PasswordInput)
    email = forms.EmailField(
            required=True, label='Enter email'
    )

    helper = FormHelper()
    helper.form_class = 'form-horizontal myform'
    helper.form_method = 'post'
    helper.form_action = ''

    helper.layout = Layout(
        Div(Div(Field('username'), css_class='col-sm-12 '), css_class='form-group has-success'),
        Div(Div(Field('password'), css_class='col-sm-12 '), css_class='form-group has-warning'),
        Div(Div(Field('email'), css_class='col-sm-12 '), css_class='form-group has-warning'),
        HTML("{% if success %} <p>Operation was successful</p> {% endif %}")

    )
    helper.add_input(Submit('submit','Submit'))

