from django.db import models

# Create your models here.

class Major(models.Model):
    name = models.CharField(max_length=512)
    def __unicode__(self):
        return self.name