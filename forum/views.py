from django.views.generic import TemplateView,ListView,DetailView,CreateView
from .models import ForumSection
from django.shortcuts import get_object_or_404
from .forms import PostCreationForm
class ForumIndexView(TemplateView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['forum'] = True
        if self.request.user.is_authenticated:
            context['logged_in'] = True
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
    def get_template_names(self):
        if self.request.user.is_authenticated:
            template_name = "forum/forum_explore.html"
        else:
            template_name = "forum/forum_not_logged.html"
        return template_name


class ForumSectionDetailView(DetailView):
    def get_object(self):
        section_link=self.kwargs.get("section_link")
        obj=get_object_or_404(ForumSection,section_link=section_link)
        return obj
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['forum'] = True
        if self.request.user.is_authenticated:
            context['logged_in'] = True
            context['explore'] = True
        return context
    def get_template_names(self):
        if self.request.user.is_authenticated:
            template_name = "forum/forum_detail.html"
        else:
            template_name = "forum/forum_not_logged.html"
        return template_name

class PostCreateView(CreateView):
    form_class = PostCreationForm
    def get_template_names(self):
        if self.request.user.is_authenticated:
            template_name = "forum/post_create.html"
        else:
            template_name = "forum/forum_not_logged.html"
        return template_name
    success_url = "/forum/explore/"