from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'is_approved')
    actions = ['approve_posts']

    def approve_posts(self, request, queryset):
        queryset.update(is_approved=True)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email')
    ordering = ('date_joined',)