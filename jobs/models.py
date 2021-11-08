from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200, blank=True)
    summary = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title