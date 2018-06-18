from django.db import models
from django.contrib.auth.models import User
class ForumSection(models.Model):
    name=models.CharField(max_length=75)
    admin=models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    picture_link=models.CharField(max_length=250)
    section_link=models.CharField(max_length=250)

class Post(models.Model):
    name=models.CharField(max_length=250)
    section=models.ForeignKey(ForumSection,on_delete=models.CASCADE)
    content=models.TextField()