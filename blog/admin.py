from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')  # Display these fields in the list
    search_fields = ('title', 'author')  # Enable search by title or author
    list_filter = ('published_date',)  # Filter posts by date

admin.site.register(BlogPost, BlogPostAdmin)

