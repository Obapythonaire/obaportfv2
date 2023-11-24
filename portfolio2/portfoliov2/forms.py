from django import forms
from .models import ContactMessage, Newsletter

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'title', 'message']

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email',]
