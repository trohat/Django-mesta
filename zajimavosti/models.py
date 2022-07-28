from django.db import models
from django.urls import reverse

# Create your models here.

class Mesto(models.Model):
    jmeno = models.CharField(max_length=60)
    zeme = models.CharField(max_length=80)
    zajimavost = models.TextField()
    pocet_obyvatel = models.IntegerField()
    hlavni_mesto = models.BooleanField()

    def __str__(self):
        return f"{self.jmeno} ({self.zeme})"

    def get_absolute_url(self):
        return reverse("detail", args=[self.jmeno])

    class Meta:
        verbose_name_plural = "Mesta"
        
