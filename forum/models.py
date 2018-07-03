from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.urls import reverse
class ForumSection(models.Model):
    name=models.CharField(max_length=75)
    section_desc=models.TextField(blank=True,null=True)
    admin=models.ForeignKey(User,on_delete=models.CASCADE,default=1,related_name="ForumSection_admin")
    picture_link=models.CharField(max_length=250,default="default_section.png")
    section_link = models.SlugField(null=True, blank=True)
    subscribers=models.ManyToManyField(User,related_name="ForumSection_subscribers")
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("forum:sections",kwargs={'section_link':self.section_link})
    @property
    def title(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=250)
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    section=models.ForeignKey(ForumSection,on_delete=models.CASCADE)
    content=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering=['-updated_time','-created_time']

def forum_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.section_link:
        instance.section_link=unique_slug_generator(instance)
pre_save.connect(forum_pre_save_receiver,sender=ForumSection)