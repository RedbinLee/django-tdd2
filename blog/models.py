from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.


class Entry(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "entries"