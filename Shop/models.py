from django.db import models
import os
import random
from django.core.validators import MinValueValidator , MaxValueValidator
from django.db.models.signals import pre_save,post_save
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import unique_slug_generator
from django.contrib.auth.models import User



def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name , ext = os.path.splitext(base_name)
    return name ,ext
def upload_image_path(instance,filenames):
    new_filename = random.randint(1,1000000)
    name , ext = get_filename_ext(filenames)
    final_filename = f'{new_filename}{ext}'
    return f"products/{new_filename}/{final_filename}"

class category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=150,blank=True, null=True, verbose_name=("Slug"))
    image = models.ImageField(upload_to=upload_image_path, null=True , blank=True ,verbose_name=("Product Image"))
    description = models.TextField(max_length=5000,verbose_name=("Description"),blank=True, null=True)
    def __str__(self):
        return f"{self.name}"
class discount(models.Model):
    title = models.CharField(max_length=120)
    Active = True
    Inactive = False
    Status_select = [
        (Active, 'Active'),
        (Inactive, 'Inactive'),
    ]
    status= models.BooleanField(default=Inactive,choices=Status_select, blank=True, null=True,max_length=15)
    priority=models.BooleanField(default=False,blank=True, null=True)
    value = models.DecimalField(decimal_places=2 , max_digits=10 , default=1, blank=True, null=True,)
    date_start = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_end = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return f"{self.title}" 
class product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=20 , decimal_places=0 ,default=39.99)
    featured = models.BooleanField(default=False) 
    category = models.ForeignKey(category,on_delete=models.CASCADE ,null=True,blank=True,default=1)
    discount = models.ForeignKey(discount,on_delete=models.CASCADE ,null=True,blank=True)
    discounted_prices = models.DecimalField(max_digits=20 , decimal_places=0 ,default=0,null=True,blank=True)
    slug = models.SlugField(max_length=150,blank=True, null=True, verbose_name=("Slug"),unique=True)
    description = models.TextField(max_length=5000,verbose_name=("Description"),blank=True, null=True)
    image = models.ImageField(upload_to=upload_image_path, null=True , blank=True ,verbose_name=("Product Image"))
    additional_image_1 = models.ImageField(
        upload_to=upload_image_path, blank=True, null=True, max_length=500, verbose_name=("Image_1"),)
    additional_image_2 = models.ImageField(
        upload_to=upload_image_path, blank=True, null=True, max_length=500, verbose_name=("Image_2"),)
    additional_image_3 = models.ImageField(
        upload_to=upload_image_path, blank=True, null=True, max_length=500, verbose_name=("Image_3"),)
    additional_image_4 = models.ImageField(
        upload_to=upload_image_path, blank=True, null=True, max_length=500, verbose_name=("Image_4"),)
    Like = models.PositiveIntegerField(default=0,blank=True, null=True, verbose_name=("Like"),)
    Active = True
    Inactive = False
    Status_select = [
        (Active, 'Active'),
        (Inactive, 'Inactive'),
    ]
    status= models.BooleanField(default=False,choices=Status_select ,blank=True, null=True,max_length=15)
    deleted = models.BooleanField(default=False, verbose_name=("Product Deleted"))
    tags = models.CharField(max_length=100, verbose_name=("Tags"), blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    date_update = models.DateTimeField(auto_now=True, blank=True, null=True)
    date_Deleted = models.DateTimeField(auto_now=False, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0,blank=True, null=True, verbose_name=("Quantity"))
    viewed =  models.PositiveIntegerField(default=0,blank=True, null=True, verbose_name=("Viewed"))
    width = models.FloatField(blank=True, null=True, verbose_name=("Width"))
    height = models.FloatField(blank=True, null=True, verbose_name=("Height"))
    length = models.DecimalField(default=0 , max_digits=10 , decimal_places=3)
    Weight = models.DecimalField(default=0,max_digits=10, decimal_places=3, blank=True, null=True,  verbose_name=("Weight"))
    blue = 'blue'
    red = 'red'
    yellow = 'yellow'
    green = 'green'
    black = 'black'
    white = 'white'
    brown = 'brown'
    pink = 'pink'
    orange = 'orange'
    Color_select =[
    (yellow , 'yellow'),
    (green , 'green'),
    (blue , 'blue'),
    (red , 'red'),
    (black , 'black'),
    (white , 'white'),
    (brown , 'brown'),
    (pink , 'pink'),
    (orange , 'orange'),
    ]
    color = models.CharField(max_length=15 , choices=Color_select,default=black,blank=True,null=True)
    feedback_average = models.PositiveIntegerField(default=0,blank=True, null=True, verbose_name=("Feedback average"))
    feedback_number = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name=("Feedback number"))
    New = 'New'
    Hot = 'Hot'
    Advertising_select = [
        (New, 'New'),
        (Hot, 'Hot'),
    ]
    Advertising = models.CharField(
        max_length=13,
        choices=Advertising_select,
        default=New, blank=True, null=True,
    )
    Medium = 'M'
    Large = 'L'
    XLarge = 'XL'
    XXLarge= 'XXL'
    Size_select = [
        (Medium, 'M'),
        (Large, 'L'),
        (XLarge, 'XL'),
        (XXLarge, 'XXL'),
    ]
    size = models.CharField(max_length=13,choices=Size_select,default=Large)
    wool = 'wool'
    leather = 'leather'
    cotton = 'cotton'
    polyester= 'polyester'
    Material_select = [
    (wool , 'wool'),
    (leather , 'leather'),
    (cotton , 'cotton'),
    (polyester , 'polyester'),
    ]
    material = models.CharField(max_length=13,choices=Material_select,default= wool)
    star = models.IntegerField(default=0 , validators=[MaxValueValidator(5),MinValueValidator(0)])
    spring = 'spring'
    summer = 'summer'
    autumn = 'autumn'
    winter= 'winter'
    season_select = [
        ( spring, 'spring'),
        (summer, 'summer'),
        (autumn , 'autumn'),
        (winter , 'winter'),
        ]
    season = models.CharField(max_length=13,choices=season_select,default=winter,null=True,blank=True)
    Women = 'Women'
    Man = 'Man'
    Both = 'Both'
    sexuality_select = [
        (Women , 'Women'),
        (Man , 'Man'),
        (Both , 'Both'),
        ]
    sexuality = models.CharField(max_length=13,choices=sexuality_select,default=Man,null=True,blank=True)
    def __str__(self):
        return self.title
