
from typing import Sequence
from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import DateTimeCheckMixin, DecimalField
from django.db.models.fields.related import ForeignKey
from django.core.validators import DecimalValidator, RegexValidator
from tinymce.models import HTMLField
import datetime
from decimal import Decimal
from phonenumber_field.modelfields import PhoneNumberField


class State(models.Model):
    country = models.ForeignKey('countries', on_delete=models.PROTECT)
    state = models.CharField(max_length=30)

    def __str__(self):
        return self.state


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


class Blog(models.Model):
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="profile/", blank=True, null=True)
    title = models.CharField(max_length=30)
    subject = HTMLField(blank=True, null=True)

    def __str__(self):
        return (self.title)


class countries(models.Model):
    class Meta:
        verbose_name_plural = "Countries"
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.country.title()

    def save(self, *args, **kwargs):
        self.country = self.country.lower()
        super(countries, self).save(*args, **kwargs)


class location(models.Model):
    place = models.CharField(max_length=30)

    def __str__(self):
        return self.place.title()

    def save(self, *args, **kwargs):
        self.place = self.place.lower()
        super(location, self).save(*args, **kwargs)


class gemtype(models.Model):
    class Meta:
        verbose_name_plural = "ColourStone - Gem"

    gem = models.CharField(max_length=50)

    def __str__(self):
        return self.gem.title()

    def save(self, *args, **kwargs):
        self.gem = self.gem.lower()
        super(gemtype, self).save(*args, **kwargs)


