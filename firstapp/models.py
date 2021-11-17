
from typing import Sequence
from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import DateTimeCheckMixin
from django.db.models.fields.related import ForeignKey
from django.core.validators import RegexValidator
from tinymce.models import HTMLField
import datetime

class Blog(models.Model):
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="profile/", blank=True, null=True)
    title = models.CharField(max_length=30)
    subject = HTMLField(blank=True, null=True)

    def __str__(self):
        return (self.title)


# Create your models here.
class Database(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)


class countries(models.Model):
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.country


class location(models.Model):
    place = models.CharField(max_length=30)

    def __str__(self):
        return self.place.title()

    def save(self, *args, **kwargs):
        self.place = self.place.lower()
        super(location, self).save(*args, **kwargs)


class gemtype(models.Model):
    gem = models.CharField(max_length=50)

    def __str__(self):
        return self.gem.title()
    def save(self, *args, **kwargs):
        self.gem = self.gem.lower()
        super(gemtype, self).save(*args, **kwargs)


class companyinfo(models.Model):
    date = models.DateField(auto_now_add=True)
    company_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    address = models.TextField()
    country = models.ForeignKey(countries, on_delete=models.PROTECT)
    mobile_no = models.CharField(max_length=20)
    tel_no = models.CharField(max_length=20, null=True)
    email = models.EmailField(blank=True,null=True)
    website = models.EmailField(max_length=150,blank=True,null=True)
    pan_no = models.CharField(max_length=20,blank=True,null=True)
    GST_no = models.CharField(max_length=20,blank=True,null=True)
    line_id = models.CharField(max_length=20,blank=True,null=True)
    wechat_id = models.CharField(max_length=5,blank=True,null=True)

    def __str__(self):
         return self.company_name.title()
         
    def save(self, *args, **kwargs):
        self.company_name = self.company_name.lower()
        super(companyinfo, self).save(*args, **kwargs)

class jewell(models.Model):
    jewel = models.CharField(max_length=30)

    def __str__(self):
        return self.jewel
    def save(self, *args, **kwargs):
        self.jewel = self.jewel.lower()
        super(jewell, self).save(*args, **kwargs)


class centerstone(models.Model):
    stone = models.CharField(max_length=30)

    def __str__(self):
        return self.stone
    def save(self, *args, **kwargs):
        self.stone = self.stone.lower()
        super(centerstone, self).save(*args, **kwargs)


class colorofcstone(models.Model):
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.color
    def save(self, *args, **kwargs):
        self.color = self.color.lower()
        super(colorofcstone, self).save(*args, **kwargs)


class shape1(models.Model):
    shape = models.CharField(max_length=30)

    def __str__(self):
        return self.shape
    def save(self, *args, **kwargs):
        self.shape = self.shape.lower()
        super(shape1, self).save(*args, **kwargs)


class metal1(models.Model):
    metal = models.CharField(max_length=30)

    def __str__(self):
        return self.metal
    def save(self, *args, **kwargs):
        self.metal= self.metal.lower()
        super(metal1, self).save(*args, **kwargs)


class certificate(models.Model):

    class Meta:
        verbose_name_plural = "ColorStone Certificates Types"
    cert = models.CharField(max_length=30)
    def __str__(self):
        return self.cert
    def save(self, *args, **kwargs):
        self.cert = self.cert.lower()
        super(certificate, self).save(*args, **kwargs)


class currencies(models.Model):
    currency = models.CharField(max_length=30)

    def __str__(self):
        return self.currency.title()
    def save(self, *args, **kwargs):
        self.currency = self.currency.lower()
        super(currencies, self).save(*args, **kwargs)


