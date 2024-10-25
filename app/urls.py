from django.urls import path
from app.views import CreateArticleView, ArticleListView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path("", ArticleListView.as_view(), name="home"),
    path("kreiraj/", CreateArticleView.as_view(), name="kreiraj_tekst"),
    path("<int:pk>/izmeni/", ArticleUpdateView.as_view(), name="izmeni_tekst"),
    path("<int:pk>/obrisi/", ArticleDeleteView.as_view(), name="obrisi_tekst"),
]