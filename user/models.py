from django.db import models
from django.contrib.auth.models import User

CATEGORY_USER = (
    ('Staff', 'Staff'),
    ('Cooperative', 'Cooperative'),
    ('Farmer', 'Farmer'),
    ('Buyer', 'Buyer'),
    

)
class profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY_USER, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    WhatsApp_No = models.CharField(max_length=200, null=True)
    image = models.ImageField(default='avatar.jpg', upload_to='profile_images')

    def __str__(self):
        return f'{self.staff.username} - Profile'


