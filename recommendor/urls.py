from django.urls import path
from . import views
urlpatterns=[
    path('',views.home_index,name="home_index"),
    path('results',views.form_results,name="home_about"),
    ]