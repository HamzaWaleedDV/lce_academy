from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=50)
    introduction = models.TextField(max_length=1500)
    subject = models.TextField(max_length=8000)
    conclusion = models.TextField(max_length=1500)
    main_image = models.ImageField()
    card_image = models.ImageField()
    sub_image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

