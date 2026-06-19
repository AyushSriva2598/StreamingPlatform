from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class StreamPlatform(models.Model):
    pname= models.CharField(max_length=100) 
    about= models.TextField()
    website= models.URLField()

    def __str__(self):
        return self.pname
    

class WatchList(models.Model):
    status_choices= [
        ('Visible', 'Visible'),
        ('Hidden', 'Hidden'),
    ]
    title=models.CharField(max_length=100)
    storyline = models.TextField()
    active= models.CharField(max_length=100, choices=status_choices, default='Visible')
    platform= models.ForeignKey(StreamPlatform, null=True, blank=True, on_delete=models.CASCADE, related_name="watchlists")
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    review_user=models.ForeignKey(User, on_delete=models.CASCADE)
    rating= models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5),])
    description= models.TextField(blank=True, null=True)
    watchlist= models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.review_user)
    
