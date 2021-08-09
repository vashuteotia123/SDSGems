
from typing import Sequence
from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields.related import ForeignKey
from django.core.validators import RegexValidator


# Create your models here.
class Database(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)


class countries(models.Model):
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.country


class loc(models.Model):
    place = models.CharField(max_length=30)

    def __str__(self):
        return self.place


class currencies(models.Model):
    curr = models.CharField(max_length=10)

    def __str__(self):
        return self.curr


class gemtype(models.Model):
    gem = models.CharField(max_length=50)

    def __str__(self):
        return self.gem


class companyinfo(models.Model):
    date = models.DateField(auto_now_add=True)
    company_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    address = models.TextField()
    country = models.ForeignKey(countries, on_delete=models.PROTECT)
    mobile_no = models.CharField(max_length=20)
    tel_no = models.CharField(max_length=20, null=True)
    email = models.EmailField()
    website = models.EmailField(max_length=150)
    pan_no = models.CharField(max_length=20)
    GST_no = models.CharField(max_length=20)
    line_id = models.CharField(max_length=20)
    wechat_id = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name


class jewell(models.Model):
    jewel = models.CharField(max_length=30)

    def __str__(self):
        return self.jewel


class centerstone(models.Model):
    stone = models.CharField(max_length=30)

    def __str__(self):
        return self.stone


class colorofcstone(models.Model):
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.color


class shape1(models.Model):
    shape = models.CharField(max_length=30)

    def __str__(self):
        return self.shape


class metal1(models.Model):
    metal = models.CharField(max_length=30)

    def __str__(self):
        return self.metal


class certificate(models.Model):
    cert = models.CharField(max_length=30)

    def __str__(self):
        return self.cert


class currencies(models.Model):
    country = models.ForeignKey('countries', on_delete=models.PROTECT)
    currency = models.CharField(max_length=30)

    def __str__(self):
        return self.currency


class POJ(models.Model):

    date = models.DateField(auto_now_add=True)
    # stockid = models.CharField(max_length=30,blank=True)
    company_name = models.ForeignKey(
        'companyinfo', on_delete=PROTECT, blank=True)
    location = models.ForeignKey(
        'loc', on_delete=models.PROTECT, null=True, blank=True)
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
    discount_amount = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    discount = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True)
    total = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True)
    purchase_approval=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        
        self.discount_amount = (self.amount * self.discount) // 100
        # self.stockid=str(str('J-')+str(self.id))
        self.total = self.amount-self.discount_amount
        super(POJ, self).save(*args, **kwargs)
        obj = Inventoryofjewellery.objects.create(stockid=str('J-')+str(self.id), location=self.location, jewellery_type=self.jewellery, center_stone=self.center_stone,
                                                  color_of_center_stone=self.color_of_center_stone, shape=self.shape,
                                                  metal=self.metal, grosswt=self.grosswt, cert=self.cert, pcs=self.pcs, tag_price=self.tag_price,
                                                  purchaseapv=self.purchase_approval)
    currencyid = models.ForeignKey('currencies', on_delete=models.PROTECT, null=True, blank=True)
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
    purchaseapv=models.BooleanField(blank=True)
    status=models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)


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
    location = models.ForeignKey('loc', on_delete=models.PROTECT, null=True)
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
    measurements = models.IntegerField()
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
    price = models.FloatField()
    units = models.IntegerField()
    amount_d = models.DecimalField(decimal_places=2, max_digits=9)
    DIS_Amount = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    DIS_d = models.PositiveSmallIntegerField(blank=True, null=True)

    total_val_d = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True)
    purchaseapvd= models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        self.amount_d = (self.price * self.units* self.PCS_d) 
        self.DIS_Amount = (self.amount_d * self.DIS_d) // 100
        self.total_val_d = self.amount_d - self.DIS_Amount
        super(POD, self).save(*args, **kwargs)
        obj2=Inventoryofdiamond.objects.create(stockid=str('D-')+str(self.id),location=self.location,shape=self.shape,
        clarity=self.clarity, white_color_grade= self.white_color_grade1,fancy_color_intensity=self.fancy_color_intensity1,
        fancy_color_grade=self.fancycolor_grade,cut=self.cut,weight=self.weight_d,polish=self.polish,symmetry=self.symmetry,measurements=self.measurements,
        depth=self.depth,table=self.table_perc,fluorescence_intensity=self.fluorescence_intensity,fluorescence_color=self.fluorescence_color,certificate_no=self.certificate_no_d,
        certificate=self.certificate_d,laser_inscription=self.laser_inscription ,PCS=self.PCS_d,tag_price=self.tag_price_d,purchase_approval_d=self.purchaseapvd)
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
    white_color_grade = models.CharField(max_length=30)
    fancy_color_intensity = models.CharField(max_length=30)
    fancy_color_grade = models.CharField(max_length=30)
    weight = models.FloatField()
    cut = models.CharField(max_length=30)
    polish = models.CharField(max_length=30)
    symmetry = models.CharField(max_length=30)
    measurements = models.FloatField()
    depth = models.FloatField()
    table = models.FloatField()
    fluorescence_intensity = models.CharField(max_length=30)
    fluorescence_color = models.CharField(max_length=30)
    certificate_no = models.CharField(max_length=30)
    certificate = models.CharField(max_length=30)
    laser_inscription = models.CharField(max_length=30)
    PCS = models.IntegerField()
    tag_price = models.FloatField()
    status = models.BooleanField(default=False)
    purchase_approval_d=models.BooleanField(blank=True)

