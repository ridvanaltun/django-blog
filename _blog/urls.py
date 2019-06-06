from django.conf.urls import url
from _blog.views import IndexView, AboutView, BlogDetailView, ContactView

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

app_name = '_blog'

urlpatterns = [
    url(r'^$', IndexView, name='homepage'),
    url(r'^about/', AboutView, name='about'),

    #  e.g. http://localhost:8000/blog/1 
    url(r'^blog/(?P<id>\d+)/$', BlogDetailView, name='blog_detail'),

    url(r'^contact/', ContactView, name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)