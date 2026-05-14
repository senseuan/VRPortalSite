from django.db import models
from django.contrib.auth.models import User


# Определяем ReviewLike ДО VRReview, но используем строковое имя 'VRReview'
class ReviewLike(models.Model):
    LIKE = 1
    DISLIKE = -1
    TYPE_CHOICES = (
        (LIKE, "Нравится"),
        (DISLIKE, "Не нравится"),
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review_likes"
    )
    review = models.ForeignKey(
        "VRReview", on_delete=models.CASCADE, related_name="likes"
    )
    type = models.SmallIntegerField(choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "review")

    def __str__(self):
        return f"{self.user.username} - {self.review.headset_model} - {'лайк' if self.type == self.LIKE else 'дизлайк'}"


class VRReview(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    headset_model = models.CharField(max_length=200, verbose_name="Модель гарнитуры")
    rating = models.IntegerField(verbose_name="Оценка (1-5)")
    comment = models.TextField(verbose_name="Комментарий", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    @property
    def username(self):
        return self.author.username

    @property
    def likes_count(self):
        # Используем related_name 'likes'
        return self.likes.filter(type=ReviewLike.LIKE).count()

    @property
    def dislikes_count(self):
        return self.likes.filter(type=ReviewLike.DISLIKE).count()

    def __str__(self):
        return f"{self.author.username} - {self.headset_model} - {self.rating}⭐"

    class Meta:
        verbose_name = "Отзыв о VR"
        verbose_name_plural = "Отзывы о VR"
