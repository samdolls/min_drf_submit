from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "music"
urlpatterns = [
    path('', album_list_read_create),
    path('<int:album_id>', album_detail_update_delete),
    path('<int:album_id>/tracks', track_read_create),
    path('tracks/<int:track_id>', track_detail_update_delete),
    path('tags/<str:tag_name>', find_tag),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)