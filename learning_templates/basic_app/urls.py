from django.urls import path
from django.conf.urls import url
from basic_app import views

# Set up for template tagging
app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
]
