from django.shortcuts import render
from. import forms

# Create your views here.
def regForm(request):
    form = forms.signUp()
    if request.method == 'POST':
        form = forms.signUp(request.POST)
        html = 'we have received this form again'
        if form.is_valid():
            html = html + "The form is valid"
    else:
        html = 'wellcome for first time'

    return render(request,'signup.html', {'html': html, 'form': form})
