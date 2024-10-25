from django.shortcuts import render, redirect


from django.http import HttpResponse
from app.models import Article
from app.forms import CreateAticleForm

# Create your views here.

def home(request):
    articles = Article.objects.all()
    return render(request, "app/home.html", {"articles":articles})
    return HttpResponse("Zdravo Svete Lepi")


def kreiraj_tekst(request):
    if request.method == "POST":
        # podaci su predloženi
        form = CreateAticleForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            novi_tekst = Article(
                title=form_data["title"],
                status=form_data["status"],
                content=form_data["content"],
                word_count=form_data["word_count"],
                twitter_post=form_data["twitter_post"]
            )
            novi_tekst.save()
            return redirect("home")
    else:
        form = CreateAticleForm(    
        )
    return render(request, "app/kreiraj_tekst.html", {"form":form})