class POJ(models.Model):

    date = models.DateField(auto_now_add=True)
    company_name = models.ForeignKey(
        'companyinfo', on_delete=PROTECT, blank=True)
    location = models.ForeignKey(
        'location', on_delete=models.PROTECT, null=True, blank=True)
    jewellery = models.ForeignKey(
        'jewell', on_delete=models.PROTECT, null=True, blank=True)
    center_stone = models.ForeignKey(
        'centerstone', on_delete=models.PROTECT, null=True, blank=True)
    color_of_center_stone = models.ForeignKey(
        'colorofcstone', on_delete=models.PROTECT, null=True, blank=True)
    shape = models.ForeignKey(
        'shape1', on_delete=models.PROTECT, null=True, blank=True)
    metal = models.ForeignKey(
        'metal1', on_delete=models.PROTECT, null=True, blank=True)
    grosswt = models.FloatField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    cert = models.ForeignKey(
        'certificate', on_delete=models.PROTECT, null=True, blank=True)
    pcs = models.BigIntegerField()
    amount = models.DecimalField(decimal_places=2, max_digits=9)
    discount = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True)
    discount_amount = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)

    total = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True)
    purchase_approval = models.BooleanField(default=False)
    comment = models.TextField(max_length=3000, blank=True, null=True)


    def save(self, *args, **kwargs):

        self.discount_amount = (self.amount * self.discount) // 100
        # self.stockid=str(str('J-')+str(self.id))
        self.total = self.amount-self.discount_amount
        super(POJ, self).save(*args, **kwargs)
        obj = Inventoryofjewellery.objects.create(stockid=str('J-')+str(self.id), location=self.location, jewellery_type=self.jewellery, center_stone=self.center_stone,
                                                  color_of_center_stone=self.color_of_center_stone, shape=self.shape,
                                                  metal=self.metal, grosswt=self.grosswt, cert=self.cert, pcs=self.pcs, tag_price=self.tag_price,
                                                  purchaseapv=self.purchase_approval)
    currencyid = models.ForeignKey(
        'currencies', on_delete=models.PROTECT, null=True, blank=True)
    tag_price = models.FloatField()
    rate = models.FloatField()
    # salesapproval

    def __str__(self):
        return str(self.id)


class Inventoryofjewellery(models.Model):
    stockid = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=30)
    jewellery_type = models.CharField(max_length=30)
    center_stone = models.CharField(max_length=30)
    color_of_center_stone = models.CharField(max_length=30)
    shape = models.CharField(max_length=30)
    metal = models.CharField(max_length=30)
    grosswt = models.FloatField()
    cert = models.CharField(max_length=30)
    pcs = models.IntegerField()
    #  def save(self, *args, **kwargs):

    #     # self.stockid=str('J-')+str(self.id)
    #     currobj=super(Inventoryofjewellery, self).save(*args, **kwargs)
    #     self.stockid=str('J-')+str(currobj.id)
    #     self.save()
    tag_price = models.FloatField()
    purchaseapv = models.BooleanField(blank=True)
    status = models.CharField(max_length=30, default=False)
    cartstatus = models.BooleanField(default=False)
    appvreturnstatus = models.BooleanField(default=False)
    frontend = models.BooleanField(default=False)

    def __str__(self):
        return str(self.stockid)


class Salesofjewellery(models.Model):
    date = models.DateField(auto_now_add=True)
    stockid = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    jewellery_type = models.CharField(max_length=30)
    center_stone = models.CharField(max_length=30)
    shape = models.CharField(max_length=30)
    metal = models.CharField(max_length=30)
    gross_wt = models.FloatField()
    certificate = models.CharField(max_length=30)
    PCS = models.IntegerField(verbose_name="Pieces")
    amount = models.FloatField()
    DIS = models.FloatField()
    DIS_amount = models.FloatField()
    total_value = models.FloatField()
    currency = models.CharField(max_length=30)
    tag_price = models.FloatField()
    rate = models.FloatField()
    salesapprovalstatus = models.BooleanField(default=False)
    comment = models.TextField(max_length=3000, blank=True, null=True)

    def __str__(self):
        return self.company_name
        
