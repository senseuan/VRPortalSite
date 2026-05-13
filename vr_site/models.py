from django.db import models

class VRReview(models.Model):
    username = models.CharField(max_length=100)
    headset_model = models.CharField(max_length=200)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.headset_model} - {self.rating}"