from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/comment/create/', views.comment_create, name='comment_create'),
    path('<int:post_id>/like', views.like, name='like'), 
    path('<int:post_id>/like-async/', views.like_async, name='like_async'),

]