class cloneInvofjewellery(models.Model):

    stockid = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    jewellery_type = models.CharField(max_length=30)
    center_stone = models.CharField(max_length=30)
    shape = models.CharField(max_length=30)
    metal = models.CharField(max_length=30)
    gross_wt = models.FloatField(null=True)
    certificate = models.CharField(max_length=30)
    PCS = models.IntegerField()
    amount = models.FloatField(blank=True, null=True)
    DIS = models.FloatField(blank=True, null=True)
    DIS_amount = models.FloatField(blank=True, null=True)
    total_value = models.FloatField(blank=True, null=True)
    currency = models.ForeignKey(
        currencies, on_delete=models.PROTECT, null=True, blank=True)
    tag_price = models.FloatField()
    rate = models.FloatField(blank=True, null=True)
    salesapprovalstatus = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # new_obj = Salesofjewellery.objects.create(stockid=self.stockid, company_name=self.company_name, location=self.location, jewellery_type=self.jewellery_type,
        #                                           center_stone=self.center_stone, shape=self.shape,
        #                                           metal=self.metal, gross_wt=self.gross_wt, certificate=self.certificate, PCS=self.PCS, amount=self.amount, DIS=self.DIS, DIS_amount=self.DIS_amount, total_value=self.total_value, currency=self.currency, tag_price=self.tag_price,
        #                                           rate=self.rate, salesapprovalstatus=self.salesapprovalstatus)
        super(cloneInvofjewellery, self).save()


class Salesreturn(models.Model):
    date = models.DateField(auto_now_add=True)
    stockid = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    jewellery_type = models.CharField(max_length=30)


# purchase of diamonds

class certificate_d(models.Model):
    certd = models.CharField(max_length=30)

    def __str__(self):
        return self.certd


class clarity(models.Model):
    clarity = models.CharField(max_length=30)

    def __str__(self):
        return self.clarity


class color_origin(models.Model):
    c_o = models.CharField(max_length=30)

    def __str__(self):
        return self.c_o


class white_color_grade(models.Model):
    w_c_g = models.CharField(max_length=30)

    def __str__(self):
        return self.w_c_g


class fancy_color_intensity(models.Model):
    f_c_i = models.CharField(max_length=30)

    def __str__(self):
        return self.f_c_i


class fancycolor_grade(models.Model):
    f_c_grade = models.CharField(max_length=30)

    def __str__(self):
        return self.f_c_grade


class cut(models.Model):
    cut = models.CharField(max_length=30)

    def __str__(self):
        return self.cut


class polish(models.Model):
    polish = models.CharField(max_length=30)

    def __str__(self):
        return self.polish


class symmetry(models.Model):
    symmetry = models.CharField(max_length=30)

    def __str__(self):
        return self.symmetry


class fluorescence_intensity(models.Model):
    f_intensity = models.CharField(max_length=30)

    def __str__(self):
        return self.f_intensity


class fluorescence_color(models.Model):
    f_color = models.CharField(max_length=30)

    def __str__(self):
        return self.f_color


class shape_d(models.Model):
    shape = models.CharField(max_length=30)

    def __str__(self):
        return self.shape


