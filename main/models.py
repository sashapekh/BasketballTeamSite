from django.db import models
from django.utils import timezone


# Create your models here.

class ImagesLogo(models.Model):
    img_name = models.CharField(max_length=100, default='first')
    img_src = models.CharField(max_length=300)
    description = models.TextField(default='Chicago bulls')
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.img_name + ' logo'
