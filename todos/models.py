from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название задачи")
    description = models.TextField(blank=True, verbose_name="Описание")
    is_done = models.BooleanField(default=False, verbose_name="Статус выполнения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title