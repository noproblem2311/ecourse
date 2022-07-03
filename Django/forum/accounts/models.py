from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

# from .views import ProfileDetailView
# method_seeds = 0
# method_flags= 0
# method_postlist=[]
# method_bookmarklist
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email= models.EmailField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    seeds=models.IntegerField( null=True) 
    flags= models.IntegerField( null=True)
    postList = models.IntegerField( null=True)
    bookmarklist= models.CharField(max_length=200, default=True, null=True)
    def __str__(self):
        return self.name
    # def counterlike():
    #     for i in Post:
    #      if Post.creator.id ==User.id:
    #         method_seeds = method_seeds + Post.counter_seed 
    #         method_flags = method_flags + Post.counter_flag
    #         method_postlist= method_postlist + Post.id
# class CounterPost(models.Model):
#     title = models.CharField(max_length=200)
#     created_by = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True,default=True)
#     seeds= models.IntegerField(null=True)
    
#     def __str__(self):
#         return self.title
# class seeds(models.Model):
#     Profile= models.ForeignKey(Profile, related_name='profile',on_delete=models.CASCADE)
#     CounterPost = models.ForeignKey(CounterPost,related_name='counterpost', on_delete=models.CASCADE)


        