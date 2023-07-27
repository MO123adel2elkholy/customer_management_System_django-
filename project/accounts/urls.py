from django.urls import path
from .views import home, customer, profile, dashboard, \
    createorder , update_order, delete_order , log , \
    register , login_backend ,logout_backend, user , account_setting
from django.contrib.auth import views as auth_views







urlpatterns=[
path('customer/<int:pk>' , customer, name='customer' ),
path('products/', profile, name='products'),
path('', dashboard , name='dashboard'),
path('create_order/<int:pk>', createorder , name='create_order'),
path('update_order/<int:pk>', update_order , name='update_order'),
path('delete_order/<int:pk>', delete_order , name='delete_order'),
path('logout/', logout_backend, name='logout'),
path('login/', log, name='login'),
path('login_backend/', login_backend, name='login_backend'),
path('register/', register, name='register'),
path('user/' ,user , name='user'),
path('account_setting/' ,account_setting , name='account_setting'),
path('rest_password/', auth_views.PasswordResetView.as_view() , name='rest_password'),
path('rest_password_sent/', auth_views.PasswordResetDoneView.as_view() , name='passwor_drest_done' ),
path('rest/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view() , name='password_reset_confirm' ),
path('rest_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_rest_complete' ),
]