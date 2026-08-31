

from django.db import models

class Drinks(models.Model):
    name = models.CharField(max_length = 250)
    description = models.CharField(max_length = 650)


    def __str__(self):
        return self.name 