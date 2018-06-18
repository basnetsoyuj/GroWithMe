from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import ForumSection
# Create your views here.
class ForumIndexView(TemplateView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['forum'] = True
        if self.request.user.is_authenticated:
            context['logged_in'] = True
            return context
        else:
            return context

    def get_template_names(self):
        if self.request.user.is_authenticated:
            template_name = "forum/forum.html"
        else:
            template_name = "forum/forum_not_logged.html"
        return template_name

class ForumSearchView(TemplateView):
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['forum'] = True
        if self.request.user.is_authenticated:
            context['logged_in'] = True
            return context
        else:
            return context
    def get_template_names(self):
        if self.request.user.is_authenticated:
            template_name = "forum/forum_search.html"
        else:
            template_name = "forum/forum_not_logged.html"
        return template_name

class ForumExploreView(ListView):
    def get_queryset(self):
        if self.request.user.is_authenticated:
            object_list = ForumSection.objects.all()
            return object_list
        else:
            return None

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['forum'] = True
        if self.request.user.is_authenticated:
            context['logged_in'] = True
            context['explore'] = True
            return context
        else:
            return context
    def get_template_names(self):
        if self.request.user.is_authenticated:
            template_name = "forum/forum_explore.html"
        else:
            template_name = "forum/forum_not_logged.html"
        return template_name