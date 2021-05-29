from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class request_for_project_upload(models.Model):
    Project_title = models.CharField(max_length=100)
    Description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    Github_link = models.URLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Project_title


    def get_absolute_url(self):
        return reverse('myapp-home')

