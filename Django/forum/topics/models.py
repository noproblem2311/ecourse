from django.db import models

# Create your models here.
class Topic(models.Model):
    type = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = [
            'created_at',
            
        ]

    def __str__(self):
        return self.type