# purchase of Colour Stones

class Origin_cs(models.Model):
    org = models.CharField(max_length=30)

    def __str__(self):
        return self.org


class Lab_cs(models.Model):
    lab = models.CharField(max_length=20)

    def __str__(self):
        return self.lab


class Treatment_cs(models.Model):
    treat = models.CharField(max_length=20)

    def __str__(self):
        return self.treat


class shape_cs(models.Model):
    shape = models.CharField(max_length=30)

    def __str__(self):
        return self.shape


class certificate_no_cs(models.Model):
    cert = models.CharField(max_length=30)

    def __str__(self):
        return self.cert


class PurchaseOfColorStones(models.Model):
    date = models.DateField(auto_now_add=True)
    stockid = models.CharField(max_length=30, blank=True)
    company_name = models.ForeignKey('CompanyInfo', on_delete=PROTECT)
    location = models.ForeignKey('loc', on_delete=models.PROTECT, null=True)
    shape_cs = models.ForeignKey(
        'shape_cs', on_delete=models.PROTECT, blank=True)
    gem_type = models.ForeignKey(
        'gemtype', on_delete=models.PROTECT, blank=True)
    origin = models.ForeignKey(
        'Origin_cs', on_delete=models.PROTECT, blank=True)
    Treatment = models.ForeignKey(
        'Treatment_cs', on_delete=models.PROTECT, blank=True)
    Clarity = models.CharField(max_length=30)
    certificate_no_cs = models.ForeignKey(
        'certificate_no_cs', on_delete=models.PROTECT, blank=True)
    colour = models.CharField(max_length=30)
    measurements = models.IntegerField()
    lab = models.ForeignKey('Lab_cs', on_delete=models.PROTECT, blank=True)
    PCS = models.IntegerField()
    Weight_cs = models.FloatField()
    Price = models.FloatField()
    units = models.IntegerField()
    amount = models.DecimalField(decimal_places=2, max_digits=9)        
    discount_amount = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    discount = models.PositiveSmallIntegerField(blank=True, null=True)
    total_val_cs = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    purchaseapvcs= models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        self.amount = (self.Price * self.units* self.PCS) 
        self.discount_amount = (self.amount * self.discount) // 100
        self.stockid = str(str('C-')+str(self.id))
        self.total_value_c_s = self.amount-self.discount_amount
        super(PurchaseOfColorStones, self).save(*args, **kwargs)
        obj1=Inventoryofcolorstones.objects.create(stockid=str('C-')+str(self.id),location=self.location,shape=self.shape_cs,
        gem_type=self.gem_type
        ,weight=self.Weight_cs,origin=self.origin,treatment=self.Treatment
        ,certificate_no_cs=self.certificate_no_cs,color=self.colour,measurements=self.measurements
        ,lab=self.lab,tag_price_cs=self.tag_price_cs,purchaseapproval_cs=self.purchaseapvcs)
    currency = models.ForeignKey('currencies', on_delete=models.PROTECT)
    tag_price_cs = models.FloatField()
    rate = models.FloatField()

    def ___str__(self):
        return str(self.id)
    
    

# inventoryofcolorstones

class Inventoryofcolorstones(models.Model):
    stockid = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=30)
    shape = models.CharField(max_length=30)
    gem_type = models.CharField(max_length=30)
    weight = models.IntegerField()
    origin = models.CharField(max_length=30)
    treatment = models.CharField(max_length=30)
    certificate_no_cs = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    measurements = models.FloatField()
    lab = models.CharField(max_length=30)
    tag_price_cs = models.FloatField()
    status = models.BooleanField(default=False)
    # def save(self, *args, **kwargs):
    #     self.stockid=str(str('C-')+str(self.id))
    #     super(Inventoryofcolorstones, self).save(*args, **kwargs)
    purchaseapproval_cs = models.BooleanField(blank=True)
    def ___str__(self):
        return str(self.id)

