from django.shortcuts import render
def index(request):
    return render(request,'<h1>MineField</h1>',{})
# Create your views here.
