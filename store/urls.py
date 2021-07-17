from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/all/', views.all, name='all'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('item/<slug:slug>/<str:pk>', views.item, name='item'),
    path('basket/', views.basket, name="basket"),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='store/logout.html'), name='logout'),
]
