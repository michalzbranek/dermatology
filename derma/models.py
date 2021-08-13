from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField(max_length=20)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('reservation-detail', args=[str(self.id)])