from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
# from django.contrib.auth import get_user_model
# Create your models here.

# User = get_user_model()
class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publie")
    content = models.TextField(blank=True, verbose_name="Contenu")
    thumbnail = models.ImageField(blank=True, upload_to="blogImage")
    
    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    @property
    def author_or_default(self):
        if self.author:
            return self.author.username
        return "Auteur non defini"
    
    def get_absolute_url(self):
        return reverse('posts:home',)