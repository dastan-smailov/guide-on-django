from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70, unique=True)
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title    

class Place(models.Model):
    title = models.CharField(max_length=130)
    slug = models.SlugField(max_length=70, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = 'guide_cateogry')
    description = models.TextField(max_length=1024)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, blank=True)
    siteurl = models.URLField(max_length=200, blank=True)
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'

    def __str__(self):
        return self.title