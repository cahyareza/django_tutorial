from django import forms

class signUp(forms.Form):
    first_name = forms.CharField(initial='First Name',)
    last_name = forms.CharField()
    email = forms.EmailField(help_text = 'write your email',)
    address = forms.CharField(required=False,)
    technology = forms.CharField(initial='Django', disabled=True,)
    age = forms.IntegerField()
    password = forms.CharField(widget = forms.PasswordInput)
    re_password = forms.CharField(help_text='reenter your password', widget=forms.PasswordInput)
