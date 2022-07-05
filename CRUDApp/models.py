from django.utils.timezone import now
from django.db import models

# Create your models here.

class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    note_title = models.CharField(max_length=255)
    note_desc = models.TextField()
    date_time = models.DateTimeField(default=now)
    user_email = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.note_title

class User_Data(models.Model):
    user_email = models.EmailField(primary_key=True)
    user_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name