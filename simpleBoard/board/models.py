from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# ORM(Object Relataion mapping)

class board( models.Model ):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  createDate = models.DateField()
 # writer = models.CharField(max_length=128)
  subject = models.CharField(max_length=255)
  content = models.TextField()