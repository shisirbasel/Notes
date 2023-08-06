from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=100,verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    createdate = models.DateField(auto_now_add= True, verbose_name='Created On')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title