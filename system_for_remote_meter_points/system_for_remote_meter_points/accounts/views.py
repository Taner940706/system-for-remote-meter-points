from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login

from system_for_remote_meter_points.accounts.forms import UserCreateForm

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


class SignUpView(SuccessMessageMixin,views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('login user')
    success_message = "User is sign up successfully!"

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        login(request, self.object)
        return response


class UserDetailsView(views.DetailView):
    template_name = 'accounts/dashboard.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserEditView(SuccessMessageMixin, views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email', 'department', 'picture')
    success_message = "User was updated successfully"

    def get_success_url(self):
        return reverse_lazy('list meter points')


class UserDeleteView(SuccessMessageMixin, views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('login user')
    success_message = "User was deleted successfully"


class SignOutView(SuccessMessageMixin, auth_views.LogoutView):
    next_page = reverse_lazy('login user')
    success_message = "User was logged out successfully"


def handler_404(request, exception):
    return render(request, '404.html')
