from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class countries(models.Model):
    class Meta:
        verbose_name_plural = "Countries"
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.country.title()

    def save(self, *args, **kwargs):
        self.country = self.country.lower()
        super(countries, self).save(*args, **kwargs)

class State(models.Model):
    country = models.ForeignKey('countries', on_delete=models.PROTECT)
    state = models.CharField(max_length=30)

    def __str__(self):
        return self.state
# Create your models here.
class User_table(models.Model):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    Business_type = (
        ('Customer', 'Customer'), ('Wholesaler',
                                   'Wholesaler'), ('Broker', 'Broker'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_id = models.EmailField(primary_key = True, unique=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    fax = models.CharField(max_length=100, null=True, blank=True)
    Businesstype = models.CharField(
        max_length=30, choices=Business_type, default='Customer')
    address1 = models.CharField(max_length=30)
    address2 = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=30)
    country = models.ForeignKey('countries', on_delete=models.PROTECT)
    state = models.ForeignKey('State', on_delete=models.PROTECT)
    password = models.CharField(max_length=100)
    
    permit_user = models.BooleanField(default=False)

    def ___str__(self):
        return self.first_name + self.last_name
