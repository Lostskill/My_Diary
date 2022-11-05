from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from .models import Page_Dairy
from django.views.generic import ListView , CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy 
from django.contrib.auth import logout 
from django.shortcuts import redirect ,render
from django.contrib.auth.mixins import LoginRequiredMixin

class Login(LoginView):
    form_class = LoginUser
    template_name = 'main_def/login.html'

    def get_success_url(self) :
        return reverse_lazy('pages')

class Page(LoginRequiredMixin ,ListView):
    model = Page_Dairy
    template_name = 'main_def/index.html'
    context_object_name = 'page'

    
    def get_queryset(self):
        return Page_Dairy.objects.filter(author=self.request.user)

def logout_user(request):
    logout(request)
    return redirect('login')

#class CreatePage(LoginRequiredMixin,CreateView):
#    form_class = CreatePage
#    template_name = 'main_def/create_page.html'
#    success_url = reverse_lazy('pages')

def page_new(request):
    form = CreatePage()
    if request.method == "POST" and request.user.is_authenticated :
        form = CreatePage(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.author = request.user
            page.save()
            return HttpResponseRedirect(reverse('pages'))
    else:
        form = CreatePage()

    return render(request,'main_def/create_page.html', {'form':form})