from django.db import models

# Create your models here.
# CharField is used for short strings and specifies a maximum length.
# TextField is used for longer form text as it don't have a maximum length limit.
# FilePathField holds a string that must point to a file path name.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
