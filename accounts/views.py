from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from django.views.generic import DetailView
def register(request):
    if not request.user.is_authenticated:
        if(request.method=='POST'):
            form=RegistrationForm(request.POST)
            if(form.is_valid()):
                form.save()
                messages.success(request, 'Successfully Signed Up ! Now you can log into you account')
                return redirect('accounts:login')
            else:
                problem=form.errors.as_data()
                for key in problem:
                    for a in range(0,len(problem[key])):
                        if key=="password1" or key=="password2":
                            #Since The key is displayed to user : 'password1' and 'password2' would be redundant so they must both mean 'password'
                            finalkey='password'
                        else:
                            finalkey=key
                        messages.error(request,finalkey+" : "+''.join(problem[key][a]))
                return redirect('accounts:register')
        else:
            form=RegistrationForm()
            jinja_dict={'form':form,'register':True}
            return render(request,'accounts/register.html',jinja_dict)
    else:
        return redirect('home:index')

class UserProfile(DetailView):
    pass
