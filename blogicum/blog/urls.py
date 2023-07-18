from django.urls import path

from . import views

# Namespace - blog.
app_name = 'blog'

# List of blog pages' addresses.
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', views.category_posts,
         name='category_posts'),
]
