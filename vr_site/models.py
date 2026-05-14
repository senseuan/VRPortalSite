from django.db import models
from django.contrib.auth.models import User

class VRReview(models.Model):
    username = models.CharField(max_length=100, verbose_name="Имя пользователя")
    headset_model = models.CharField(max_length=200, verbose_name="Модель гарнитуры")
    rating = models.IntegerField(verbose_name="Оценка (1-5)")
    comment = models.TextField(verbose_name="Комментарий", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.username} - {self.headset_model} - {self.rating}⭐"

    class Meta:
        verbose_name = "Отзыв о VR"
        verbose_name_plural = "Отзывы о VR"