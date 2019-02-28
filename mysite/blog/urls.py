from django.urls import path,include
from blog import views

urlpatterns = [
    path('', views.post_list,name='post_list'),

]
