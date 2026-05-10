from django.db import models
from django.contrib.auth.models import User


class LoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} logged in"
    
class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=10, blank=True, null=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, null=True)

    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return self.user.username
    
class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="jobs_done")
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews_given")
    reviewee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews_received")

    rating = models.IntegerField()  # 1–5
    comment = models.TextField(blank=True)