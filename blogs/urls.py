from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    BlogListView,
    BlogDetailView,
    PostCreateView,
    VideoView,
)

app_name = 'blog'
urlpatterns = [
    path('blog/', BlogListView.as_view(), name='list'),
    path('blog/add/', PostCreateView.as_view(), name='create'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('video/', VideoView.as_view(), name='video'),
]
# Раздача медиа-файлов в режиме отладки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
