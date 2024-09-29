from django.db import models

class HWID(models.Model):
    login = models.TextField()
    hwid = models.TextField()

class users(models.Model):
    login = models.TextField()
    password = models.TextField()
    id = models.IntegerField(primary_key=True)