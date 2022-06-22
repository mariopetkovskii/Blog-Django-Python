from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class BlogUser(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_image = models.ImageField(upload_to="profile_images/", null=True, blank=True)
    interests = models.CharField(max_length=100, null=True, blank=True)
    skills = models.CharField(max_length=100, null=True, blank=True)
    profession = models.CharField(max_length=30, null=True, blank=True)
    blocked_users = models.ManyToManyField(User, related_name="blocked_users", null=True, blank=True)

    def __str__(self):
        return self.name + " " + self.last_name

    def show_name_and_surname(self):
        return self.name + " " + self.last_name


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    files = models.FileField(upload_to="files/", null=True, blank=True)
    date_of_creating = models.DateTimeField(auto_now=True)
    date_of_last_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content_of_comment = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.content_of_comment
