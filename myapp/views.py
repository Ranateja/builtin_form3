from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.core.files.storage import FileSystemStorage



from myapp.utilities import store_image

from myapp import forms

def builtinforms(request):
    if request.method=="POST":
        form=forms.SampleForm(request.POST,request.FILES)#im creating a form instance with the data filled the all the firlds will get th
        #the specified value
        if form.is_valid():
            #cleaned_data is varible in form instance that holds the dictonary containing the data that we 
            #have filled
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')
            email=form.cleaned_data.get('email')
            phno=form.cleaned_data.get('phno')
            pwd=form.cleaned_data.get('pwd')
            birth_day=form.cleaned_data.get('birth_day')
            birth_month=form.cleaned_data.get('birth_month')
            birth_year=form.cleaned_data.get('birth_year')
            gender=form.cleaned_data.get('gender')
            image=form.cleaned_data.get('image')
            store_image(image)
            data=form.cleaned_data
            return render(request,"display_data.html",context=data)
    form=forms.SampleForm()
    return render(request,'builtin.html',{'form':form})

#forms is a file or a library 
#in forms Form is a class so we inherit from forms.Form