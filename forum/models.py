from django.db import models
from django.contrib.auth.models import User
class ForumSection(models.Model):
    name=models.CharField(max_length=75)
    admin=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    picture_link=models.CharField(max_length=250,default="/forum/images/default_section.png")
    section_link=models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Post(models.Model):
    name=models.CharField(max_length=250)
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    section=models.ForeignKey(ForumSection,on_delete=models.CASCADE)
    content=models.TextField()
    def __str(self):
        return self.name