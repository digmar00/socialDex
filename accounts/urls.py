from django.urls import path
from .views import login, sign_up, main_page, user_detail
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', sign_up, name='sign_up'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('user/<int:pk>/', user_detail, name='user_detail'),
    path('', main_page, name='main_page'),
]
