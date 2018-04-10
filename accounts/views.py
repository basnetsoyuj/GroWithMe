from django.shortcuts import render, redirect
from .forms import RegistrationForm
def register(request):
    if(request.method=='POST'):
        form=RegistrationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('accounts:login')
        else:
            return render(request,'accounts:hom')
    else:
        form=RegistrationForm()
        jinja_dict={'form':form,'register':True}
        return render(request,'accounts/register.html',jinja_dict)