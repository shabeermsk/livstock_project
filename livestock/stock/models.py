from django.db import models
from django.utils import timezone
from django.contrib import auth
from django.urls import reverse
from django.template.defaultfilters import slugify
from seller.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver



class Stock(models.Model):
    image = models.ImageField(upload_to='stock_pics',blank=True)
    name = models.CharField(max_length=256)
    user = models.ForeignKey('auth.user',related_name='stock',on_delete=models.CASCADE,default='')
    slug = models.SlugField(null=False,unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    sellers_message = models.TextField(max_length=256)
    more_details = models.TextField(max_length=1000)
    posted_date = models.DateTimeField(auto_now=True)
    # qty_available = models.PositiveIntegerField(blank=True)
    minimum_order = models.PositiveIntegerField(blank=True)
    rate = models.PositiveIntegerField(blank=True)
    per_unit = models.ForeignKey('Unit',related_name='rate_unit',on_delete=models.CASCADE)
    unit = models.ForeignKey('Unit',related_name='order_unit',on_delete=models.CASCADE)
    breed = models.CharField(max_length=200)
    location = models.ManyToManyField('Location')
    delivery_within = models.PositiveIntegerField()
    deliverytimechoice = models.CharField(
                             choices=[('Hours','Hours'),('Days','Days'),('Weeks','weeks')],
                             max_length=20
                            )


    class Meta:
       ordering = ('-posted_date', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stock:detail',kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 600:
            output_size = (300, 600)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Category(models.Model):
    title = models.CharField(max_length=300)
    primaryCategory = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Location(models.Model):
    district = models.CharField(max_length=100)

    def __str__(self):
        return self.district

class Unit(models.Model):
    unit_name = models.CharField(max_length=20)

    def __str__(self):
            return self.unit_name
