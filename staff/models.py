from django.db import models
from django.utils import timezone


class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = 'Должности'


class Staff(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    date_except = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} {self.surname} {self.last_name}"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = 'Сотрудники'
