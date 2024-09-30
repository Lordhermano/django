from django.db import models

# Create your models here.
class Record(models.Model):

    creation_data = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length=100)