from django.contrib import admin
from .models import Blog,Comment



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    search_fields = ['title']  # Specify the fields to be searched
    ordering = ['-created_at']  # Specify the default sorting order
    list_per_page = 5



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['content']  # Specify the fields to be searched
    ordering = ['-created_at']  # Specify the default sorting order
    

