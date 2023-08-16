from django.db import models

class Contacts(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=50)
    message = models.TextField()
    date = models.DateField()