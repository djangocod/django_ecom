from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

app_name = 'users'

urlpatterns = [
    path('register/',views.account_register,name='account_register'),
    path('activate-account/<uidb64>/<token>/',views.account_activte,name='activate'),
    path('login/',views.account_login,name='account_login'),
    path('logout/',views.account_logout,name='account_logout'),

    # reset password
    path('password_reset/',auth_view.PasswordResetView.as_view(
                                                                template_name='users/reset/password_reset.html',
                                                                email_template_name='users/reset/email_reset.html',
                                                                success_url='/account/password_reset_done'),
                                                                name='password_reset'),
    path('password_reset_done/',auth_view.PasswordResetDoneView.as_view(
                                                                        template_name='users/reset/password_reset_done.html'),
                                                                        name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(
                                                                    template_name='users/reset/password_reset_confirm.html',
                                                                    success_url='/account/password_reset_complete'),name='password_reset_confirm'),
    path('password_reset_complete/',auth_view.PasswordResetCompleteView.as_view(template_name='users/reset/password_reset_complete.html'),
                                                                                name='password_reset_complete'),                                                                                                                          
    path('user_contact/', views.users_contact, name='users_contact'),
]
