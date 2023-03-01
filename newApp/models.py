from django.db import models
class Receiver(models.Model):
    receiver_name = models.CharField(max_length=50,null=False,default=None)
    description = models.TextField(blank=True)
    receiver_mail = models.EmailField(blank=True,default=None)
    
# Create your models here.
