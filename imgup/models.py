from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.forms import ModelForm
from PIL import Image
from time import strftime


@python_2_unicode_compatible
class Image(models.Model):

    def path(instance, filename):
        ext = filename.split('.')[-1]
        return '{}.{}'.format(strftime('%d%m%y%H%M%S'), ext)

    image = models.ImageField(upload_to=path)
    comment = models.CharField(max_length=200)


class UploadForm(ModelForm):

    class Meta:
        model = Image
        fields = ('image', 'comment')
