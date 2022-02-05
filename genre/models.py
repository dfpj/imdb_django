from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=50,primary_key=True)

    def __str__(self):
        return self.title


