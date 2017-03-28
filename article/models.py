from django.db import models
from django.core.urlresolvers import reverse


class Article(models.Model):
    title = models.CharField(max_length=80)
    category = models.CharField(max_length=100, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    article = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.article

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'article_id': self.article_id})
        return "http://127.0.0.1:8000%s" % path

    class Meta:
        ordering = ['-date_time']