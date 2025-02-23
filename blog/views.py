from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from .models import BlogPost

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

class BlogCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/blog_forms.html'
    fields = ["title", "author", "content", "published_date"]
    success_url = reverse_lazy('blog_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Blog post successfully submitted!")
        return response