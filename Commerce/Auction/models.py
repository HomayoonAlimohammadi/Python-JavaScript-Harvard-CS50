from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')
    amount = models.FloatField()


class Category(models.Model):
    name = models.CharField(max_length=20)



class Comment(models.Model):
    user = models.ForeignKey(Bid, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Listing(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, related_name='listings', on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
    watchers = models.ManyToManyField(User, related_name='watchlist')
    bids = models.ForeignKey(Bid,  on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='listings')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)