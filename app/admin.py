from django.contrib import admin
from app.models import UserProfile, Article

# Register your models here.

# Da bise moglo videti na admin stranici
admin.site.register(UserProfile)  
admin.site.register(Article)