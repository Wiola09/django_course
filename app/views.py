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
    template_name = "app/create_article.html"
    model = Article
    fields = ("title", "status", "content", "twitter_post")
    success_url = reverse_lazy("home")
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    template_name = "app/update_article.html"
    model = Article
    fields = ("title", "status", "content", "twitter_post")
    success_url = reverse_lazy("home")
    context_object_name = "article"


class ArticleDeleteView(DeleteView):
    template_name = "app/delete_article.html"
    model = Article
    success_url = reverse_lazy("home")
    context_object_name = "article"