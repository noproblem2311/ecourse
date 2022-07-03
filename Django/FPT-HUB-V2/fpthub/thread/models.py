from django.db import models

# Create your models here.
class Thread(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type