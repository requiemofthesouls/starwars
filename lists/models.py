from django.db import models

# Create your models here.


class Type(models.Model):
    type = models.CharField(max_length=128, unique=True, primary_key=True)

    def __str__(self):
        return self.type


class Series(models.Model):
    series = models.CharField(max_length=128, unique=True, primary_key=True)

    class Meta:
        verbose_name_plural = 'Series'

    def __str__(self):
        return self.series


class Side(models.Model):
    side = models.CharField(max_length=128, unique=True, primary_key=True)

    def __str__(self):
        return self.side


class Ship(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    lenght = models.IntegerField()
    name = models.CharField(max_length=128)
    side = models.ForeignKey(Side, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



