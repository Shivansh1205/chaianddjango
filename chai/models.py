from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class chai_variety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ml', 'masala'),
        ('pl', 'plain'),
        ('el', 'elaichi'),
        ('gi', 'ginger'),
        ('ki', 'kiwi'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default="description not provided")

    def __str__(self):
        return self.name

# one to many
class chai_reviews(models.Model):
    chai = models.ForeignKey(chai_variety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(default="your reviews")
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.chai.name}"
    
# many to many
    
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField(default="address")
    chai_varity = models.ManyToManyField(chai_variety, related_name='stores')

    def __str__(self):
        return self.name
    
# one to one
class certificate(models.Model):
    chai = models.OneToOneField(chai_variety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.IntegerField()
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f"certificate for {self.chai.name}"
