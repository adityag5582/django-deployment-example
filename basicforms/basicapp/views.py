from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')

def form_page_view(request):
    form_object = forms.userform()
    if request.method == 'POST':
        form_object = forms.userform(request.POST)
        if form_object.is_valid():
            print("validation success")
            print("NAME: " + form_object.cleaned_data['name'])
            print("EMAIL: " + form_object.cleaned_data['email'])
            print("TEXT: " + form_object.cleaned_data['text'])
    return render(request,'basicapp/form_page.html',{'form':form_object})
