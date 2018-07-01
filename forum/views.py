from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView,CreateView,View
from .models import ForumSection
from django.shortcuts import get_object_or_404,reverse,redirect
from .forms import PostCreationForm
from django.contrib.auth.models import User
class ForumIndexView(LoginRequiredMixin,TemplateView):
    login_url = "/accounts/login/"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({'forum': True, 'logged_in': True})
        return context
    template_name = "forum/forum.html"

class ForumSearchView(LoginRequiredMixin,TemplateView):
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context.update({'forum': True, 'logged_in': True})
        return context
    template_name = "forum/forum_search.html"

class ForumExploreView(LoginRequiredMixin,ListView):
    def get_queryset(self):
        object_list = ForumSection.objects.all()
        return object_list

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context.update({'forum':True,'logged_in':True,'explore':True})
        return context
    template_name = "forum/forum_explore.html"


class ForumSectionDetailView(LoginRequiredMixin,DetailView):
    def get_object(self):
        section_link=self.kwargs.get("section_link")
        obj=get_object_or_404(ForumSection,section_link=section_link)
        return obj
    def get_context_data(self, *args,**kwargs):
        section_link = self.kwargs.get("section_link")
        obj = get_object_or_404(ForumSection, section_link=section_link)
        subscribers = list(obj.subscribers.all())
        is_subscribed= self.request.user in subscribers
        context = super().get_context_data(*args,**kwargs)
        context.update({'forum': True, 'logged_in': True, 'explore': True ,'is_subscribed':is_subscribed})
        return context
    template_name = "forum/forum_detail.html"

class PostCreateView(LoginRequiredMixin,CreateView):
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context.update({'forum':True,'logged_in':True,'explore':True})
        return context
    form_class = PostCreationForm
    template_name = "forum/post_create.html"
    success_url = "/forum/explore/"

class Subscribe(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        section_pk=kwargs['pk']
        loggedin_user=self.request.user
        section = get_object_or_404(ForumSection, id=section_pk)
        subscribers = list(section.subscribers.all())
        is_subscribed = self.request.user in subscribers
        if section and not is_subscribed :
            section.subscribers.add(loggedin_user)
        return redirect('forum:sections',section_link=section.section_link)
