from django.db import models

class Note(models.Model):
    name = models.CharField(max_length = 20, blank = False, null = False)
    description = models.TextField(max_length= 300, blank=True, null= True)
    def __str__(self):
        return self.name
    
# Create your models here.