class companyinfo(models.Model):
    class Meta:
        verbose_name_plural = "Company Details"
    date = models.DateField(auto_now_add=True)
    company_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    address = models.TextField()
    country = models.ForeignKey(countries, on_delete=models.PROTECT)
    mobile_no = models.CharField(max_length=20)
    tel_no = models.CharField(max_length=20, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.EmailField(max_length=150, blank=True, null=True)
    pan_no = models.CharField(max_length=20, blank=True, null=True)
    GST_no = models.CharField(max_length=20, blank=True, null=True)
    line_id = models.CharField(max_length=20, blank=True, null=True)
    wechat_id = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.company_name.title()

    def save(self, *args, **kwargs):
        self.company_name = self.company_name.lower()
        super(companyinfo, self).save(*args, **kwargs)


class jewell(models.Model):
    jewel = models.CharField(max_length=30)

    def __str__(self):
        return self.jewel.title()

    def save(self, *args, **kwargs):
        self.jewel = self.jewel.lower()
        super(jewell, self).save(*args, **kwargs)


class centerstone(models.Model):
    stone = models.CharField(max_length=30)

    def __str__(self):
        return self.stone.title()

    def save(self, *args, **kwargs):
        self.stone = self.stone.lower()
        super(centerstone, self).save(*args, **kwargs)


class colorofcstone(models.Model):
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.color.title()

    def save(self, *args, **kwargs):
        self.color = self.color.lower()
        super(colorofcstone, self).save(*args, **kwargs)


class shape1(models.Model):
    shape = models.CharField(max_length=30)

    def __str__(self):
        return self.shape.title()

    def save(self, *args, **kwargs):
        self.shape = self.shape.lower()
        super(shape1, self).save(*args, **kwargs)


class metal1(models.Model):
    metal = models.CharField(max_length=30)

    def __str__(self):
        return self.metal.title()

    def save(self, *args, **kwargs):
        self.metal = self.metal.lower()
        super(metal1, self).save(*args, **kwargs)


class certificate(models.Model):

    class Meta:
        verbose_name_plural = "ColourStone Certificates Types"
    cert = models.CharField(max_length=30)

    def __str__(self):
        return self.cert.title()

    def save(self, *args, **kwargs):
        self.cert = self.cert.lower()
        super(certificate, self).save(*args, **kwargs)


class currencies(models.Model):
    class Meta:
        verbose_name_plural = "Currencies"
    currency = models.CharField(max_length=30)

    def __str__(self):
        return self.currency.upper()

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
        return str(self.stockid).title()


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
        return self.company_name.title()


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


class Jewel_media(models.Model):
    jewel_object = models.ForeignKey(
        Inventoryofjewellery, on_delete=models.CASCADE)
    image1 = models.ImageField(
        upload_to="JewelleryMedia/", blank=True, null=True)
    image2 = models.ImageField(
        upload_to="JewelleryMedia/", blank=True, null=True)
    image3 = models.ImageField(
        upload_to="JewelleryMedia/", blank=True, null=True)
    image4 = models.ImageField(
        upload_to="JewelleryMedia/", blank=True, null=True)
    image5 = models.ImageField(
        upload_to="JewelleryMedia/", blank=True, null=True)
    image6 = models.ImageField(
        upload_to="JewelleryMedia/", blank=True, null=True)
    image7 = models.ImageField(
        upload_to="JewelleryMedia/", blank=True, null=True)
    image8 = models.ImageField(
        upload_to="JewelleryMedia/", blank=True, null=True)
    image9 = models.ImageField(
        upload_to="JewelleryMedia/", blank=True, null=True)
    image10 = models.ImageField(
        upload_to="JewelleryMedia/", blank=True, null=True)
    video_embed_link = models.TextField(null=True, blank=True)
    certificate = models.FileField(
        upload_to="Certificates/Jewellery/", blank=True, null=True)


# purchase of diamonds

class certificate_d(models.Model):
    certd = models.CharField(max_length=30)

    def __str__(self):
        return self.certd.title()


class clarity(models.Model):
    clarity = models.CharField(max_length=30)

    def __str__(self):
        return self.clarity.title()


class color_origin(models.Model):
    class Meta:
        verbose_name_plural = "Diamonds - Color Origin"

    c_o = models.CharField(max_length=30)

    def __str__(self):
        return self.c_o.title()


class white_color_grade(models.Model):
    w_c_g = models.CharField(max_length=30)

    def __str__(self):
        return self.w_c_g.title()


class fancy_color_intensity(models.Model):
    f_c_i = models.CharField(max_length=30)

    def __str__(self):
        return self.f_c_i.title()


class fancycolor_grade(models.Model):
    f_c_grade = models.CharField(max_length=30)

    def __str__(self):
        return self.f_c_grade.title()


class cut(models.Model):
    cut = models.CharField(max_length=30)

    def __str__(self):
        return self.cut.title()


class polish(models.Model):
    polish = models.CharField(max_length=30)

    def __str__(self):
        return self.polish.title()


class symmetry(models.Model):
    symmetry = models.CharField(max_length=30)

    def __str__(self):
        return self.symmetry.title()


class fluorescence_intensity(models.Model):
    f_intensity = models.CharField(max_length=30)

    def __str__(self):
        return self.f_intensity.title()


class fluorescence_color(models.Model):
    f_color = models.CharField(max_length=30)

    def __str__(self):
        return self.f_color.title()


class shape_d(models.Model):
    shape = models.CharField(max_length=30)

    def __str__(self):
        return self.shape


class POD(models.Model):
    date = models.DateField(auto_now_add=True)
    # stockid_d = models.CharField(max_length=30)
    company_name = models.ForeignKey('CompanyInfo', on_delete=PROTECT)
    location = models.ForeignKey(
        'location', on_delete=models.PROTECT, null=True)
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
    measurements = models.CharField(max_length=30, blank=True, null=True)
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
    units = models.CharField(max_length=30, blank=True, null=True)
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
    measurements = models.CharField(max_length=30, blank=True, null=True)
    depth = models.FloatField(null=True, blank=True)
    table = models.FloatField(null=True, blank=True)
    fluorescence_intensity = models.CharField(max_length=30)
    fluorescence_color = models.CharField(max_length=30)
    certificate_no_d = models.CharField(max_length=30)
    certificate_d = models.CharField(max_length=30)
    laser_inscription = models.CharField(max_length=30)
    PCS_d = models.IntegerField(null=True, blank=True)
    weight_d = models.FloatField(null=True, blank=True)
    units = models.CharField(max_length=30, blank=True, null=True)
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
    measurements = models.CharField(max_length=30, blank=True, null=True)
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
    units = models.CharField(max_length=30, blank=True, null=True)
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
    measurements = models.CharField(max_length=30, blank=True, null=True)
    depth = models.FloatField(null=True, blank=True)
    table = models.FloatField(null=True, blank=True)
    fluorescence_intensity = models.CharField(max_length=30)
    fluorescence_color = models.CharField(max_length=30)
    certificate_no_d = models.CharField(max_length=30)
    certificate_d = models.CharField(max_length=30)
    laser_inscription = models.CharField(max_length=30)
    PCS_d = models.IntegerField(null=True, blank=True)
    weight_d = models.FloatField(null=True, blank=True)
    units = models.CharField(max_length=30, blank=True, null=True)
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

class color_of_colorstone(models.Model):
    class Meta:
        verbose_name_plural = "ColourStone - Color"

    color = models.CharField(max_length=30)

    def __str__(self):
        return self.color.title()

    def save(self, *args, **kwargs):
        self.color = self.color.lower()
        super(color_of_colorstone, self).save(*args, **kwargs)        


class Origin_cs(models.Model):
    class Meta:
        verbose_name_plural = "ColourStone - Origin"
    org = models.CharField(max_length=30)

    def __str__(self):
        return self.org.title()

    def save(self, *args, **kwargs):
        self.org = self.org.lower()
        super(Origin_cs, self).save(*args, **kwargs)


class Lab_cs(models.Model):
    class Meta:
        verbose_name_plural = "ColourStone - Labs"
    lab = models.CharField(max_length=20)

    def __str__(self):
        return self.lab.upper()

    def save(self, *args, **kwargs):
        self.lab = self.lab.lower()
        super(Lab_cs, self).save(*args, **kwargs)


class Treatment_cs(models.Model):
    class Meta:
        verbose_name_plural = "ColourStone - Treatment"
    treatment = models.CharField(max_length=30)

    def __str__(self):
        return self.treatment.title()

    def save(self, *args, **kwargs):
        self.treatment = self.treatment.lower()
        super(Treatment_cs, self).save(*args, **kwargs)


class shape_cs(models.Model):
    class Meta:
        verbose_name_plural = "ColourStone - Shape"
    shape = models.CharField(max_length=30)

    def __str__(self):
        return self.shape.title()

    def save(self, *args, **kwargs):
        self.shape = self.shape.lower()
        super(shape_cs, self).save(*args, **kwargs)


class PurchaseOfColorStones(models.Model):
    date = models.DateField()
    # stockid = models.CharField(max_length=30, blank=True)
    company_name = models.ForeignKey('CompanyInfo', on_delete=PROTECT)
    location = models.ForeignKey(
        'location', on_delete=models.PROTECT, null=True)
    shape = models.ForeignKey(
        'shape_cs', on_delete=models.PROTECT, blank=True)
    gem_type = models.ForeignKey(
        'gemtype', on_delete=models.PROTECT, blank=True)
    origin = models.ForeignKey(
        'Origin_cs', on_delete=models.PROTECT, blank=True)
    Treatment = models.ForeignKey(
        'Treatment_cs', on_delete=models.PROTECT, blank=True)
    Clarity = models.CharField(max_length=30, null=True, blank=True)
    certificate_no = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="Certificate Number")
    colour = models.ForeignKey('color_of_colorstone', on_delete=models.PROTECT)
    measurements = models.CharField(max_length=30, blank=True, null=True)
    lab = models.ForeignKey('Lab_cs', on_delete=models.PROTECT, blank=True)
    PCS = models.IntegerField()
    Weight = models.FloatField(null=True)
    Price = models.FloatField()
    units = models.CharField(max_length=30, blank=True, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=9)
    discount = models.PositiveSmallIntegerField(blank=True, null=True)
    discount_amount = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    total_val = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    purchaseapv = models.BooleanField(default=False)
    currency = models.ForeignKey('currencies', on_delete=models.PROTECT)
    tag_price = models.FloatField()
    rate = models.FloatField(null=True, blank=True)

    # comment Field
    comment = models.TextField(
        max_length=3000, blank=True, null=True, default="")

    def __str__(self):
        return str("C-" + str(self.id))

    def save(self, *args, **kwargs):
        # self.amount = (self.Price * self.Weight)
        # self.discount_amount = (self.amount * self.discount) // 100
        self.stockid = str(str('C-')+str(self.id))
        # self.total_value_c_s = self.amount-self.discount_amount
        super(PurchaseOfColorStones, self).save(*args, **kwargs)
        obj1 = Inventoryofcolorstones.objects.create(stockid=str('C-')+str(self.id), location=self.location, shape=self.shape,
                                                     Clarity=self.Clarity, PCS=self.PCS, gem_type=self.gem_type, Weight=self.Weight, origin=self.origin, treatment=self.Treatment, certificate_no=self.certificate_no, color=self.colour.color, measurements=self.measurements, lab=self.lab, tag_price=self.tag_price, purchaseapv=self.purchaseapv)


