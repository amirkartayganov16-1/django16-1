from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=155),
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name='Имя')
    descriptions = models.TextField(verbose_name='Описание')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кино'
        verbose_name_plural = 'Кино'

class Review(models.Model):
    text = models.TextField(verbose_name='Текст')