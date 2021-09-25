from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('signup', views.signup_view, name='signup'),
    path('create', views.CreatePostView.as_view(), name='newpost'),
    path('view/<int:pk>/', views.PostDetailView.as_view(), name='viewpost'),


]
