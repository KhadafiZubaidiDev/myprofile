from django.db import models

# Create your models here.
class Pelatihan(models.Model):
  nama = models.CharField(max_length=255)
  deskripsi = models.CharField(max_length=255)
  penyelenggara = models.CharField(max_length=255)
  tahun = models.CharField(max_length=4)
