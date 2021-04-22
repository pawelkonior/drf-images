from rest_framework.serializers import ModelSerializer

from images.models import Image


class ImageSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'image_file', 'updated_at', 'created_at')
        model = Image
