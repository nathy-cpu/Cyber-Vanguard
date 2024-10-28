from django.db import models

# Create your models here.


class ContactMessage(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name
