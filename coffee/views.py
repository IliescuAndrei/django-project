from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.generic import (
    TemplateView, ListView, DetailView,
    CreateView, UpdateView, DeleteView
)

from coffee.forms import CommentForm
from coffee.models import Cafea, User, Comment
# Create your views here.



def cafea_index(request):
    cafele = Cafea.objects.all()
    context = {
        'cafele': cafele
    }
    return render(request, 'cafea_index.html', context)

def cafea_detail(request, pk):
    cafea = Cafea.objects.get( id = pk )
    context = {
        'cafea': cafea
    }
    return render(request, 'cafea_detail.html', context)


class LoginView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self):
        form = AuthenticationForm()
        return {'form': form}

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'],
                                password=data['password'])
            login(request, user)
            return redirect(reverse_lazy('cafea_index'))
        else:
            return render(request, "login.html", {"form": form})


class RegisterView(CreateView):
    template_name= 'register.html'
    form_class = UserCreationForm
    model = User

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create_user(username=data['username'],
                                        password=data['password1'])
        return redirect('cafea_index')

class LogoutView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse_lazy('cafea_index'))



# @login_required
# def comment_create(request, pk):
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             book = Book.objects.get(id=pk)
#             Comment.objects.create(
#                 created_by=request.user,
#                 book=book,
#                 **form.cleaned_data
#             )
#             return redirect(reverse_lazy("book_detail", kwargs={"pk": pk}))

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']

    def form_valid(self, form):
        cafea = Cafea.objects.get(id=self.kwargs['pk'])
        Comment.objects.create(
            created_by=self.request.user,
            cafea=cafea,
            **form.cleaned_data
        )
        return redirect(reverse_lazy("cafea_detail", kwargs={"pk": self.kwargs['pk']}))
