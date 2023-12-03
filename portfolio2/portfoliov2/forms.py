from django import forms
from .models import ContactMessage, Newsletter, Comment
from ckeditor.widgets import CKEditorWidget

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'title', 'message']

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'text']
        widgets = {
            'text': CKEditorWidget(config_name='limited_config'),
        }
