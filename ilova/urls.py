from django.urls import path
from .views import HomeViews, AboutViews

urlpatterns=[
    path('',HomeViews.as_view(), name='home'),
    path('about/',AboutViews.as_view(), name='about')
]