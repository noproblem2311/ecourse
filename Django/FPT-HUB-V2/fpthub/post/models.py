from django.db import models
from django.utils.text import Truncator
from django.contrib.auth.models import User
from thread.models import Thread


class Post(models.Model):
    """ Model to represent the post in a thread """
    content = models.TextField()
# gán về cái thread đã tạo 
    thread = models.ForeignKey(
        Thread,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    counter_seed=models.CharField(max_length=200, null=True) 
    counter_flag = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
   
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ['created_at']

    def __str__(self):
        truncated_content = Truncator(self.content)
        return truncated_content.chars(30) 