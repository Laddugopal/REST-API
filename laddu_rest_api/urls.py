from django.urls import path
from laddu_rest_api import views

urlpatterns =[
    path('hello-view/', views.HelloApiView.as_view()),
    
]