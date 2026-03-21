from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, ProfileEditForm, UserEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views import View
from .models import Profile
from news_app.models import News, Comment
from django.contrib.auth.models import User


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('news:home')
            else:
                return render(request, 'registration/login.html', {
                    'form': form,
                    'error': "Username yoki parol noto'g'ri!"
                })
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if user.is_staff or user.is_superuser:
        post_count = News.objects.filter(author=user).count()
    else:
        post_count = Comment.objects.filter(author=user).count()

    context = {
        "user": user,
        "profile": profile,
        "post_count": post_count,
    }
    return render(request, "pages/user_profile.html", context)


class SignUpView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:register_done')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EditProfileView(LoginRequiredMixin, View):
    template_name = 'accounts/edit_profile.html'

    def get_profile(self, user):
        profile, _ = Profile.objects.get_or_create(user=user)
        return profile

    def get(self, request, *args, **kwargs):
        profile = self.get_profile(request.user)
        return render(request, self.template_name, {
            'user_form': UserEditForm(instance=request.user),
            'profile_form': ProfileEditForm(instance=profile),
        })

    def post(self, request, *args, **kwargs):
        profile = self.get_profile(request.user)
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=profile,
            data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('accounts:user_profile')

        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form,
        })


@staff_member_required
def admin_page(request):
    context = {
        'users_count': User.objects.count(),
        'news_count': News.objects.count(),
        'last_users': User.objects.order_by('-date_joined')[:6],
        'last_news': News.objects.select_related('author').order_by('-created_at')[:6],
        'admin_users': User.objects.filter(is_staff=True),
    }
    return render(request, 'accounts/admin_page.html', context)