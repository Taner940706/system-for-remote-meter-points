# urlpatterns = (
# 	path('login/', SignInView.as_view(), name='login user'),
#     path('register/', SignUpView.as_view(), name='register user'),
#     path('logout/', SignOutView.as_view(), name='logout user'),
#     path('profile/<int:pk>/', include([
#         path('', UserDetailsView.as_view(), name='details user'),
#         path('edit/', UserEditView.as_view(), name='edit user'),
#         path('delete/', UserDeleteView.as_view(), name='delete user'),
#     ])),
# )
from django.contrib.auth import logout
from django.urls import include, path

from system_for_remote_meter_points.accounts.views import login_user, register_user, details_user, edit_user, \
    delete_user

urlpatterns = (
    path('login/', login_user, name='login user'),
    path('register/', register_user, name='register user'),
    path('logout/', logout, name='logout user'),
    path('profile/<int:pk>/', include([
        path('', details_user, name='details user'),
        path('edit/', edit_user, name='edit user'),
        path('delete/', delete_user, name='delete user'),
    ])),
)