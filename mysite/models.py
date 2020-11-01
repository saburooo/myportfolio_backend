from django.db import models


# Create your models here.

# 自分自身についてのクラス


class About(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=300)
    basic = models.TextField()
    episode = models.TextField()
    appeal = models.TextField()
    email = models.EmailField()

    def __str__(self):
        """何をリターンしましょうかね"""
        return self.title


class NameDetail(models.Model):
    name = models.OneToOneField(About, verbose_name='概要', on_delete=models.CASCADE)