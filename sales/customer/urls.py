from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('register/success/', views.register_view, name='register_success'),
    path('login/success/', views.login_view, name='login_success'),
    path('logout/', views.login_view, name='logout'),
    path('logout/success/', views.login_view, name='logout_success')
]
