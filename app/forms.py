from django import forms
from app.models import Article


# class CreateAticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = ("title", "status", "content", "word_count", "twitter_post")



# Kreiranje rucno
class CreateAticleForm(forms.Form):

    ARTICLE_STATUS = (
        ("draft", "draft"),
        ("in_progress", "in progress"),
        ("published", "published")
    )

    title = forms.CharField(max_length=100)
    status = forms.ChoiceField(choices=ARTICLE_STATUS)
    content = forms.CharField(widget=forms.Textarea)
    word_count = forms.IntegerField()
    twitter_post = forms.CharField(widget=forms.Textarea, required=False)