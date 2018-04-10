from django.shortcuts import render

def index(request):
    dict_jinja = {'home':True,'login':False}
    if(request.user.is_authenticated):
        dict_jinja['logged_in']= True
    else:
        pass
    return render(request,'home/index.html',dict_jinja)

def about(request):
    pass