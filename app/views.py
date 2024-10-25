from django.shortcuts import render, redirect
from django.urls import reverse_lazy


from django.http import HttpResponse
from app.models import Article
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

# Create your views here.

class ArticleListView(ListView):
    template_name = "app/home.html"
    model = Article
    context_object_name = "articles"

class CreateArticleView(CreateView):
    template_name = "app/kreiraj_tekst.html"
    model = Article
    fields = ("title", "status", "content", "word_count", "twitter_post")
    success_url = reverse_lazy("home")


class ArticleUpdateView(UpdateView):
    template_name = "app/izmeni_tekst.html"
    model = Article
    fields = ("title", "status", "content", "word_count", "twitter_post")
    success_url = reverse_lazy("home")
    context_object_name = "article"


class ArticleDeleteView(DeleteView):
    template_name = "app/obrisi_tekst.html"
    model = Article
    success_url = reverse_lazy("home")
    context_object_name = "article"