from django.db import models

# Create your models here.


class Dataset(models.Model):
    id = models.AutoField(primary_key=True)
    p1 = models.BooleanField()
    p2 = models.BooleanField()
    p3 = models.BooleanField()
    p4 = models.BooleanField()
    p5 = models.BooleanField()
    p6 = models.BooleanField()
    p7 = models.BooleanField()
    p8 = models.BooleanField()
    p9 = models.BooleanField()
    p10 = models.BooleanField()
    p11 = models.BooleanField()
    lvl = models.PositiveSmallIntegerField(default=0)
    percent1 = models.FloatField()
    percent2 = models.FloatField()
    percent3 = models.FloatField()
