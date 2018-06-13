from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class ForumIndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request,'forum/forum_not_logged.html',{})
        else:
            return render(request, 'forum/forum.html', {})
