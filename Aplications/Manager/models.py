from django.db import models

# Create your models here.

class Example(models.Model):
    code = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return "{0}".format(self.name)