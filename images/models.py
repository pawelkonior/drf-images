from django.contrib.auth import get_user_model
from django.db import models

from helpers.image_resizing import ThumbnailMakerService
from images.validators import validate_file_type


class Image(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image_file = models.FileField(upload_to='images/', blank=True, validators=[validate_file_type])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # print('*' * 100)
        # print(dir(self.image_file))
        # print(self.image_file.path)
        # print(self.image_file.storage)
        # tn_maker = ThumbnailMakerService()
        # tn_maker.make_thumbnails([self.image_file.name])
        super().save(*args, **kwargs)

    def __str__(self):
        return self.image_file.name
