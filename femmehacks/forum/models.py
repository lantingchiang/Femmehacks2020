from django.db import models
from django.contrib.auth.models import AbstractUser
# reference user model by settings.AUTH_USER_MODEL
from django.conf import settings

class User(AbstractUser):
    pass
    # optional fields listing user's profession/field
    profession = models.CharField(max_length=200, blank=True)
    field = models.CharField(max_length=200, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'email']

    def __str__(self):
        return self.username


class Post(models.Model):
    def allow_comment_default():
        return False   

    def __str__(self):
        return self.title

    title = models.CharField(max_length=400)
    description = models.TextField()
    allow_comments = models.BooleanField(default=allow_comment_default())
    date = models.DateTimeField()

    class Meta:
        ordering = ['-date']


class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField()
    # also delete this comment when the corresponding post is deleted
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-date']