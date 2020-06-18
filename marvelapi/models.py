from django.db import models

# Create your models here.
class Rus(models.Model):
    eng_title = models.TextField('Title_eng',null=True)
    rus_title = models.TextField('Title_eng',null=True)

    class Meta:
        verbose_name = 'Локальное название'
        verbose_name_plural = 'Локальные названия'