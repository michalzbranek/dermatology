from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length = 20)
    phone = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)
    time = models.DateTimeField

    def __str__(self):
        return  ' '.join([
            self.name,
            self.phone,
            self.email,
            self.time
        ])