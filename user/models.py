from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from tinymce.models import HTMLField
from taggit.managers import TaggableManager
from rest_framework import serializers


class countries(models.Model):
    class Meta:
        verbose_name_plural = "Countries"
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.country.title()

    def save(self, *args, **kwargs):
        self.country = self.country.lower()
        super(countries, self).save(*args, **kwargs)


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
    email_id = models.EmailField(primary_key=True, unique=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    fax = models.CharField(max_length=100, null=True, blank=True)
    Businesstype = models.CharField(
        max_length=30, choices=Business_type, default='Customer')
    address1 = models.CharField(max_length=30)
    address2 = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=30)
    country = models.ForeignKey('countries', on_delete=models.PROTECT)
    password = models.CharField(max_length=100)
    permit_user = models.BooleanField(default=False)
    activate_hash = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.first_name + str(" ")+self.last_name+str(" -> ")+str(self.Businesstype)


class Blog(models.Model):
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="blog_images/", blank=True, null=True)
    title = models.CharField(max_length=30)
    subject = HTMLField(blank=True, null=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return (self.title)


class Subscribed_users(models.Model):
    class Meta:
        verbose_name_plural="Subscribed Users"
    email = models.EmailField(max_length=90)

    def __str__(self):
        return str(self.email)


class ConversionRate(models.Model):
    class Meta:
        verbose_name_plural = "Conversion Rate"
    conversion_rate = models.FloatField(
        verbose_name="Conversion Rate Value in INR ")

    def __str__(self):
        return str(self.conversion_rate)


class ConversionRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversionRate
        fields = '__all__'


class BirthStones(models.Model):
    class Meta:
        verbose_name_plural = "Birth Stones"

    image = models.ImageField(upload_to="birthstones/", blank=True, null=True)
    name = models.CharField(max_length=30, verbose_name="Stone Name")
    month = models.CharField(max_length=30, verbose_name="Month")
    tagline = models.CharField(max_length=300, verbose_name="Tagline")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.month + " - " + self.name
