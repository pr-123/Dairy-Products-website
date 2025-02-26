from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.conf import settings


CATEGORY_CHOICES=(
    ('CR','Curd'),
    ('ML','Milk'),
    ('LS','Lassi'),
    ('MS','MilkShake'),
    ('PN','Paneer'),
    ('GH','Ghee'),
    ('CZ','Cheese'),
    ('IC','Ice-Cream'),

)

COUNTRIES = [
    ('United States', 'United States'),
    ('Canada', 'Canada'),
    ('India', 'India'),
    ('GB', 'United Kingdom'),
    ('Australia', 'Australia'),
    ('Germany', 'Germany'),
    ('France', 'France'),
    ('Spain', 'Spain'),
    ('Italy', 'Italy'),
    ('Mexico', 'Mexico'),
    ('Brazil', 'Brazil'),
    ('Japan', 'Japan'),
    ('South Korea', 'South Korea'),
    ('China', 'China'),
    ('Russia', 'Russia'),
    ('South Africa', 'South Africa'),
    ('Egypt', 'Egypt'),
    ('Argentina', 'Argentina'),
    ('Chile', 'Chile'),
    ('Turkey', 'Turkey'),
    ('Nigeria', 'Nigeria'),
    ('Saudi Arabia', 'Saudi Arabia'),
    ('United Arab Emirates', 'United Arab Emirates'),
    ('Thailand', 'Thailand'),
    ('Vietnam', 'Vietnam'),
    ('Singapore', 'Singapore'),
    ('Malaysia', 'Malaysia'),
    ('Indonesia', 'Indonesia'),
    ('Philippines', 'Philippines')
    # Add more countries here as needed
]

class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)  # ForeignKey to User model
    title=models.CharField(max_length=100,default='dairy')
    selling_price=models.FloatField(default=0.0)
    discounted_price=models.FloatField(default=0)
    description=models.TextField(default="""100% natural, non-homogenised, and carefully tested for being 
    antibiotic-free and artificially administered hormone-free. Your search for pure cow milk near me ends here""")
    composition=models.TextField(default='')
    prodapp=models.TextField(default='Directly sourced from farm, connected with the farmers nearby and everywhere')
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2,default='CR')
    product_image=models.ImageField(upload_to='product')
    country=models.CharField(choices=COUNTRIES,blank=False,null=False,default='United States')
    def __str__(self):
        return self.title

class ProductRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)  # ForeignKey to User model
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_orders')  # ForeignKey to Product model
    quantity = models.PositiveIntegerField(default=1)  # Quantity of the product ordered
    order_date = models.DateTimeField(auto_now_add=True)  # Date and time when the order was placed
    country = models.CharField(max_length=100, default='United States')  # Country from where the order is placed

    def __str__(self):
        return f"{self.user} ordered {self.product.title} on {self.order_date}"

    class Meta:
        verbose_name = "Product Order"
        verbose_name_plural = "Product Orders"
        db_table_comment = "Records the product details alongwith the country and the user"
    
# models.py

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    phone_number = models.CharField(max_length=15, null=True, default="0000000000")


    def __str__(self):
        return self.name
    
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    confirm_password=models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.username
    






