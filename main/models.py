from django.db import models


class TestApi(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    check = models.BooleanField(default=False)

    def __str__(self):
        return self.title
