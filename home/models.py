from django.db import models
from profiles.models import User


class SiteReviews(models.Model):
    class Meta:
        verbose_name_plural = 'Site Reviews'
        ordering = ('-date',)

    CHOICES = [(i, i) for i in range(1, 6)]

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(choices=CHOICES, default=1, null=False)
    review = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.review
