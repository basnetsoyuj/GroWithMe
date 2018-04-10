from django.shortcuts import render
from django.views.generic import TemplateView
def index(request):
    dict_jinja = {'home':True,'login':False}
    if(request.user.is_authenticated):
        dict_jinja['logged_in']= True
    else:
        pass
    return render(request,'home/index.html',dict_jinja)

class indexView(TemplateView):
    template_name = "home/index.html"

def about(request):
    pass