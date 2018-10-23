from django.db import models


class AbstractAbout(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')

    class Meta:
        abstract = True


class About(AbstractAbout):
    pass
