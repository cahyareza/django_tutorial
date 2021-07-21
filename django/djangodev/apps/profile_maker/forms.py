from django import forms
from .models import User_profile

class Profile_Form(forms.ModelForm):

    class Meta:
        model = User_profile
        fields = [
            'fname',
            'lname',
            'technologies',
            'email',
            'display_picture'
        ]