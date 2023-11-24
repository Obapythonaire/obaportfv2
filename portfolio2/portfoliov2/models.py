from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
# from ckeditor.fields import RichTextField


# For Newsletter
from django.core.mail import EmailMessage
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
import os

# Create your models here.
class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    graduation_year = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.institution
    
class Internship(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.company

class TechStack(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='images/')
    favicon = models.ImageField(upload_to='images/')
    introduction = models.TextField()
    education = models.ManyToManyField(Education)
    internship = models.ManyToManyField(Internship)
    tech_stack = models.ManyToManyField(TechStack)
    cv_link = models.FileField(upload_to='documents/')
    twitter_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    facebook_link = models.URLField(null=True, blank=True)
    whatsapp_link = models.URLField(null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)
    header_title = models.CharField(max_length=100)
    header_description = models.TextField()
    header_keywords = models.TextField()

    def __str__(self):
        return self.name

class Project(models.Model):
    CATEGORY_CHOICES = (
        ('WebDev', 'Web Dev'),
        ('AI', 'AI'),
        ('Bash Scripting', 'Bash Scripting'),
        ('Web Scraping', 'Web Scraping'),
        ('Django/Flask', 'Django/Flask'),
        ('Python', 'Python'),
        ('JS/React', 'JS/React'),
        ('Others', 'Others'),
    )

    title = models.CharField(max_length=100)
    project_image = models.ImageField(upload_to='projects/')
    poster_image = models.ImageField(upload_to='projects/poster/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    posted_date = models.DateField()
    live_project_link = models.URLField(null=True, blank=True)
    github_repo_link = models.URLField(null=True, blank=True)

    # Thought of using this for ..days ago for the posted_date
    # field but decided against it for timesince
    # def days_ago(self):
    #     time_difference = timezone.now() - self.posted_date
    #     if time_difference.days == 1:
    #         return "1 day ago"
    #     elif time_difference.days > 1:
    #         return f"{time_difference.days} days ago"
    #     else:
    #         return "Today"

    def __str__(self):
        return self.title

class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    subscription_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = [ '-subscription_date']

    def __str__(self):
        return f"{self.email} -{self.subscription_date}"
    
class BlogPost(models.Model):
    CATEGORY_CHOICES = (
        ('WebDev', 'Web Dev'),
        ('AI', 'AI'),
        ('Bash Scripting', 'Bash Scripting'),
        ('Web Scraping', 'Web Scraping'),
        ('Django/Flask', 'Django/Flask'),
        ('Python', 'Python'),
        ('JS/React', 'JS/React'),
        ('Others', 'Others'),
    )
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    post_author = models.CharField(max_length=100, default='Abdulahi')
    post_author_url = models.URLField(default='https://twitter.com/Sdecipher')
    post_title = models.CharField(
        _("Blog Title"), max_length=250,
        null=False, blank=False)
    post_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    post_content = RichTextUploadingField()
    image_thumbnail = models.ImageField(upload_to='blog_thumbnails/')
    send_post_to_subscribers = models.BooleanField(default=False)

    class Meta:
        ordering = [ '-updated', '-post_date']

    def __str__(self):
        return self.post_title
    



    def get_absolute_url(self):
        # Define the logic to generate the URL for the blog post
        # For example, if you have a URL pattern named 'blog-detail', you can use:
        # return f"/blog/{self.slug}/"
        from django.urls import reverse

        return f"{settings.BASE_URL}{reverse('blogpost', kwargs={'pk': self.pk})}"
    
# @receiver(post_save, sender=BlogPost)
# def send_email_to_subscribers(sender, instance, **kwargs):
#     if instance.send_post_to_subscribers:
#         subject = 'New Blog Post: ' + instance.post_title
#         # url = instance.get_absolute_url()
#         # short_body = instance.body[:100]
#         # message = f"{short_body} "
#         message = f"Check out our latest blog post: " '\n' + instance.post_content[:300]+"....." + '\n' +"Click below to read in detail" + '\n' + instance.get_absolute_url()

#         file_path = os.path.join(settings.MEDIA_ROOT, 'subscriberslist.txt')
#         with open(file_path, 'r') as file:
#             subscribers = [line.strip()[:-1] for line in file]

#         email = EmailMessage(subject, message, to=subscribers)
#         email.send()
#         print('Blog post sent to all subscribers')


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.name} ({self.email})"
    