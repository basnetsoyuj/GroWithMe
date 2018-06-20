from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
class ForumSection(models.Model):
    name=models.CharField(max_length=75)
    admin=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    picture_link=models.CharField(max_length=250,default="default_section.png")
    section_link = models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name

class Post(models.Model):
    name=models.CharField(max_length=250)
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    section=models.ForeignKey(ForumSection,on_delete=models.CASCADE)
    content=models.TextField()
    def __str(self):
        return self.name

def forum_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.section_link:
        instance.section_link=unique_slug_generator(instance)
pre_save.connect(forum_pre_save_receiver,sender=ForumSection)