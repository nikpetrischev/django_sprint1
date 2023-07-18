from django.urls import path

from . import views

# Namespace - pages.
app_name = 'pages'

# List of info-pages' addresses.
urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
]
