from audioop import reverse
from django.shortcuts import render
from .models import Page_Dairy
from django.views.generic import TemplateView,ListView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class Main(TemplateView):
    template_name = 'main_def/index.html'
    


class Page(LoginRequiredMixin,ListView):
    model = Page_Dairy
    template_name = 'main_def/index.html'
    context_object_name = 'page'

    def get_queryset(self):
        return Page_Dairy.objects.filter(author=self.request.user)