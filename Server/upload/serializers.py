from upload.models import Uploader
from rest_framework import serializers
from .utils import createUniqueUrlFile

class FileUploadedSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'title',
            'file_upload',
        ]


    def create(self, validated_data):

        uploaded = Uploader.objects.create(
            title=validated_data['title'],
            file_upload=self.context['request'].FILES,
            sender=self.context['request'].user
        )

        uploaded.file_code = createUniqueUrlFile(uploaded.pk, uploaded.title)
        uploaded.save()