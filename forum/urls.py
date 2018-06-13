from django.urls import path
from .views import ForumIndexView
app_name="forum"
urlpatterns = [
    path('',ForumIndexView.as_view(),name="index"),
]
