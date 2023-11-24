from .models import BlogPost, Newsletter
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import EmailMessage
from django.conf import settings  # Import Django settings


@receiver(post_save, sender=BlogPost)
def send_email_to_subscribers(sender, instance, created, **kwargs):
    if (created  or not created) and instance.send_post_to_subscribers: #created or not created to check if just created or updated
        subscribers = Newsletter.objects.all()  # Retrieve all subscribers from the Newsletter model
        if subscribers:
            subject = instance.post_title
            message = f"{instance.post_content[:300]}.....\nClick below to read in detail {instance.get_absolute_url()}"
            email_addresses = [subscriber.email for subscriber in subscribers]
            
            # Create an EmailMessage using SendinBlue SMTP settings from your Django configuration
            email = EmailMessage(
                subject,
                message,
                from_email=settings.EMAIL_HOST_USER,  # Use the SendinBlue username as the sender
                to=email_addresses,
                reply_to=[settings.EMAIL_HOST_USER],  # Set the reply-to email address
                connection=None,  # Use the default email backend configuration from Django settings
            )
            
            email.send()
            print('Blog post sent to all subscribers')

