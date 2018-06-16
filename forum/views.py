from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class ForumIndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        context=super(ForumIndexView,self).get_context_data(*args,**kwargs)
        context={'forum':True}
        if not request.user.is_authenticated:
            return render(request,'forum/forum_not_logged.html',context)
        else:
            context['logged_in']=True
            return render(request,'forum/forum.html', context)
class ForumSearchView(TemplateView):
    def get(self, request, *args, **kwargs):
        context=super(ForumSearchView,self).get_context_data(*args,**kwargs)
        context={'forum':True}
        if not request.user.is_authenticated:
            return render(request,'forum/forum_not_logged.html',context)
        else:
            context['logged_in']=True
            return render(request,'forum/forum_search.html', context)

