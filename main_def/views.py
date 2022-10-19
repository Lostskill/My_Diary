from .forms import *
from .models import Page_Dairy
from django.views.generic import TemplateView,ListView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout 
from django.shortcuts import redirect

class Login(LoginView):
    form_class = LoginUser
    template_name = 'main_def/login.html'

    def get_success_url(self) :
        return reverse_lazy('pages')

class Page(ListView):
    model = Page_Dairy
    template_name = 'main_def/index.html'
    context_object_name = 'page'

    
    def get_queryset(self):
        return Page_Dairy.objects.filter(author=self.request.user)

def logout_user(request):
    logout(request)
    return redirect('login')