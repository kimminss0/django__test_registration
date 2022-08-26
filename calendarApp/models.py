from django.db import models

# Create your models here.
class Small(models.Model):
    s1 = models.TextField()
    s2 = models.TextField()

class Cal(models.Model):
    s = models.Field()
    var1 = models.TextField()
    var2 = models.TextField()
    var3 = models.TextField()