class POD(models.Model):
    date = models.DateField(auto_now_add=True)
    # stockid_d = models.CharField(max_length=30)
    company_name = models.ForeignKey('CompanyInfo', on_delete=PROTECT)
    location = models.ForeignKey('location', on_delete=models.PROTECT, null=True)
    shape = models.ForeignKey('shape_d', on_delete=models.PROTECT, null=True)
    clarity = models.ForeignKey('clarity', on_delete=models.PROTECT)
    color_origin1 = models.ForeignKey('color_origin', on_delete=models.PROTECT)
    white_color_grade1 = models.ForeignKey(
        'white_color_grade', on_delete=models.PROTECT)
    fancy_color_intensity1 = models.ForeignKey(
        'fancy_color_intensity', on_delete=models.PROTECT)
    fancycolor_grade = models.ForeignKey(
        'fancycolor_grade', on_delete=models.PROTECT)
    cut = models.ForeignKey('cut', on_delete=models.PROTECT)
    polish = models.ForeignKey('polish', on_delete=models.PROTECT)
    symmetry = models.ForeignKey('symmetry', on_delete=models.PROTECT)
    measurements = models.CharField(max_length=30,blank=True,null=True)
    depth = models.IntegerField()
    table_perc = models.IntegerField()
    fluorescence_intensity = models.ForeignKey(
        'fluorescence_intensity', on_delete=models.PROTECT)
    fluorescence_color = models.ForeignKey(
        'fluorescence_color', on_delete=models.PROTECT)
    certificate_no_d = models.CharField(max_length=30)
    certificate_d = models.ForeignKey(
        'certificate_d', on_delete=models.PROTECT)
    laser_inscription = models.BooleanField()
    PCS_d = models.IntegerField()
    weight_d = models.FloatField()
    price = models.FloatField(null=True, blank=True)
    units = models.CharField(max_length=30,blank=True,null=True)
    amount_d = models.DecimalField(decimal_places=2, max_digits=9)
    DIS_d = models.PositiveSmallIntegerField(blank=True, null=True)
    DIS_Amount_d = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    

    total_val_d = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True)
    purchaseapv_d = models.BooleanField(default=False)
    comment = models.TextField(max_length=3000, blank=True, null=True)


    def save(self, *args, **kwargs):
        # self.amount_d = (self.price * self.units * self.PCS_d)
        # self.DIS_Amount_d = (self.amount_d * self.DIS_d) // 100
        # self.total_val_d = self.amount_d - self.DIS_Amount_d
        super(POD, self).save(*args, **kwargs)
        obj2 = Inventoryofdiamond.objects.create(stockid=str('D-')+str(self.id), location=self.location, shape=self.shape,
                                                 clarity=self.clarity, white_color_grade1=self.white_color_grade1, fancy_color_intensity1=self.fancy_color_intensity1,
                                                 fancycolor_grade=self.fancycolor_grade, cut=self.cut, weight_d=self.weight_d, price=self.price, polish=self.polish, symmetry=self.symmetry, measurements=self.measurements,
                                                 depth=self.depth, table=self.table_perc, fluorescence_intensity=self.fluorescence_intensity, fluorescence_color=self.fluorescence_color, certificate_no_d=self.certificate_no_d,
                                                 certificate_d=self.certificate_d, units=self.units, laser_inscription=self.laser_inscription, PCS_d=self.PCS_d, tag_price_d=self.tag_price_d, purchaseapv_d=self.purchaseapv_d)
    currency = models.ForeignKey('currencies', on_delete=models.PROTECT)
    tag_price_d = models.FloatField()
    rate_d = models.FloatField()

    def __str__(self):
        return str(self.id)

# Inventory of Diamond


class Inventoryofdiamond(models.Model):
    stockid = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    shape = models.CharField(max_length=30)
    clarity = models.CharField(max_length=30)
    white_color_grade1 = models.CharField(max_length=30)
    fancy_color_intensity1 = models.CharField(max_length=30)
    fancycolor_grade = models.CharField(max_length=30)
    cut = models.CharField(max_length=30)
    polish = models.CharField(max_length=30)
    symmetry = models.CharField(max_length=30)
    measurements = models.CharField(max_length=30,blank=True,null=True)
    depth = models.FloatField(null=True, blank=True)
    table = models.FloatField(null=True, blank=True)
    fluorescence_intensity = models.CharField(max_length=30)
    fluorescence_color = models.CharField(max_length=30)
    certificate_no_d = models.CharField(max_length=30)
    certificate_d = models.CharField(max_length=30)
    laser_inscription = models.CharField(max_length=30)
    PCS_d = models.IntegerField(null=True, blank=True)
    weight_d = models.FloatField(null=True, blank=True)
    units = models.CharField(max_length=30,blank=True,null=True)
    tag_price_d = models.FloatField(null=True, blank=True)
    status = models.BooleanField(default=False)
    purchaseapv_d = models.BooleanField(blank=True)
    cartstatus = models.BooleanField(default=False)
    appvreturnstatus_d = models.BooleanField(default=False)
    price = models.FloatField(null=True, blank=True)
    def __str__(self):
        return str(self.stockid)