# class Salesofcolorstones(models.Model):
#     date=models.DateField(auto_now_add=True)
#     stockid = models.CharField(max_length=30)
#     company_name = models.CharField(max_length=30)
#     location=models.CharField(max_length=30)
#     shape = models.CharField(max_length=30)
#     gem_type = models.CharField(max_length=30)
#     origin=models.CharField(max_length=30)
#     treatment=models.CharField(max_length=30)
#     clarity=models.CharField(max_length=30)
#     certificate_no=models.CharField(max_length=30)
#     color=models.CharField(max_length=30)
#     measurements = models.FloatField()
#     lab=models.CharField(max_length=30)
#     PCS=models.IntegerField()
#     weight=models.FloatField()
#     price=models.FloatField()
#     units=models.IntegerField()
#     amount = models.FloatField()
#     DIS=models.FloatField()
#     DIS_amount=models.FloatField()
#     total_value=models.FloatField()
#     currency=models.CharField(max_length=30)
#     tag_price=models.FloatField()
#     rate=models.FloatField()

# SALE OF DIAMOND
# class Salesofdiamond(models.Model):
#     date=models.DateField(auto_now_add=True)
#     stockid = models.CharField(max_length=30)
#     company_name = models.CharField(max_length=30)
#     location=models.CharField(max_length=30)
#     shape = models.CharField(max_length=30)
#     clarity =models.CharField(max_length=30)
#     color_origin=models.CharField(max_length=30)
#     white_color_grade=models.CharField(max_length=30)
#     fancy_color_intensity=models.CharField(max_length=30)
#     overtone =models.CharField(max_length=30)
#     fancy_color_1=models.CharField(max_length=30)
#     fancy_color_2=models.CharField(max_length=30)
#     fancy_color_grade=models.CharField(max_length=30)
#     cut=models.CharField(max_length=30)
#     polish=models.CharField(max_length=30)
#     symmetry=models.CharField(max_length=30)
#     measurements = models.FloatField()
#     depth= models.FloatField()
#     table=models.FloatField()
#     fluorescence_intensity=models.CharField(max_length=30)
#     fluorescence_color=models.CharField(max_length=30)
#     certificate_no=models.CharField(max_length=30)
#     certificate=models.CharField(max_length=30)
#     laser_inscription=models.CharField(max_length=30)
#     PCS=models.IntegerField()
#     weight=models.FloatField()
#     price=models.FloatField()
#     units=models.IntegerField()
#     amount = models.FloatField()
#     DIS=models.FloatField()
#     DIS_amount=models.FloatField()
#     total_value=models.FloatField()
#     currency=models.CharField(max_length=30)
#     tag_price=models.FloatField()
#     rate=models.FloatField()

# class Salesofjewellery(models.Model):
#     date=models.DateField(auto_now_add=True)
#     stockid = models.CharField(max_length=30)
#     company_name = models.CharField(max_length=30)
#     location=models.CharField(max_length=30)
#     jewellery_type = models.CharField(max_length=30)
#     centre_stone = models.CharField(max_length=30)
#     shape=models.CharField(max_length=30)
#     metal=models.CharField(max_length=30)
#     gross_wt=models.Floatfield()
#     certificate=models.CharField(max_length=30)
#     PCS=models.Integerfield()
#     amount = models.FloatField()
#     DIS=models.FloatField()
#     DIS_amount=models.FloatField()
#     total_value=models.FloatField()
#     currency=models.CharField(max_length=30)
#     tag_price=models.FloatField()
#     rate=models.FloatField()

# class Salesapproval(models.Model):
#     date=models.DateField(auto_now_add=True)
#     stockid = models.CharField(max_length=30)
#     company_name = models.CharField(max_length=30)
#     location=models.CharField(max_length=30)
#     shape = models.CharField(max_length=30)
#     gem_type = models.CharField(max_length=30)
#     origin=models.CharField(max_length=30)
#     treatment=models.CharField(max_length=30)
#     clarity=models.Floatfield()
#     certificate=models.CharField(max_length=30)
#     color=models.CharField(max_length=30)
#     measurements=models.FloatField()
#     lab=models.Charfield(max_length=30)
#     PCS=models.Integerfield()
#     weight = models.FloatField()
#     price= models.FloatField()
#     units=models.IntegerField()
#     amount=models.FloatField()
#     DIS=models.FloatField()
#     DIS_amount=models.FloatField()
#     total_value=models.FloatField()
#     currency=models.CharField(max_length=30)
#     tag_price=models.FloatField()
#     rate=models.FloatField()
