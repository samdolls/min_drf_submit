from rest_framework import serializers
from .models import *

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'

class AlbumImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url = True, required = False)

    class Meta:
        model = AlbumImage
        fields = ['image']

class AlbumSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only = True)

    tracks = serializers.SerializerMethodField(read_only = True)
    tag = serializers.SerializerMethodField(read_only = True)
    images = serializers.SerializerMethodField()
    
    def get_tracks(self, instance):
        serializers = TrackSerializer(instance.tracks, many = True)
        return serializers.data
    
    def get_tag(self, instance):
        tags = instance.tag.all()
        return [tag.name for tag in tags]
    
    def get_images(self, instance):
        image = instance.image.all()
        return AlbumImageSerializer(image, many = True, context = self.context).data

    class Meta:
        model = Album
        fields = '__all__'

    def create(self, validated_data):
        instance = Album.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            AlbumImage.objects.create(album = instance, image = image_data)
        return instance
    
    def update(self, instance, validated_data):
        instance.image.all().delete()
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            AlbumImage.objects.create(album = instance, image = image_data)
        return instance

class TrackSerializer(serializers.ModelSerializer):
    album = serializers.CharField(read_only = True)

    album = serializers.SerializerMethodField()

    def get_album(self, instance):
        return instance.album.title
    
    class Meta:
        model = Track
        fields = ('album', 'number', 'title')