# SALE OF DIAMOND
class Salesofdiamond(models.Model):
    date = models.DateField(auto_now_add=True)
    stockid = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    shape = models.CharField(max_length=30)
    clarity = models.CharField(max_length=30)
    color_origin1 = models.CharField(max_length=30)
    white_color_grade1 = models.CharField(max_length=30)
    fancy_color_intensity1 = models.CharField(max_length=30)
    fancycolor_grade = models.CharField(max_length=30)
    fancy_color_grade = models.CharField(max_length=30)
    cut = models.CharField(max_length=30)
    polish = models.CharField(max_length=30)
    symmetry = models.CharField(max_length=30)
    measurements = models.CharField(max_length=30,blank=True,null=True)
    depth = models.FloatField(null=True, blank=True)
    table = models.FloatField(null=True, blank=True)
    fluorescence_intensity = models.CharField(max_length=30)
    fluorescence_color = models.CharField(max_length=30)
    certificate_no_d = models.CharField(max_length=30)
    certificate_d = models.CharField(max_length=30)
    laser_inscription = models.CharField(max_length=30)
    PCS_d = models.IntegerField(null=True, blank=True)
    weight_d = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    units = models.CharField(max_length=30,blank=True,null=True)
    amount_d = models.FloatField(blank=True, null=True)
    DIS_d = models.FloatField(blank=True, null=True)
    DIS_Amount_d = models.FloatField(blank=True, null=True)
    total_value_d = models.FloatField(blank=True, null=True)
    currency = models.CharField(max_length=30, blank=True, null=True)
    tag_price_d = models.FloatField()
    rate_d = models.FloatField(blank=True, null=True)
    salesapprovalstatus_d = models.BooleanField(default=False)
    comment = models.TextField(max_length=3000, blank=True, null=True)
    def __str__(self):
        return self.stockid



class cloneInvofdiamond(models.Model):
    stockid = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    shape = models.CharField(max_length=30)
    clarity = models.CharField(max_length=30)
    color_origin1 = models.CharField(max_length=30)
    white_color_grade1 = models.CharField(max_length=30)
    fancy_color_intensity1 = models.CharField(max_length=30)
    fancycolor_grade = models.CharField(max_length=30)
    cut = models.CharField(max_length=30)
    polish = models.CharField(max_length=30)
    symmetry = models.CharField(max_length=30)
    measurements = models.CharField(max_length=30,blank=True,null=True)
    depth = models.FloatField(null=True, blank=True)
    table = models.FloatField(null=True, blank=True)
    fluorescence_intensity = models.CharField(max_length=30)
    fluorescence_color = models.CharField(max_length=30)
    certificate_no_d = models.CharField(max_length=30)
    certificate_d = models.CharField(max_length=30)
    laser_inscription = models.CharField(max_length=30)
    PCS_d = models.IntegerField(null=True, blank=True)
    weight_d = models.FloatField(null=True, blank=True)
    units = models.CharField(max_length=30,blank=True,null=True)
    amount_d = models.FloatField(blank=True, null=True)
    DIS_d = models.FloatField(blank=True, null=True)
    DIS_Amount_d = models.FloatField(blank=True, null=True)
    total_value_d = models.FloatField(blank=True, null=True)
    currency = models.CharField(max_length=30, blank=True, null=True)
    tag_price_d = models.FloatField()
    rate_d = models.FloatField(blank=True, null=True)
    salesapprovalstatus_d = models.BooleanField(default=False)
    price = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):

        super(cloneInvofdiamond, self).save()


class Salesreturn_d(models.Model):
    date = models.DateField(auto_now_add=True)
    stockid = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    shape = models.CharField(max_length=30)

# purchase of Colour Stones

