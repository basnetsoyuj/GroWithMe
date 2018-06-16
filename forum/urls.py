from django.urls import path
from .views import ForumIndexView,ForumSearchView
app_name="forum"
urlpatterns = [
    path('',ForumIndexView.as_view(),name="index"),
    path('explore/',ForumIndexView.as_view(),name="explore"),
    path('search',ForumSearchView.as_view(),name="search"),
]
