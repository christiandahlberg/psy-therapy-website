from django.urls import path
from . import views

urlpatterns = [
    # ex: /psychotherapy/
    path(r'^$', views.index),

    path('', views.index, name='index'),

    # ex: /psychotherapy/therapy/
    path('therapy/', views.therapy, name='therapy'),

    # ex: /psychotherapy/about/
    path('about/', views.about, name='about'),

    # ex: /psychotherapy/contact/
    path('getstarted/', views.getstarted, name='getstarted')
]