class user_model(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True, )
    bio = models.TextField(blank=True, null=True)
    PhoneNumber = models.CharField(max_length=13)
    city = models.CharField(max_length=100, blank=True, null=True, )
    address = models.CharField(max_length=150)
    post_code = models.CharField(max_length=100, blank=True, null=True, ) 
    country = models.CharField(max_length=100, blank=True, null=True, )
    birthday = models.DateField(auto_now=False, blank=True, null=True)
    customer = 'customer'
    seller = 'seller'
    Roll_select = [
        (customer, 'customer'),
        (seller, 'seller'),
        ]
    roll = models.CharField(
        max_length=13,
        choices=Roll_select,
        default=customer,
        blank=True, null=True,
    )
    Active = True
    Inactive = False
    Status_select = [
        (Active, True),
        (Inactive, False),
    ]
    status_online= models.BooleanField(default=False,choices=Status_select, blank=True, null=True,max_length=15)
    slug = models.SlugField(
        blank=True, null=True, verbose_name=("Slug"))
    def __str__(self):
        return self.user.username
class seller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    Active = True
    Inactive = False
    Status_select = [
        (Active, True),
        (Inactive, False),
    ]
    status= models.BooleanField(default=False,choices=Status_select, blank=True, null=True,max_length=15)
    message = models.TextField(max_length=500)
class OrderProduct(models.Model):
    quantity = models.PositiveIntegerField(default=0,blank=True, null=True, verbose_name=("Quantity"))
    product = models.ForeignKey(product, on_delete=models.CASCADE)
class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(OrderProduct)
    title = models.CharField(max_length=120)
    quantity = models.PositiveIntegerField(default=0,blank=True, null=True, verbose_name=("Quantity"))
    price = models.DecimalField(decimal_places=2 , max_digits=10 , default=39.99,verbose_name=("Price"))
    discount = models.ForeignKey(discount, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    date_update = models.DateTimeField(auto_now=True, blank=True, null=True)
    ordered=models.BooleanField(default=False)
    Weight = models.DecimalField(default=0,max_digits=10, decimal_places=3, blank=True, null=True,  verbose_name=("Weight"))
    PENDING = 'PENDING'
    Underway = 'Underway'
    COMPLETE = 'COMPLETE'
    Refunded = 'Refunded'
    Status_select = [
            (PENDING, 'PENDING'),
            (Underway, 'Underway'),
            (COMPLETE, 'COMPLETE'),
            (Refunded, 'Refunded'),
        ]
    status = models.CharField(
            max_length=13,
            choices=Status_select,
            default=PENDING,
        )
    details = models.CharField(max_length=120)
    def __str__(self):
        return self.title

class Comment(models.Model):
    product = models.ForeignKey(product,related_name="Comments",on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    massage = models.TextField()
    date = models.DateField(auto_now_add=True)
class CommentReply(models.Model):
    comment = models.ForeignKey(Comment, related_name="replies", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    massage = models.TextField()
    date = models.DateField(auto_now_add=True)
class payment(models.Model):
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    request_amount = models.FloatField(default=0.00, blank=True, null=True)
    fee = models.FloatField(default=0.00, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    Paid = 'Paid'
    Pending = 'Pending'
    Progressing = 'Progressing'
    Refunded = 'Refunded'
    Status_select = [
            (Paid, 'Paid'),
            (Pending, 'Pending'),
            (Progressing, 'Progressing'),
            (Refunded, 'Refunded'),
        ]
    status = models.CharField(
            max_length=13,
            choices=Status_select,
            default=Pending,
        )
    status= models.BooleanField(default=False,blank=True, null=True,max_length=15)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_update = models.DateTimeField(auto_now=True, blank=True, null=True)
    order = models.ForeignKey(order, on_delete=models.CASCADE)
#function for crate a Random Slug For each product before create it.
def product_pre_save_receiver(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(product_pre_save_receiver,sender=product)