class Inventoryofcolorstones(models.Model):
    stockid = models.CharField(max_length=30)
    location = models.ForeignKey(
        'location', on_delete=models.PROTECT, null=True)
    shape = models.ForeignKey(
        'shape_cs', on_delete=models.PROTECT, blank=True)
    gem_type = models.ForeignKey(
        'gemtype', on_delete=models.PROTECT, blank=True)
    origin = models.ForeignKey(
        'Origin_cs', on_delete=models.PROTECT, blank=True)
    treatment = models.ForeignKey(
        'Treatment_cs', on_delete=models.PROTECT, blank=True)
    Clarity = models.CharField(max_length=30, null=True, blank=True)
    certificate_no = models.CharField(max_length=30)
    color = models.ForeignKey('color_of_colorstone', on_delete=models.PROTECT)
    measurements = models.CharField(max_length=30, blank=True, null=True)
    lab = models.ForeignKey('Lab_cs', on_delete=models.PROTECT, blank=True)
    PCS = models.IntegerField(null=True)
    Weight = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True, verbose_name="Weight")
    tag_price = models.FloatField(null=True)
    status = models.BooleanField(default=False)
    purchaseapv = models.BooleanField(blank=True)
    appvreturnstatus = models.BooleanField(default=False)
    cartstatus = models.BooleanField(default=False)
    frontend = models.BooleanField(default=False)

    def __str__(self):
        return str(self.stockid)


