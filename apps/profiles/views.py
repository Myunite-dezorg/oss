from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Profile

class UserProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'user_profile_list.html'
    context_object_name = 'profiles'

class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'user_profile_detail.html'
    context_object_name = 'profile'
    
    def get_object(self, queryset=None):
        return get_object_or_404(Profile, unique_id=self.kwargs.get('unique_id'))
    

class UserProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    template_name = 'user_profile_form.html'
    fields = ['position', 'birth_date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'user_profile_form.html'
    fields = ['position', 'birth_date']

class UserProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'user_profile_confirm_delete.html'
    success_url = reverse_lazy('profiles')