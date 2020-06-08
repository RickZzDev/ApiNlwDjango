from django.db import models

# Create your models here.
class Item(models.Model):
    image = models.TextField()
    title = models.CharField(max_length=35, null=False, blank=False)

    def __str__(self):
        self.title


class Point(models.Model):
    image = models.TextField()
    name = models.CharField(max_length=85,null=False, blank=False)
    email = models.CharField(max_length=85,null=False, blank=False)
    whatsapp = models.CharField(max_length=20, null=False, blank=False)
    latitude = models.FloatField(null=False, blank=False)
    longitude = models.FloatField(null=False, blank=False)
    city = models.CharField(max_length=15, null=False, blank=False)
    uf = models.CharField(max_length=2, null=False, blank=False)
    item = models.ManyToManyField(Item)


    def __str__(self):
        return self.name

    