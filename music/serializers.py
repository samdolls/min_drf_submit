from rest_framework import serializers
from .models import *

class AlbumSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only = True)

    tracks = serializers.SerializerMethodField(read_only = True)

    def get_tracks(self, instance):
        serializers = TrackSerializer(instance.tracks, many = True)
        return serializers.data

    class Meta:
        model = Album
        fields = '__all__'

class TrackSerializer(serializers.ModelSerializer):
    album = serializers.CharField(read_only = True)

    album = serializers.SerializerMethodField()

    def get_album(self, instance):
        return instance.album.title
    
    class Meta:
        model = Track
        fields = ('album', 'number', 'title')