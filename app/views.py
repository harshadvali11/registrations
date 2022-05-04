from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.forms import *

def registration(request):
    uf=UserForm()
    pf=ProfileForm()
    d={'uf':uf,'pf':pf}
    if request.method=='POST' and request.FILES:
        ud=UserForm(request.POST)
        pd=ProfileForm(request.POST,request.FILES)
        if ud.is_valid() and pd.is_valid():
            u=ud.save(commit=False)
            u.set_password(ud.cleaned_data.get('password'))
            u.save()
            p=pd.save(commit=False)
            p.user=u
            p.save()
            return HttpResponse('registarion is successfull')
    return render(request,'registration.html',d)