from django.urls import path
from .views import *

app_name = "music"
urlpatterns = [
    path('', album_list_read_create),
    path('<int:album_id>', album_detail_update_delete),
    path('<int:album_id>/track', track_read_create),
    path('track/<int:track_id>', track_detail_update_delete),
]