from django.db import models

# Create your models here.

ACTIVE_CHOICES = (
    ("", "Select status"),
    ("active", "Active"),
    (" ", "Inactive"),
)

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)
    price = models.FloatField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Opinion(models.Model):
    name = models.CharField(max_length=50)
    career = models.CharField(max_length=100)
    image = models.ImageField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class New(models.Model):
    subject = models.CharField(max_length=70)
    message = models.TextField(max_length=5000)


class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    is_active = models.CharField(
        max_length=50,
        choices=ACTIVE_CHOICES,
        default='Select status',
    )
