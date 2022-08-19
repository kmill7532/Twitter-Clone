from inspect import ClosureVars
from django.db import models
from cloudinary.models import CloudinaryField
class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'abcs', blank=False, null=False, max_length=35, db_index=True, default='Anonymous')

    image = CloudinaryField('Upload', blank=True, db_index=True)

    likes = models.PositiveIntegerField('Likes', default=0, db_index=True, blank = True)

    body = models.CharField('Body', blank=True, null=True, max_length=140, db_index=True)

    created_at = models.DateTimeField('Created DateTime', blank=True, auto_now_add=True)