from django.urls import path
from . import views
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'api/recommend',views.recommend_view)

urlpatterns=[
    path('',views.home_index,name="home_index"),
    path('results',views.form_results,name="home_about"),
    path('api/recommend',views.recommend_view,name="apirecommend")
    ]