class Origin_cs(models.Model):
    org = models.CharField(max_length=30)

    def __str__(self):
        return self.org.title()
    def save(self, *args, **kwargs):
        self.org = self.org.lower()
        super(Origin_cs, self).save(*args, **kwargs)

class Lab_cs(models.Model):
    lab = models.CharField(max_length=20)
    def __str__(self):
        return self.lab.title()
    def save(self, *args, **kwargs):
        self.lab= self.lab.lower()
        super(Lab_cs, self).save(*args, **kwargs)

class Treatment_cs(models.Model):
    treatment = models.CharField(max_length=30)

    def __str__(self):
        return self.treatment.title()
    def save(self, *args, **kwargs):
        self.treatment = self.treatment.lower()
        super(Treatment_cs, self).save(*args, **kwargs)

class shape_cs(models.Model):
    shape = models.CharField(max_length=30)

    def __str__(self):
        return self.shape.title()
    def save(self, *args, **kwargs):
        self.shape = self.shape.lower()
        super(shape_cs, self).save(*args, **kwargs)

class cert_no_cs(models.Model):
    cert = models.CharField(max_length=30)

    def __str__(self):
        return self.cert
    def save(self, *args, **kwargs):
        self.cert = self.cert.lower()
        super(cert_no_cs, self).save(*args, **kwargs)

class PurchaseOfColorStones(models.Model):
    date = models.DateField()
    # stockid = models.CharField(max_length=30, blank=True)
    company_name = models.ForeignKey('CompanyInfo', on_delete=PROTECT)
    location = models.ForeignKey('location', on_delete=models.PROTECT, null=True)
    shape = models.ForeignKey(
        'shape_cs', on_delete=models.PROTECT, blank=True)
    gem_type = models.ForeignKey(
        'gemtype', on_delete=models.PROTECT, blank=True)
    origin = models.ForeignKey(
        'Origin_cs', on_delete=models.PROTECT, blank=True)
    Treatment = models.ForeignKey(
        'Treatment_cs', on_delete=models.PROTECT, blank=True)
    Clarity = models.CharField(max_length=30,null=True,blank=True)
    certificate_no = models.CharField(max_length=30,null=True,blank=True,verbose_name="Certificate Number")
    colour = models.CharField(max_length=30)
    measurements = models.CharField(max_length=30,blank=True,null=True)
    lab = models.ForeignKey('Lab_cs', on_delete=models.PROTECT, blank=True)
    PCS = models.IntegerField()
    Weight = models.FloatField(null=True)
    Price = models.FloatField()
    units = models.CharField(max_length=30,blank=True,null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=9)
    discount = models.PositiveSmallIntegerField(blank=True, null=True)
    discount_amount = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    total_val = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    purchaseapv = models.BooleanField(default=False)
    currency = models.ForeignKey('currencies', on_delete=models.PROTECT)
    tag_price = models.FloatField()
    rate = models.FloatField(null=True,blank=True)

    #comment Field
    comment = models.TextField(max_length=3000, blank=True, null=True, default="")

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        # self.amount = (self.Price * self.Weight)
        # self.discount_amount = (self.amount * self.discount) // 100
        self.stockid = str(str('C-')+str(self.id))
        # self.total_value_c_s = self.amount-self.discount_amount
        super(PurchaseOfColorStones, self).save(*args, **kwargs)
        obj1 = Inventoryofcolorstones.objects.create(stockid=str('C-')+str(self.id), location=self.location, shape=self.shape,
                                                     Clarity=self.Clarity, PCS=self.PCS, gem_type=self.gem_type, Weight=self.Weight, origin=self.origin, treatment=self.Treatment, certificate_no=self.certificate_no, color=self.colour, measurements=self.measurements, lab=self.lab.lab, tag_price=self.tag_price, purchaseapv=self.purchaseapv)


