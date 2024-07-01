from django.db import models
class service(models.Model):
    service_icon=models.CharField(max_length=50)
    service_titel=models.CharField(max_length=50)
    service_dec=models.TextField()

# Create your models here.
