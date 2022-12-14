from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()


    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Coach(models.Model):
    DIRECTIONS = (
        ("bacha","бачата сеншуаль"),
        ("casno","сальса касіно(кубано)"),
        ("kimba", "кізомба"),
        ("urkiz","урбанкіз"),
        ("zouka","зук"),
        ("salna","сальса нью-йорк"),
        ("booga","бугі-вугі"),
        ("menga","меренге")
    )
    name = models.CharField(max_length=50, verbose_name="Викладачі, група яку ведуть. наприклад  Юрій Іванов, бачата сеншуаль")
    direction = models.CharField(max_length=30, choices=DIRECTIONS, default="menga", verbose_name='напрямок танцю(стиль)')
    details = models.TextField( verbose_name="детальний опис про заняття для групи")
    maintainer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   #default=1,
                                   verbose_name="Відповідальний за актуальність інформації")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'викладач або пара викладачів'
        permissions = (
            ('create_coach', 'create coach'),
        )

class Party(models.Model):
    title = models.CharField(max_length=40, verbose_name='назва вечірки'),
    price = models.CharField(max_length=8),
    brief = models.TextField()
    full = models.TextField()