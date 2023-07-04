from django.contrib import admin
from .models import Blog, Comment



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    search_fields = ['title']  
    ordering = ['-created_at']  
    list_per_page = 5


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['content']  
    ordering = ['-created_at']  

