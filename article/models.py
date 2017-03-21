from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=80)
    category = models.CharField(max_length=100, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    article = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.article


