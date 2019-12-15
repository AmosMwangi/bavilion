from django.db import models
import datetime as dt


class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ["first_name"]


class Category(models.Model):
    choise = models.CharField(max_length=30)

    def __str__(self):
        return self.choise

    class Meta:
        ordering = ["choise"]


class Location(models.Model):
    area = models.CharField(max_length=30)

    def __str__(self):
        return self.area

    class Meta:
        ordering = ["area"]
