from django.db import models
from django.contrib.auth.models import User

class Filma(models.Model):
    izenburua = models.CharField(max_length=60)
    zuzendaria = models.CharField(max_length=60)
    urtea = models.IntegerField()
    generoa = models.CharField(max_length=2)
    sinopsia = models.CharField(max_length=700)
    bozkak = models.IntegerField()

    def __str__(self):
        return self.izenburua

class Bozkatzailea(models.Model):
    erabiltzailea = models.ForeignKey(User, on_delete=models.CASCADE)
    gogoko_filmak = models.ManyToManyField(Filma, related_name='bozkatzaileak')

    def __str__(self):
        return str(self.erabiltzailea)
