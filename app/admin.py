from django.contrib import admin
from .models import Product
from .forms import ContactForm
from .models import Contact
from .models import User
from .models import ProductRecord
from django.contrib.auth.admin import UserAdmin  # Import the default UserAdmin

# Register your models here.

@admin.register(Product)

class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','discounted_price','category','product_image']

@admin.register(ProductRecord)
class ProductrecordAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity','country']

class ContactAdmin(admin.ModelAdmin):
    form = ContactForm  # Specify the form to be used in the admin interface
    list_display = ['name', 'email', 'message','phone_number']  # Customize the fields shown in the admin panel

# Register the model in the admin
admin.site.register(Contact, ContactAdmin)

# Register your custom User model with the default UserAdmin
admin.site.register(User, UserAdmin)
