from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from posts.models import BlogPost
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

class BlogHome(ListView):
    model = BlogPost
    context_object_name = 'posts'
    # template_name='posts/blogpostList.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published='True')
    
@method_decorator(login_required, name='dispatch')
class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ['title', 'content']
    

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_edit.html"
    fields = ['title', 'content', 'published']
    

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "posts/blogpost_detail.html"
    context_object_name = 'post'
    

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = "posts/blogpost_confirm_delete.html"
    success_url = reverse_lazy("posts:home")
    context_object_name = 'post'




