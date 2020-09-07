from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)           #using info pulled in form native django User imported above
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name                #names the thingy in admin

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)       #a booleanfield, havent seen before, but represents a yes or no, true or false secnario.  is this product digital or phyical
    description = models.CharField(max_length=50, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property                               #little decorator thingy. idk just do it
    def imageURL(self):                     #this little number is a fix for our shop page incase a product doesnt have an image.
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)                     #create a many to one relationship between Order and Customer. many Customer attributes to one order
    date_ordered = models.DateTimeField(auto_now_add=True)                  #grabs current time, just copy paste
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total



class OrderItem(models.Model):                          #aka the cart
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)                     #create a many to one relationship between Order and Customer. many Customer attributes to one order
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.product.name

    @property
    def get_total(self):                    #logic to get the total of your cart. remember "OrderItem" is aka for Cart
        total = (self.product.price * self.quantity)
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.name
