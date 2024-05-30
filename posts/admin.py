from django.contrib import admin

from posts.models import BlogPost


# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_on", "last_updated")
    # Permet d'editer le champs published durant son affichage
    list_editable = ("published",)
    
admin.site.register(BlogPost, BlogPostAdmin)