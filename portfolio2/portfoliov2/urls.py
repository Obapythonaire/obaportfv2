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

]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)