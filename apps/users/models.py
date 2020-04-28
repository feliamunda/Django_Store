from django.db import models
from django.contrib.auth.models import AbstractUser

from apis.stripeAPI.customer import create_customer
from apps.orders.common import OrderStatus

# Create your models here.
class User(AbstractUser):
    customer_id = models.CharField(max_length=100, blank=True, null=True)

    @property
    def shipping_address(self):
        return self.shippingaddress_set.filter(default=True).first()

    @property
    def addresses(self):
        return self.shippingaddress_set.all().order_by('-default')

    @property
    def description(self):
        return 'Descripción para el usuario {}'.format(self.username)

    @property
    def billing_profiles(self):
        return self.billingprofile_set.all().order_by('-default')

    @property
    def billing_profile(self):
        return self.billingprofile_set.filter(default=True).first()

    def create_customer_id(self):
        if not self.has_customer():
            customer = create_customer(self)
            self.customer_id = customer.id
            self.save()

    def has_customer(self):
        return self.customer_id is not None
    
    def has_billing_profiles(self):
        return self.billingprofile_set.exists()

    def get_full_name(self):
        return '{} {}'.format(self.first_name,self.last_name)

    def has_shipping_address(self):
        return self.shipping_address is not None
    
    def orders_completed(self):
        return self.order_set.filter(status=OrderStatus.COMPLETED).order_by('-id')

    def has_shipping_addresses(self):
        return self.shippingaddress_set.exists()

    def has_billing_profile(self):
        return self.billingprofile_set.exists()

class Customer(User):
    class Meta:
        proxy = True
    
    def get_products(self):
        return []

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField()