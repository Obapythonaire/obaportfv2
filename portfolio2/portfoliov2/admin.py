from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # Customize these fields
    list_filter = ("name", "email",)
    search_fields = ['name', 'text']
    # prepopulated_fields = {'slug': ('title',)}

admin.site.register([Education, WorkExperience, TechStack, PersonalInfo,
                      Project, BlogPost, ContactMessage, Newsletter
                      ])
# admin.site.register(CommentAdmin, Comment)