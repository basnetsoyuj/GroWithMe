from django.urls import path
from . import views
app_name="minefield"
urlpatterns = [
    path('',views.index,name='index'),
]
