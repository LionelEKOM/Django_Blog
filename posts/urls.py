from django.urls import path
from .views import BlogHome, BlogPostCreateView, BlogPostDeleteView, BlogPostDetailView, BlogPostUpdateView

app_name = 'posts'
urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('create/', BlogPostCreateView.as_view(), name='create'),
    path('<str:slug>/', BlogPostDetailView.as_view(), name='detail'),
    path('edit/<str:slug>/', BlogPostUpdateView.as_view(), name='edit'),
    path('delete/<str:slug>/', BlogPostDeleteView.as_view(), name='delete'),
]