class Salesofcolorstones(models.Model):
    class Meta:
        verbose_name_plural = "ColourStone - Sales"
    date = models.DateField(
        auto_now_add=False, verbose_name="Date of transaction")
    stockid = models.CharField(max_length=30)
    company_name = models.ForeignKey('CompanyInfo', on_delete=PROTECT)
    location = models.ForeignKey(
        'location', on_delete=models.PROTECT, null=True)
    shape = models.ForeignKey(
        'shape_cs', on_delete=models.PROTECT, blank=True)
    gem_type = models.ForeignKey(
        'gemtype', on_delete=models.PROTECT, blank=True)
    origin = models.ForeignKey(
        'Origin_cs', on_delete=models.PROTECT, blank=True)
    treatment = models.ForeignKey(
        'Treatment_cs', on_delete=models.PROTECT, blank=True)
    Clarity = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="Clarity")
    certificate_no = models.CharField(
        max_length=30, verbose_name="Certificate No.")
    color = models.ForeignKey('color_of_colorstone', on_delete=models.PROTECT)
    measurements = models.CharField(
        max_length=30, blank=True, null=True, verbose_name="Measurement")
    lab = models.ForeignKey('Lab_cs', on_delete=models.PROTECT, blank=True)
    PCS = models.IntegerField(verbose_name="Pieces")
    Weight_cs = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True, verbose_name="Weight")
    price = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    units_cs = models.CharField(max_length=30, default="")
    amount_cs = models.DecimalField(
        verbose_name="Amount", null=True, blank=True, decimal_places=2, max_digits=9)
    DIS_cs = models.DecimalField(
        verbose_name="Discount Percentage", null=True, blank=True, decimal_places=2, max_digits=9)
    DIS_amount_cs = models.DecimalField(
        verbose_name="Discount Amount", null=True, blank=True, decimal_places=2, max_digits=9)
    total_value_cs = models.DecimalField(
        verbose_name="Total Value", null=True, blank=True, decimal_places=2, max_digits=9)
    currency_cs = models.ForeignKey(
        currencies, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Currency")
    tag_price_cs = models.DecimalField(
        verbose_name="Tag Price", decimal_places=2, max_digits=9)
    rate_cs = models.DecimalField(
        verbose_name="Rate", default=1, decimal_places=2, max_digits=9)
    salesapprovalstatus_cs = models.BooleanField(
        default=False, verbose_name="Sold")
    comment = models.TextField(
        max_length=3000, blank=True, null=True, verbose_name="Comment")

    def save(self, *args, **kwargs):
        self.amount_cs = Decimal(self.Weight_cs) * self.price
        self.DIS_amount_cs = (self.amount_cs * self.DIS_cs)//100
        self.total_value_cs = self.amount_cs - self.DIS_amount_cs
        super(Salesofcolorstones, self).save(*args, **kwargs)


class cloneInvofcolorstones(models.Model):
    date = models.DateField(auto_now_add=True)
    stockid = models.CharField(max_length=30)
    company_name = models.ForeignKey(
        companyinfo, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Company")
    location = models.ForeignKey(
        'location', on_delete=models.PROTECT, null=True)
    shape = models.ForeignKey(
        'shape_cs', on_delete=models.PROTECT, blank=True)
    gem_type = models.ForeignKey(
        'gemtype', on_delete=models.PROTECT, blank=True)
    origin = models.ForeignKey(
        'Origin_cs', on_delete=models.PROTECT, blank=True)
    treatment = models.ForeignKey(
        'Treatment_cs', on_delete=models.PROTECT, blank=True)
    Clarity = models.CharField(max_length=30, null=True, blank=True)
    certificate_no = models.CharField(max_length=30)
    color = models.ForeignKey('color_of_colorstone', on_delete=models.PROTECT)
    measurements = models.CharField(max_length=30, blank=True, null=True)
    lab = models.ForeignKey('Lab_cs', on_delete=models.PROTECT, blank=True)
    PCS = models.IntegerField(null=True, verbose_name="Pieces")
    Weight_cs = models.FloatField(null=True, verbose_name="Weight")
    price = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=9)
    units_cs = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="Units")
    amount_cs = models.DecimalField(
        blank=True, null=True, verbose_name="Amount Per CTS", decimal_places=2, max_digits=9)
    DIS_cs = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True, verbose_name="Discount in %")
    DIS_amount_cs = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True, verbose_name="Discounted Amount")
    total_value_cs = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True, verbose_name="Total Value")
    currency_cs = models.ForeignKey(
        currencies, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Currency")
    tag_price_cs = models.DecimalField(
        decimal_places=2, max_digits=9, null=True, verbose_name="Tag Price")
    rate_cs = models.DecimalField(
        blank=True, null=True, verbose_name="Rate", default=1, decimal_places=2, max_digits=9)
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
    location = models.ForeignKey(
        'location', on_delete=models.PROTECT, null=True, blank=True)
    gem_type = models.ForeignKey(
        'gemtype', on_delete=models.PROTECT, blank=True)
    weight = models.FloatField(null=True)
    tag_price_cs = models.FloatField(null=True)


class ColorStone_media(models.Model):
    class Meta:
        verbose_name_plural = "ColourStone - Media"
    stockid = models.ForeignKey(
        Inventoryofcolorstones, on_delete=models.CASCADE)
    image1 = models.ImageField(
        upload_to="ColorStoneMedia/", blank=True, null=True)
    image2 = models.ImageField(
        upload_to="ColorStoneMedia/", blank=True, null=True)
    image3 = models.ImageField(
        upload_to="ColorStoneMedia/", blank=True, null=True)
    image4 = models.ImageField(
        upload_to="ColorStoneMedia/", blank=True, null=True)
    image5 = models.ImageField(
        upload_to="ColorStoneMedia/", blank=True, null=True)
    image6 = models.ImageField(
        upload_to="ColorStoneMedia/", blank=True, null=True)
    image7 = models.ImageField(
        upload_to="ColorStoneMedia/", blank=True, null=True)
    image8 = models.ImageField(
        upload_to="ColorStoneMedia/", blank=True, null=True)
    image9 = models.ImageField(
        upload_to="ColorStoneMedia/", blank=True, null=True)
    image10 = models.ImageField(
        upload_to="ColorStoneMedia/", blank=True, null=True)
    video_embed_link = models.TextField(null=True, blank=True)
    certificate = models.FileField(
        upload_to="Certificates/ColorStone/", blank=True, null=True)
