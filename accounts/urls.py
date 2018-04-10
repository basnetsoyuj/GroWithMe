from django.urls import path
from . import views
from django.contrib.auth.views import login,logout
app_name="accounts"
urlpatterns = [
    path('login/', login,{'template_name':'accounts/login.html','extra_context':{'login':True}},name="login"),
    path('register/', views.register,name="register"),
    path('logout/', logout,{'next_page':'home:index'},name="logout"),
]
