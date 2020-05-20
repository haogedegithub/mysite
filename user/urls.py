from django.urls import path,re_path
from . import views

urlpatterns = [
    path('logout/', views.logout, name='logout'),
    path('user_info', views.user_info, name='user_info'),
    path('regiest/', views.register, name='register'),
    path('login_for_modal/', views.login_for_medal, name='login_for_medal'),
    path('login/', views.login, name='login'),
    path('change_nickname/',views.change_nickname,name = 'change_nickname'),
    path('bind_email/',views.bind_email,name = 'bind_email'),
    path('send_verification_code/',views.send_verification_code,name = 'send_verification_code')
]