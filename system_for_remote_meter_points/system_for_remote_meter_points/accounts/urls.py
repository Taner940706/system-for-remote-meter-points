from django.urls import include, path

from system_for_remote_meter_points.accounts.views import SignInView, SignUpView, SignOutView, UserDetailsView, \
    UserEditView, UserDeleteView

urlpatterns = (
    path('', SignInView.as_view(redirect_authenticated_user=True), name='login user'),
    path('register/', SignUpView.as_view(), name='register user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
)
