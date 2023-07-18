from django.contrib import admin
from django.urls import include, path

# List of pages' addresses.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('pages/', include('pages.urls', namespace='pages')),
]
