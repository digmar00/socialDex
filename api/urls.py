from django.urls import path
from .views import posts, last_day_posts, last_hour_posts, string_appearances, api

urlpatterns = [
    path('', api, name='api'),
    path('posts/', posts, name='posts'),
    path('last_day_posts/', last_day_posts, name='last_day_posts'),
    path('last_hour_posts/', last_hour_posts, name='last_hour_posts'),
    path('string_appearances/', string_appearances, name='string_appearances'),
]
