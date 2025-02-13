from django.contrib.auth.views import LogoutView
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView, UserLoginView, UpdateCustomUser, email_verification, AllCustomUserListView, block_user, \
    CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, \
    CustomPasswordResetCompleteView

app_name = "users"

urlpatterns = [
    path("login/", UserLoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="clients:home"), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("email-verification/<str:token>/", email_verification, name="email-confirm"),
    path("update-user/<int:pk>/", UpdateCustomUser.as_view(), name="update-user"),
    path("all-customusers/", AllCustomUserListView.as_view(), name="all-customusers"),
    path("block-user/<int:pk>/", block_user, name="block_user"),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset-complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
        ]