class Inventoryofcolorstones(models.Model):
    stockid = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=30)
    shape = models.CharField(max_length=30)
    gem_type = models.CharField(max_length=30)
    origin = models.CharField(max_length=30)
    treatment = models.CharField(max_length=30)
    Clarity = models.CharField(max_length=30,null=True,blank=True)
    certificate_no = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    measurements = models.CharField(max_length=30,blank=True,null=True)
    lab = models.CharField(max_length=30)
    PCS = models.IntegerField(null=True)
    Weight = models.FloatField(null=True)
    tag_price = models.FloatField(null=True)
    status = models.BooleanField(default=False)
    purchaseapv = models.BooleanField(blank=True)
    appvreturnstatus = models.BooleanField(default=False)
    cartstatus = models.BooleanField(default=False)
    frontend = models.BooleanField(default=False)
    def __str__(self):
        return str(self.stockid)


class Salesofcolorstones(models.Model):
    date = models.DateField(auto_now_add=False, verbose_name="Date of transaction")
    stockid = models.CharField(max_length=30, verbose_name="Stock ID")
    company_name = models.CharField(max_length=30, verbose_name="Company name")
    location = models.CharField(max_length=30, verbose_name="Location")
    shape = models.CharField(max_length=30, verbose_name="Shape")
    gem_type = models.CharField(max_length=30,verbose_name="Gem Type")
    origin = models.CharField(max_length=30, verbose_name="Origin")
    treatment = models.CharField(max_length=30, verbose_name="Treatment")
    Clarity = models.CharField(max_length=30,null=True,blank=True, verbose_name="Clarity")
    certificate_no = models.CharField(max_length=30, verbose_name="Certificate No.")
    color = models.CharField(max_length=30, verbose_name="Color")
    measurements = models.CharField(max_length=30,blank=True,null=True, verbose_name="Measurement")
    lab = models.CharField(max_length=30, verbose_name="Lab")
    PCS = models.IntegerField(verbose_name="Pieces")
    Weight_cs = models.FloatField(verbose_name="Weight")
    price=models.FloatField(default=0)
    units_cs=models.CharField(max_length=30,default="")
    amount_cs = models.FloatField(verbose_name="Amount")
    DIS_cs = models.FloatField(verbose_name="Discount Percentage")
    DIS_amount_cs = models.FloatField(verbose_name="Discount Amount")
    total_value_cs = models.FloatField(verbose_name="Total Value")
    currency_cs = models.CharField(max_length=30, verbose_name="Currency")
    tag_price_cs = models.FloatField(verbose_name="Tag Price")
    rate_cs = models.FloatField(verbose_name="Rate", default=1)
    salesapprovalstatus_cs = models.BooleanField(default=False, verbose_name="Sold")
    comment = models.TextField(max_length=3000, blank=True,null=True, verbose_name="Comment")


    
class cloneInvofcolorstones(models.Model):
    date = models.DateField(auto_now_add=True)
    stockid = models.CharField(max_length=30, blank=True,verbose_name="Stock ID")
    company_name = models.CharField(max_length=30,verbose_name="Company Name")
    location = models.CharField(max_length=30,verbose_name="Location")
    shape = models.CharField(max_length=30,verbose_name="Shape")
    gem_type = models.CharField(max_length=30)
    # weight = models.IntegerField()
    origin = models.CharField(max_length=30)
    treatment = models.CharField(max_length=30)
    Clarity = models.CharField(max_length=30,null=True,blank=True)
    certificate_no = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    measurements = models.CharField(max_length=30,blank=True,null=True)
    lab = models.CharField(max_length=30)
    PCS = models.IntegerField(null=True,verbose_name="Pieces")
    Weight_cs = models.FloatField(null=True,verbose_name="Weight")
    price=models.FloatField(null=True, blank=True)
    units_cs=models.CharField(max_length=30,null=True, blank=True,verbose_name="Units")
    amount_cs = models.FloatField(blank=True, null=True,verbose_name="Amount Per CTS")
    DIS_cs = models.FloatField(blank=True, null=True,verbose_name="Discount in %")
    DIS_amount_cs = models.FloatField(blank=True, null=True,verbose_name="Discounted Amount")
    total_value_cs = models.FloatField(blank=True, null=True,verbose_name="Total Value")
    currency_cs = models.ForeignKey(currencies, on_delete=models.PROTECT, null=True, blank=True,verbose_name="Currency")
    tag_price_cs = models.FloatField(null=True,verbose_name="Tag Price")
    rate_cs = models.FloatField(blank=True, null=True,verbose_name="Rate",default=1)
    salesapprovalstatus_cs = models.BooleanField(default=False)


    def save(self, *args, **kwargs):

        # self.delete()

        # new_obj = Salesofcolorstones.objects.create(stockid=str('C-')+str(self.id),company_name=self.company_name, location=self.location,
        #                                            shape=self.shape,gem_type=self.gem_type,origin=self.origin,treatment=self.treatment, clarity=self.clarity,certificate_no_cs=self.certificate_no, color=self.color,measurement=self.measurements,lab=self.lab,pcs=self.PCS,weight=self.weight,price=self.price,
        #                                           units=self.units,amount=self.amount,DIS=self.DIS,DIS_amount=self.DIS_amount,total_value=self.total_value,currency=self.currency, tag_price=self.tag_price,
        #                                           rate=self.rate,salesapprovalstatus=self.salesapprovalstatus)
        super(cloneInvofcolorstones, self).save()


