from django.db import models


class Star(models.Model):
    id = models.CharField(primary_key=True,max_length=50)
    name = models.CharField(max_length=200,null=True)
    bio = models.TextField(null=True)
    image = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name