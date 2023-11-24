from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([Education, Internship, TechStack, PersonalInfo,
                      Project, BlogPost, ContactMessage, Newsletter])