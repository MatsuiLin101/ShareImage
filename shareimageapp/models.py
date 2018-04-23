from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=8, null=False)
    img = models.ImageField(upload_to='shareimageapp/', null=False)

    def __str__(self):
        return self.name