class Salesreturn_cs(models.Model):
    date = models.DateField(auto_now_add=True)
    stockid = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    gem_type = models.CharField(max_length=30)
    weight = models.FloatField(null=True)
    tag_price_cs = models.FloatField(null=True)


class Jewel_media(models.Model):
    jewel_object = models.ForeignKey(Inventoryofjewellery, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to="JewelleryMedia/", blank=True, null=True)
    image2 = models.ImageField(upload_to="JewelleryMedia/", blank=True, null=True)
    image3 = models.ImageField(upload_to="JewelleryMedia/", blank=True, null=True)
    image4 = models.ImageField(upload_to="JewelleryMedia/", blank=True, null=True)
    image5 = models.ImageField(upload_to="JewelleryMedia/", blank=True, null=True)
    image6 = models.ImageField(upload_to="JewelleryMedia/", blank=True, null=True)
    image7 = models.ImageField(upload_to="JewelleryMedia/", blank=True, null=True)
    image8 = models.ImageField(upload_to="JewelleryMedia/", blank=True, null=True)
    image9 = models.ImageField(upload_to="JewelleryMedia/", blank=True, null=True)
    image10 = models.ImageField(upload_to="JewelleryMedia/", blank=True, null=True)
    video_embed_link = models.TextField(null=True, blank=True)
    certificate  = models.FileField(upload_to="Certificates/Jewellery/", blank =True, null=True)



class ColorStone_media(models.Model):
    class Meta:
        verbose_name_plural = "ColorStone Media"
    stockid = models.ForeignKey(Inventoryofcolorstones, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to="ColorStoneMedia/", blank=True, null=True)
    image2 = models.ImageField(upload_to="ColorStoneMedia/", blank=True, null=True)
    image3 = models.ImageField(upload_to="ColorStoneMedia/", blank=True, null=True)
    image4 = models.ImageField(upload_to="ColorStoneMedia/", blank=True, null=True)
    image5 = models.ImageField(upload_to="ColorStoneMedia/", blank=True, null=True)
    image6 = models.ImageField(upload_to="ColorStoneMedia/", blank=True, null=True)
    image7 = models.ImageField(upload_to="ColorStoneMedia/", blank=True, null=True)
    image8 = models.ImageField(upload_to="ColorStoneMedia/", blank=True, null=True)
    image9 = models.ImageField(upload_to="ColorStoneMedia/", blank=True, null=True)
    image10 = models.ImageField(upload_to="ColorStoneMedia/", blank=True, null=True)
    video_embed_link = models.TextField(null=True, blank=True)
    certificate  = models.FileField(upload_to="Certificates/ColorStone/", blank =True, null=True)

