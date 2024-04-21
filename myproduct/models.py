from django.db import models
from django.contrib.auth.models import User
#from .choices import CATEGORY_PRODUCT

CATEGORY_PRODUCT = (
    ('Fruit', 'Fruit'),
    ('Grains', 'Grains'),
    ('Vegetables', 'Vegetables'),
    ('Legumes', 'Legumes'),
    ('Oilseeds', 'Oilseeds'),
    ('Roots and Tubers', 'Roots and Tubers'),
    ('Nuts', 'Nuts'),
    ('Animal', 'Animal'),
    ('Poetry', 'Poetry'),
    ('Tropical Crops', 'Tropical Crops'),
    ('Indistrial crops', 'Indusctrial Crop'),
)

class product(models.Model):
    name = models.CharField(max_length=100, null=True)
    origin = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY_PRODUCT, null=True)
    packaging = models.CharField(max_length=100, null=True)
    harvest_date = models.DateField(null=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=3)
    Shelf_life = models.CharField(max_length=100, null=True)
    date_added = models.DateTimeField(auto_now_add=True)




    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name}'


class Sell_poultry(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    caption = models.TextField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    picture = models.ImageField(upload_to='profile_picture/', null=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)  

    def __str__(self):
        return f'Sold {self.product.name} on {self.date_posted}'

class Sell_cereals(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    caption = models.TextField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    picture = models.ImageField(upload_to='profile_picture/', null=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)  

    def __str__(self):
        return f'Sold {self.product.name} on {self.date_posted}'

class Sell_roottubers(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    caption = models.TextField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    picture = models.ImageField(upload_to='profile_picture/', null=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)  

    def __str__(self):
        return f'Sold {self.product.name} on {self.date_posted}'

class Sell_legumes(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    caption = models.TextField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    picture = models.ImageField(upload_to='profile_picture/', null=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)  

    def __str__(self):
        return f'Sold {self.product.name} on {self.date_posted}'

class Sell_cattle(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    caption = models.TextField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    picture = models.ImageField(upload_to='profile_picture/', null=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)  

    def __str__(self):
        return f'Sold {self.product.name} on {self.date_posted}'

    

    

class make_order(models.Model):
    myproduct = models.ForeignKey(product, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Make Order'

    def __str__(self):
        return f'{self.myproduct} ordered by {self.staff.username}'

    def __str(self):
        return f'{self.myproduct} ordered by {self.staff.username}'