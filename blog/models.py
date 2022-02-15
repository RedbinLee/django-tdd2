from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.urls import reverse # import reversing has changed to django.urls

# Create your models here.


class Entry(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        # change the  __self__ method!! from object to title
        return self.title

    def get_absolute_url(self) :
        # by using reverse, get url of entry_detail defined in urls.py 
        # kwargs == arguments are treated as dictionary / args == arguments are treated as tuple type
        return reverse('entry_detail', kwargs={'pk': self.pk})

    class Meta:
        # this will be tested under the _meta class in test.py
        verbose_name_plural = "entries"

class Comment(models.Model) :
    entry = models.ForeignKey(Entry, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    
    def __str__(self) :
        return self.body