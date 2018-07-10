from django.urls import path
from .views import UserProfile,register
from django.contrib.auth.views import login,logout
app_name="accounts"
urlpatterns = [
    path('login/', login,{'template_name':'accounts/login.html','extra_context':{'login':True}},name="login"),
    path('register/',register,name="register"),
    path('logout/', logout,{'next_page':'home:index'},name="logout"),
    path('profile/<username>', UserProfile.as_view(),name="profile"),
]
