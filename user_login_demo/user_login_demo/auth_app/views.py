# auth_app/views
from django.contrib.auth import views as auth_views, login, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views
from user_login_demo.auth_app.forms import SignUpForm

UserModel = get_user_model()


class SignUpView(views.CreateView):
    template_name = 'auth/sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')

    # Signs in after successful sign up
    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class SignInView(auth_views.LoginView):
    template_name = 'auth/sign-in.html'
    success_url = reverse_lazy('index')

    # def get_success_url(self):
    #     if self.success_url:
    #         return self.success_url
    #     return self.get_redirect_url() or self.get_default_redirect_url()


class SignOutView(auth_views.LogoutView):
    template_name = 'auth/sign-out.html'


# class SignInForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField()


# def sign_in(request):
#     if request.method == 'GET':
#         form = SignInForm()
#     else:
#         form = SignInForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             # user = authenticate(request, username=username, password=password)
#             user = authenticate(request, **form.cleaned_data)
#
#             if user:
#                 login(request, user)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'auth/sign-in.html', context)

'''
!pasWo42D%23
'''