from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NoteCategory(models.Model):
    name = models.CharField(max_length=300)

class Note(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    category = models.ForeignKey(NoteCategory,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
