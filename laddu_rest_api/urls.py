from django.urls import path, include
from rest_framework.routers import DefaultRouter
from laddu_rest_api import views

router = DefaultRouter()

router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profiles',views.UserProfileViewSet)

urlpatterns =[
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
    
]