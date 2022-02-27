from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('auction:category', args=[self.name])



class Listing(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, related_name='listings', on_delete=models.CASCADE)
    watchers = models.ManyToManyField(User, related_name='watchlist', blank=True)
    category = models.ManyToManyField(Category, related_name='listings', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    starting_price = models.FloatField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')
    amount = models.FloatField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bids')
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

