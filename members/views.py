from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from members.forms import SignUpForm, EditProfileForm
from django.views.generic import DetailView
from theblog.models import Profile



# Create your views here.

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context['page_user'] = page_user
        return context


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

    # def password_success(request):
    #     return render(request, 'registration/password_change_form.html')

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'  # Updated path
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'  # Updated path
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


