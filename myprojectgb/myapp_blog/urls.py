from django.urls import path
from . import views

urlpatterns = [
    path('author_read/', views.author_read, name='author_read'),
    path('post_read/', views.post_read, name='posts'),
    path('post_by_authors/', views.post_by_authors, name='post_by_authors'),
    path('author/<int:author_id>/', views.author_posts, name='author_posts'),
    path('post/<int:post_id>/', views.post_full, name='post_full'),
    path('post/all/', views.view_all_posts, name='view_all_posts'),
    # path('post/a/<int:id_post>/', views.view_post, name='view_post'),
    path('post/comment/<int:post_id>/', views.post_comm, name='post_comm'),
    path('create-author/', views.create_author, name='create_author'),
    path('create_post/', views.create_post, name='create_post'),

]
