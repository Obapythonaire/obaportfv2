from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contactus, name='contact'),
    # path('search-results/', views.home, name='search_results_view'),
    path('blog/<str:pk>', views.blog_single_post, name='blogpost'),
    path('projects', views.projects, name='projects'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('upvote-comment/<int:comment_id>/', views.upvote_comment, name='upvote_comment'),
    path('downvote-comment/<int:comment_id>/', views.downvote_comment, name='downvote_comment'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)