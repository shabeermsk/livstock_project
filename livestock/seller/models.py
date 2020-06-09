from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
from PIL import Image
from phone_field import PhoneField
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()


class Profile(models.Model):
    user = models.OneToOneField(User, unique=True,related_name='profile' ,on_delete=models.CASCADE)
    image = models.ImageField(default='default.JPG', upload_to='profile_pics',storage=gd_storage)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    address = models.CharField(blank=True,max_length=200)
    city = models.CharField(blank=True,max_length=100)
    state = models.CharField(blank=True,max_length=100)
    pincode = models.IntegerField(blank=True,null=True)
    is_verified = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
