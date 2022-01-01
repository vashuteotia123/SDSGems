
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
    class Meta:
        verbose_name_plural = "Locations"
    place = models.CharField(max_length=30)

    def __str__(self):
        return self.place.title()

    def save(self, *args, **kwargs):
        self.place = self.place.lower()
        super(location, self).save(*args, **kwargs)


class gemtype(models.Model):
    class Meta:
        verbose_name_plural = "ColourStone - Gemtype"

    gem = models.CharField(max_length=50,unique=True)

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
    class Meta:
        verbose_name_plural = "Jewellery -Type"
    jewel = models.CharField(max_length=30)

    def __str__(self):
        return self.jewel.title()

    def save(self, *args, **kwargs):
        self.jewel = self.jewel.lower()
        super(jewell, self).save(*args, **kwargs)


class centerstone(models.Model):
    class Meta:
        verbose_name_plural = "Jewellery - Center Stone"

    stone = models.CharField(max_length=30)

    def __str__(self):
        return self.stone.title()

    def save(self, *args, **kwargs):
        self.stone = self.stone.lower()
        super(centerstone, self).save(*args, **kwargs)


class colorofcstone(models.Model):
    class Meta:
        verbose_name_plural = "Jewellery - Colour of Center Stone"
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.color.title()

    def save(self, *args, **kwargs):
        self.color = self.color.lower()
        super(colorofcstone, self).save(*args, **kwargs)


class shape1(models.Model):
    class Meta:
        verbose_name_plural = "Jewellery - Shape"
    shape = models.CharField(max_length=30)

    def __str__(self):
        return self.shape.title()

    def save(self, *args, **kwargs):
        self.shape = self.shape.lower()
        super(shape1, self).save(*args, **kwargs)


class metal1(models.Model):
    class Meta:
        verbose_name_plural = "Jewellery - Metal"
    metal = models.CharField(max_length=30)

    def __str__(self):
        return self.metal.upper()

    def save(self, *args, **kwargs):
        self.metal = self.metal.lower()
        super(metal1, self).save(*args, **kwargs)


class certificate(models.Model):

    class Meta:
        verbose_name_plural = "Jewellery - Certificates Types"
    cert = models.CharField(max_length=30)

    def __str__(self):
        return self.cert.upper()

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

#yaha fir bakchodi hogi
class clonePOJ(models.Model):

    date = models.DateField()
    company_name = models.ForeignKey(
        'CompanyInfo', on_delete=PROTECT, blank=True)
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
    center_stone_weight=models.DecimalField(decimal_places=2, max_digits=9)
    center_stone_pieces=models.BigIntegerField()
    grosswt = models.DecimalField(decimal_places=2, max_digits=9)
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
    currency = models.ForeignKey(
        'currencies', on_delete=models.PROTECT, null=True, blank=True)
    tag_price = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True)
    rate = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True)
    def save(self, *args, **kwargs):
        super(clonePOJ, self).save(*args, **kwargs)
        obj = POJ.objects.create(date = self.date,company_name=self.company_name, location=self.location, jewellery=self.jewellery, center_stone=self.center_stone,
                                                  color_of_center_stone=self.color_of_center_stone, shape=self.shape,
                                                  metal=self.metal, center_stone_weight=self.center_stone_weight,center_stone_pieces=self.center_stone_pieces,
                                                  grosswt=self.grosswt, cert=self.cert, pcs=self.pcs, tag_price=self.tag_price,
                                                  purchase_approval=self.purchase_approval, amount = self.amount, discount = self.discount,
                                                  discount_amount = self.discount_amount, total = self.total, currency = self.currency, rate=self.rate)
    # salesapproval

    def __str__(self):
        return str("J-"+str(self.id))



class POJ(models.Model):
    class Meta:
        verbose_name_plural = "Jewellery - Purchases"
    date = models.DateField()
    company_name = models.ForeignKey(
        'CompanyInfo', on_delete=PROTECT, blank=True)
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
    center_stone_weight=models.DecimalField(decimal_places=2, max_digits=9)
    center_stone_pieces=models.BigIntegerField()
    grosswt = models.DecimalField(decimal_places=2, max_digits=9)
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
    currency = models.ForeignKey(
        'currencies', on_delete=models.PROTECT, null=True, blank=True)
    tag_price = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True)
    rate = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True)
    comment = models.TextField(max_length=3000, blank=True, null=True)
    def save(self, *args, **kwargs):
        super(POJ, self).save(*args, **kwargs)
        obj = Inventoryofjewellery.objects.create(stockid=str('J-')+str(self.id), location=self.location, jewellery_type=self.jewellery, center_stone=self.center_stone,
                                                  color_of_center_stone=self.color_of_center_stone, shape=self.shape,
                                                  metal=self.metal, center_stone_weight=self.center_stone_weight,center_stone_pieces=self.center_stone_pieces,
                                                  grosswt=self.grosswt, cert=self.cert, pcs=self.pcs, tag_price=self.tag_price,
                                                  purchaseapv=self.purchase_approval)
    # salesapproval

    def __str__(self):
        return str("J-"+str(self.id))


class Inventoryofjewellery(models.Model):
    class Meta:
        verbose_name_plural = "Jewellery - Inventory"
    stockid = models.CharField(max_length=30, blank=True)
    location = models.ForeignKey(
        'location', on_delete=models.PROTECT, null=True, blank=True)
    jewellery_type =models.ForeignKey(
        'jewell', on_delete=models.PROTECT, null=True, blank=True)
    center_stone = models.ForeignKey(
        'centerstone', on_delete=models.PROTECT, null=True, blank=True)
    color_of_center_stone = models.ForeignKey(
        'colorofcstone', on_delete=models.PROTECT, null=True, blank=True)
    shape = models.ForeignKey(
        'shape1', on_delete=models.PROTECT, null=True, blank=True)
    metal = models.ForeignKey(
        'metal1', on_delete=models.PROTECT, null=True, blank=True)
    center_stone_weight=models.DecimalField(decimal_places=2, max_digits=9)
    center_stone_pieces=models.BigIntegerField()
    grosswt = models.DecimalField(decimal_places=2, max_digits=9)
    cert = models.ForeignKey(
        'certificate', on_delete=models.PROTECT, null=True, blank=True)
    pcs = models.IntegerField()
    tag_price = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True)
    purchaseapv = models.BooleanField(blank=True)
    cartstatus = models.BooleanField(default=False)
    appvreturnstatus = models.BooleanField(default=False)
    frontend = models.BooleanField(default=False)

    def __str__(self):
        return str(self.stockid).title()


class Salesofjewellery(models.Model):
    class Meta:
        verbose_name_plural = "Jewellery - Sales"
    date = models.DateField(
        auto_now_add=False, verbose_name="Date of transaction")
    stockid = models.CharField(max_length=30, verbose_name="Stock ID")
    company_name = models.ForeignKey(
        'companyinfo', on_delete=PROTECT, blank=True, verbose_name="Company name")
    location = models.ForeignKey(
        'location', on_delete=models.PROTECT, null=True, verbose_name="Location")
    jewellery_type = models.ForeignKey(
        'jewell', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Jewellery Type")
    center_stone = models.ForeignKey(
        'centerstone', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Center Stone")
    color_of_center_stone = models.ForeignKey(
        'colorofcstone', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Colour of Center Stone")
    shape = models.ForeignKey(
        'shape1', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Shape")
    metal = models.ForeignKey(
        'metal1', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Metal")
    center_stone_weight=models.DecimalField(decimal_places=2, max_digits=9, verbose_name="Center Stone Weight")
    center_stone_pieces=models.BigIntegerField(verbose_name="Center Stone Pieces")
    gross_wt = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, verbose_name="Gross Weight")
    certificate = models.ForeignKey(
        'certificate', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Certificate Type")
    PCS = models.BigIntegerField(verbose_name="Pieces")
    amount =models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, verbose_name="Amount")
    DIS =models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, verbose_name="Discount %")
    DIS_amount = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, verbose_name="DISCOUNT Amount")
    total_value = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, verbose_name="Total Value")
    currency = models.ForeignKey(
        currencies, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Currency")
    tag_price = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, verbose_name="Tag Price")
    rate = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, verbose_name="Rate")
    salesapprovalstatus = models.BooleanField(default=False, verbose_name="Sold")
    comment = models.TextField(max_length=3000, blank=True, null=True, verbose_name="Comment")
    def __str__(self):
        return self.stockid
  


class cloneInvofjewellery(models.Model):
    class Meta:
        verbose_name_plural = "Jewellery - Cart"
    date=models.DateField(auto_now_add=True)
    stockid = models.CharField(max_length=30)
    company_name =models.ForeignKey(
        companyinfo, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Company")
    location = models.ForeignKey(
        'location', on_delete=models.PROTECT, null=True)
    jewellery_type = jewellery_type =models.ForeignKey(
        'jewell', on_delete=models.PROTECT, null=True, blank=True)
    center_stone = models.ForeignKey(
        'centerstone', on_delete=models.PROTECT, null=True, blank=True)
    color_of_center_stone = models.ForeignKey(
        'colorofcstone', on_delete=models.PROTECT, null=True, blank=True)
    shape = models.ForeignKey(
        'shape1', on_delete=models.PROTECT, null=True, blank=True)
    metal = models.ForeignKey(
        'metal1', on_delete=models.PROTECT, null=True, blank=True)
    center_stone_weight=models.DecimalField(decimal_places=2, max_digits=9)
    center_stone_pieces=models.BigIntegerField()
    gross_wt = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True)
    certificate = models.ForeignKey(
        'certificate', on_delete=models.PROTECT, null=True, blank=True)
    PCS = models.IntegerField()
    amount =models.DecimalField(
        decimal_places=2, max_digits=9, blank=True,null=True)
    DIS = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True,null=True)
    DIS_amount = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True,null=True)
    total_value = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True,null=True)
    currency = models.ForeignKey(
        currencies, on_delete=models.PROTECT, null=True, blank=True)
    tag_price = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True,null=True)
    rate = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True,default=1)
    salesapprovalstatus = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # new_obj = Salesofjewellery.objects.create(stockid=self.stockid, company_name=self.company_name, location=self.location, jewellery_type=self.jewellery_type,
        #                                           center_stone=self.center_stone, shape=self.shape,
        #                                           metal=self.metal, gross_wt=self.gross_wt, certificate=self.certificate, PCS=self.PCS, amount=self.amount, DIS=self.DIS, DIS_amount=self.DIS_amount, total_value=self.total_value, currency=self.currency, tag_price=self.tag_price,
        #                                           rate=self.rate, salesapprovalstatus=self.salesapprovalstatus)
        super(cloneInvofjewellery, self).save()


class Salesreturn(models.Model):
    class Meta:
        verbose_name_plural = "Jewellery - Sales Return"
    date = models.DateField(auto_now_add=True)
    stockid = models.CharField(max_length=30,blank=True, null=True,)
    company_name = models.CharField(max_length=30,blank=True, null=True,)
    location = models.CharField(max_length=30,blank=True, null=True,)
    grosswt=models.DecimalField(null=True,blank=True,decimal_places=2, max_digits=9,default=1)
    jewellery_type = models.CharField(max_length=30,blank=True, null=True,)
    total_amount=models.DecimalField(null=True,blank=True,decimal_places=2, max_digits=9,default=1)


class Jewel_media(models.Model):
    class Meta:
        verbose_name_plural = "Jewellery - Media"
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
    description = models.TextField(null=True, blank=True, max_length=5000, verbose_name="Description")
    jewellery_info = models.TextField(null=True, blank=True,  max_length=3000, verbose_name="Jewellery Information")


# purchase of diamonds

class certificate_d(models.Model):
    class Meta:
        verbose_name_plural = "Diamond - Certificates Types"
    certd = models.CharField(max_length=30)

    def __str__(self):
        return self.certd.upper()
    def save(self, *args, **kwargs):
        self.certd = self.certd.lower()
        super(certificate_d, self).save(*args, **kwargs)


class clarity(models.Model):
    class Meta:
        verbose_name_plural = "Diamond - Clarity"
    clarity = models.CharField(max_length=30)

    def __str__(self):
        return self.clarity.title()

    def save(self, *args, **kwargs):
        self.clarity = self.clarity.lower()
        super(clarity, self).save(*args, **kwargs)

class color_origin(models.Model):
    class Meta:
        verbose_name_plural = "Diamond - Colour Origin"

    c_o = models.CharField(max_length=30)

    def __str__(self):
        return self.c_o.title()
    
    def save(self, *args, **kwargs):
        self.c_o = self.c_o.lower()
        super(color_origin, self).save(*args, **kwargs)


class white_color_grade(models.Model):
    class Meta:
        verbose_name_plural = "Diamond - White Colour Grades"
    w_c_g = models.CharField(max_length=30)
    def __str__(self):
        return self.w_c_g.title()
    def save(self, *args, **kwargs):
        self.w_c_g = self.w_c_g.lower()
        super(white_color_grade, self).save(*args, **kwargs)


class fancy_color_intensity(models.Model):
    class Meta:
        verbose_name_plural = "Diamond - Fancy Color Intensities"
    f_c_i = models.CharField(max_length=30)

    def __str__(self):
        return self.f_c_i.title()

    def save(self, *args, **kwargs):
        self.f_c_i = self.f_c_i.lower()
        super(fancy_color_intensity, self).save(*args, **kwargs)
        

class fancycolor_grade(models.Model):
    class Meta:
        verbose_name_plural = "Diamond - Fancy Colour Grades"
    f_c_grade = models.CharField(max_length=30)

    def __str__(self):
        return self.f_c_grade.title()
    def save(self, *args, **kwargs):
        self.f_c_grade = self.f_c_grade.lower()
        super(fancycolor_grade, self).save(*args, **kwargs)

class cut(models.Model):
    class Meta:
        verbose_name_plural = "Diamond - Cuts"
    cut = models.CharField(max_length=30)

    def __str__(self):
        return self.cut.title()
    def save(self, *args, **kwargs):
        self.cut = self.cut.lower()
        super(cut, self).save(*args, **kwargs)


class polish(models.Model):
    class Meta:
        verbose_name_plural = "Diamond - Polishes"
    polish = models.CharField(max_length=30)

    def __str__(self):
        return self.polish.title()
    def save(self, *args, **kwargs):
        self.polish = self.polish.lower()
        super(polish, self).save(*args, **kwargs)

class symmetry(models.Model):
    class Meta:
        verbose_name_plural = "Diamond - Symmetries"
    symmetry = models.CharField(max_length=30)

    def __str__(self):
        return self.symmetry.title()
    def save(self, *args, **kwargs):
        self.symmetry = self.symmetry.lower()
        super(symmetry, self).save(*args, **kwargs)

class fluorescence_intensity(models.Model):
    class Meta:
        verbose_name_plural = "Diamond - Fluorescence Intensities"
    f_intensity = models.CharField(max_length=30)

    def __str__(self):
        return self.f_intensity.title()
    def save(self, *args, **kwargs):
        self.f_intensity = self.f_intensity.lower()
        super(fluorescence_intensity, self).save(*args, **kwargs)

class fluorescence_color(models.Model):
    class Meta:
        verbose_name_plural = "Diamond - Fluorescence Colours"
    f_color = models.CharField(max_length=30)

    def __str__(self):
        return self.f_color.title()
    def save(self, *args, **kwargs):
        self.f_color = self.f_color.lower()
        super(fluorescence_color, self).save(*args, **kwargs)

class shape_d(models.Model):
    class Meta:
        verbose_name_plural = "Diamond - Shapes"
    shape = models.CharField(max_length=30)

    def __str__(self):
        return self.shape.title()

    def save(self, *args, **kwargs):
        self.shape = self.shape.lower()
        super(shape_d, self).save(*args, **kwargs)
class clonePOD(models.Model):
    date = models.DateField()
    # stockid_d = models.CharField(max_length=30)
    company_name = models.ForeignKey('CompanyInfo', on_delete=PROTECT)
    location = models.ForeignKey(
        'location', on_delete=models.PROTECT, null=True)
    shape = models.ForeignKey('shape_d', on_delete=models.PROTECT, null=True)
    clarity = models.ForeignKey('clarity', on_delete=models.PROTECT)
    color_origin1 = models.ForeignKey('color_origin', on_delete=models.PROTECT)
    white_color_grade1 = models.ForeignKey(
        'white_color_grade', on_delete=models.PROTECT, null=True, blank=True)
    fancycolor_grade = models.CharField(max_length=100,null=True, blank=True)
    cut = models.ForeignKey('cut', on_delete=models.PROTECT)
    polish = models.ForeignKey('polish', on_delete=models.PROTECT)
    symmetry = models.ForeignKey('symmetry', on_delete=models.PROTECT)
    measurements = models.CharField(max_length=30, blank=True, null=True)
    depth = models.DecimalField(decimal_places=2, max_digits=9)
    table_perc = models.DecimalField(decimal_places=2, max_digits=9)
    fluorescence_intensity = models.ForeignKey(
        'fluorescence_intensity', on_delete=models.PROTECT)
    fluorescence_color = models.ForeignKey(
        'fluorescence_color', on_delete=models.PROTECT)
    certificate_no_d = models.CharField(max_length=30)
    certificate_d = models.ForeignKey(
        'certificate_d', on_delete=models.PROTECT)
    laser_inscription = models.BooleanField()
    PCS_d = models.IntegerField()
    weight_d = models.DecimalField(decimal_places=2, max_digits=9)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    units = models.CharField(max_length=30, blank=True, null=True)
    amount_d = models.DecimalField(decimal_places=2, max_digits=9)
    DIS_d = models.DecimalField(decimal_places=2, max_digits=9)
    DIS_Amount_d = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)

    total_val_d = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True)
    purchaseapv_d = models.BooleanField(default=False)
    currency = models.ForeignKey('currencies', on_delete=models.PROTECT)
    tag_price_d = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True)
    rate_d = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True)
    comment = models.TextField(max_length=3000, blank=True, null=True)

    def save(self, *args, **kwargs):
        # self.amount_d = (self.price * self.units * self.PCS_d)
        # self.DIS_Amount_d = (self.amount_d * self.DIS_d) // 100
        # self.total_val_d = self.amount_d - self.DIS_Amount_d
        super(clonePOD, self).save(*args, **kwargs)
        obj2 = POD.objects.create(date=self.date,company_name=self.company_name, location=self.location, shape=self.shape,color_origin1=self.color_origin1,
                                                 clarity=self.clarity, white_color_grade1=self.white_color_grade1,
                                                 fancycolor_grade=self.fancycolor_grade,cut=self.cut, weight_d=self.weight_d,  polish=self.polish, symmetry=self.symmetry, measurements=self.measurements,
                                                 price=self.price,depth=self.depth, table_perc=self.table_perc, fluorescence_intensity=self.fluorescence_intensity, fluorescence_color=self.fluorescence_color, certificate_no_d=self.certificate_no_d,
                                                 certificate_d=self.certificate_d, units=self.units, laser_inscription=self.laser_inscription, PCS_d=self.PCS_d, tag_price_d=self.tag_price_d, purchaseapv_d=self.purchaseapv_d,rate_d=self.rate_d,
                                                amount_d=self.amount_d,DIS_d=self.DIS_d,DIS_Amount_d=self.DIS_Amount_d,total_val_d=self.total_val_d,currency=self.currency,)
    

    def __str__(self):
        return str(self.id)


class POD(models.Model):
    class Meta:
        verbose_name_plural = "Diamond - Purchase"
    date = models.DateField()
    # stockid_d = models.CharField(max_length=30)
    company_name = models.ForeignKey('CompanyInfo', on_delete=PROTECT)
    location = models.ForeignKey(
        'location', on_delete=models.PROTECT, null=True)
    shape = models.ForeignKey('shape_d', on_delete=models.PROTECT, null=True)
    clarity = models.ForeignKey('clarity', on_delete=models.PROTECT)
    color_origin1 = models.ForeignKey('color_origin', on_delete=models.PROTECT)
    white_color_grade1 = models.ForeignKey(
        'white_color_grade', on_delete=models.PROTECT, null=True, blank=True)
    fancycolor_grade = models.CharField(max_length=100,null=True, blank=True)
    cut = models.ForeignKey('cut', on_delete=models.PROTECT)
    polish = models.ForeignKey('polish', on_delete=models.PROTECT)
    symmetry = models.ForeignKey('symmetry', on_delete=models.PROTECT)
    measurements = models.CharField(max_length=30, blank=True, null=True)
    depth = models.DecimalField(decimal_places=2, max_digits=9)
    table_perc = models.DecimalField(decimal_places=2, max_digits=9)
    fluorescence_intensity = models.ForeignKey(
        'fluorescence_intensity', on_delete=models.PROTECT)
    fluorescence_color = models.ForeignKey(
        'fluorescence_color', on_delete=models.PROTECT)
    certificate_no_d = models.CharField(max_length=30)
    certificate_d = models.ForeignKey(
        'certificate_d', on_delete=models.PROTECT)
    laser_inscription = models.BooleanField()
    PCS_d = models.IntegerField()
    weight_d = models.DecimalField(decimal_places=2, max_digits=9)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    units = models.CharField(max_length=30, blank=True, null=True)
    amount_d = models.DecimalField(decimal_places=2, max_digits=9)
    DIS_d = models.DecimalField(decimal_places=2, max_digits=9)
    DIS_Amount_d = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)

    total_val_d = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True)
    purchaseapv_d = models.BooleanField(default=False)
    currency = models.ForeignKey('currencies', on_delete=models.PROTECT)
    tag_price_d = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True)
    rate_d = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True)
    comment = models.TextField(max_length=3000, blank=True, null=True)

    def save(self, *args, **kwargs):
        # self.amount_d = (self.price * self.units * self.PCS_d)
        # self.DIS_Amount_d = (self.amount_d * self.DIS_d) // 100
        # self.total_val_d = self.amount_d - self.DIS_Amount_d
        super(POD, self).save(*args, **kwargs)
        obj2 = Inventoryofdiamond.objects.create(stockid=str('D-')+str(self.id), location=self.location, shape=self.shape,color_origin1=self.color_origin1,
                                                 clarity=self.clarity, white_color_grade1=self.white_color_grade1,
                                                 fancycolor_grade=self.fancycolor_grade,cut=self.cut, weight_d=self.weight_d,  polish=self.polish, symmetry=self.symmetry, measurements=self.measurements,
                                                 depth=self.depth, table=self.table_perc, fluorescence_intensity=self.fluorescence_intensity, fluorescence_color=self.fluorescence_color, certificate_no_d=self.certificate_no_d,
                                                 certificate_d=self.certificate_d, units=self.units, laser_inscription=self.laser_inscription, PCS_d=self.PCS_d, tag_price_d=self.tag_price_d, purchaseapv_d=self.purchaseapv_d)
    

    def __str__(self):
        return str(self.id)

# Inventory of Diamond


class Inventoryofdiamond(models.Model):
    class Meta:
        verbose_name_plural = "Diamond - Inventory"
    stockid = models.CharField(max_length=30)
    location = models.ForeignKey(
        'location', on_delete=models.PROTECT, null=True)
    shape = models.ForeignKey('shape_d', on_delete=models.PROTECT, null=True)
    clarity = models.ForeignKey('clarity', on_delete=models.PROTECT)
    color_origin1 = models.ForeignKey('color_origin', on_delete=models.PROTECT)
    white_color_grade1 = models.ForeignKey('white_color_grade', on_delete=models.PROTECT, null=True, blank=True)
    fancycolor_grade = models.CharField(max_length=100,null=True, blank=True)
    cut = models.ForeignKey('cut', on_delete=models.PROTECT) 
    polish = models.ForeignKey('polish', on_delete=models.PROTECT)
    symmetry = models.ForeignKey('symmetry', on_delete=models.PROTECT)
    measurements = models.CharField(max_length=30, blank=True, null=True)
    depth = models.DecimalField(decimal_places=2, max_digits=9)
    table = models.DecimalField(decimal_places=2, max_digits=9)
    fluorescence_intensity = models.ForeignKey('fluorescence_intensity', on_delete=models.PROTECT)
    fluorescence_color = models.ForeignKey('fluorescence_color', on_delete=models.PROTECT)
    certificate_no_d = models.CharField(max_length=30)
    certificate_d = models.ForeignKey('certificate_d', on_delete=models.PROTECT)
    laser_inscription = models.BooleanField()
    PCS_d = models.IntegerField(null=True, blank=True,verbose_name="Pieces")
    weight_d = models.DecimalField(decimal_places=2, max_digits=9,verbose_name="Weight in Grams")
    units = models.CharField(max_length=30, blank=True, null=True)
    tag_price_d = models.DecimalField(decimal_places=2, max_digits=9)
    # status = models.BooleanField(default=False)
    purchaseapv_d = models.BooleanField(blank=True)
    cartstatus = models.BooleanField(default=False)
    appvreturnstatus_d = models.BooleanField(default=False)
    frontend=models.BooleanField(default=False)

    def __str__(self):
        return str(self.stockid)


# SALE OF DIAMOND
class Salesofdiamond(models.Model):
    class Meta:
        verbose_name_plural = "Diamond - Sales"
    date = models.DateField(
        auto_now_add=False, verbose_name="Date of transaction")
    stockid = models.CharField(max_length=30, verbose_name="Stock ID")
    company_name = models.ForeignKey(companyinfo,on_delete=models.PROTECT, verbose_name="Company name")
    location = models.ForeignKey('location', on_delete=models.PROTECT, null=True, verbose_name="Location")
    shape =  models.ForeignKey('shape_d', on_delete=models.PROTECT, null=True, verbose_name="Shape")
    clarity =  models.ForeignKey('clarity', on_delete=models.PROTECT, verbose_name="Clarity")
    color_origin1 = models.ForeignKey('color_origin', on_delete=models.PROTECT, verbose_name="Colour origin")
    white_color_grade1 = models.ForeignKey('white_color_grade', on_delete=models.PROTECT, null=True, blank=True, verbose_name="White Colour Grade")
    # fancy_color_intensity1 = models.CharField(max_length=30)
    fancycolor_grade = models.CharField(max_length=30, verbose_name="Fancy Color Grade")
    # fancy_color_grade = models.CharField(max_length=30)
    cut = models.ForeignKey('cut', on_delete=models.PROTECT, verbose_name="Cut") 
    polish = models.ForeignKey('polish', on_delete=models.PROTECT, verbose_name="Polish")
    symmetry = models.ForeignKey('symmetry', on_delete=models.PROTECT, verbose_name="Symmetry")
    measurements = models.CharField(max_length=30, blank=True, null=True, verbose_name="Measurements")
    depth = models.DecimalField(decimal_places=2, max_digits=9, verbose_name="Depth")
    table = models.DecimalField(decimal_places=2, max_digits=9, verbose_name="Table")
    fluorescence_intensity = models.ForeignKey('fluorescence_intensity', on_delete=models.PROTECT, verbose_name="Fluorescence Intensity")
    fluorescence_color = models.ForeignKey('fluorescence_color', on_delete=models.PROTECT, verbose_name="Fluorescence Color")
    certificate_no_d = models.CharField(max_length=30, verbose_name="Certificate Number")
    certificate_d = models.ForeignKey('certificate_d', on_delete=models.PROTECT, verbose_name="Lab")
    laser_inscription = models.BooleanField(default=False, verbose_name="Laser Inscription")
    PCS_d = models.IntegerField(null=True, blank=True, verbose_name="Pieces")
    weight_d = models.DecimalField(decimal_places=2, max_digits=9, verbose_name="Weight")
    price = models.DecimalField(decimal_places=2, max_digits=9, verbose_name="Price")
    units = models.CharField(max_length=30, blank=True, null=True, verbose_name="Units")
    amount_d = models.DecimalField(decimal_places=2, max_digits=9, verbose_name="Amount")
    DIS_d = models.DecimalField(decimal_places=2, max_digits=9, verbose_name = "Discount %")
    DIS_Amount_d = models.DecimalField(decimal_places=2, max_digits=9, verbose_name="Discount Amount")
    total_value_d = models.DecimalField(decimal_places=2, max_digits=9, verbose_name="Total Value")
    currency = models.ForeignKey(currencies,on_delete=models.PROTECT, verbose_name="Currency")
    tag_price_d = models.DecimalField(decimal_places=2, max_digits=9, verbose_name="Tag Price")
    rate_d = models.DecimalField(decimal_places=2, max_digits=9, verbose_name="Rate")
    salesapprovalstatus_d = models.BooleanField(default=False, verbose_name="Sold")
    comment = models.TextField(max_length=3000, blank=True, null=True, verbose_name="Comment")

    def __str__(self):
        return self.stockid


class cloneInvofdiamond(models.Model):
    class Meta:
        verbose_name_plural = "Diamond - Cart"
    date=models.DateField(auto_now_add=True)
    stockid = models.CharField(max_length=30)
    company_name = models.ForeignKey(companyinfo,on_delete=models.PROTECT,null=True,blank=True)
    location = models.ForeignKey(location, on_delete=models.PROTECT)
    shape = models.ForeignKey(shape_d,on_delete=models.PROTECT)
    clarity = models.ForeignKey(clarity, on_delete=models.PROTECT)
    color_origin1 = models.ForeignKey(color_origin ,on_delete=models.PROTECT)
    white_color_grade1 = models.ForeignKey(white_color_grade ,on_delete=models.PROTECT,null=True,blank=True)
    fancycolor_grade = models.CharField(max_length=30)
    cut = models.ForeignKey('cut', on_delete=models.PROTECT) 
    polish = models.ForeignKey('polish', on_delete=models.PROTECT)
    symmetry = models.ForeignKey('symmetry', on_delete=models.PROTECT)
    measurements = models.CharField(max_length=30, blank=True, null=True)
    depth = models.DecimalField(decimal_places=2, max_digits=9)
    table = models.DecimalField(decimal_places=2, max_digits=9)
    fluorescence_intensity = models.ForeignKey('fluorescence_intensity', on_delete=models.PROTECT)
    fluorescence_color = models.ForeignKey('fluorescence_color', on_delete=models.PROTECT)
    certificate_no_d = models.CharField(max_length=30)
    certificate_d = models.ForeignKey('certificate_d', on_delete=models.PROTECT)
    laser_inscription = models.BooleanField(default=False)
    PCS_d = models.IntegerField(null=True, blank=True)
    weight_d = models.DecimalField(decimal_places=2, max_digits=9)
    price = models.DecimalField( blank=True, null=True, verbose_name="Price", decimal_places=2, max_digits=9)
    units = models.CharField(max_length=30, blank=True, null=True)
    amount_d = models.DecimalField( blank=True, null=True, verbose_name="Amount", decimal_places=2, max_digits=9)
    DIS_d = models.DecimalField( blank=True, null=True, verbose_name="Discount", decimal_places=2, max_digits=9)
    DIS_Amount_d = models.DecimalField( blank=True, null=True, verbose_name="Discount Amount", decimal_places=2, max_digits=9)
    total_value_d = models.DecimalField( blank=True, null=True, verbose_name="Total Value", decimal_places=2, max_digits=9)
    currency = models.ForeignKey(currencies,on_delete=models.PROTECT,null=True,blank=True)
    tag_price_d = models.DecimalField( blank=True, null=True, verbose_name="Tag Price", decimal_places=2, max_digits=9)
    rate_d = models.DecimalField(blank=True, null=True, verbose_name="Rate", decimal_places=2, max_digits=9)
    salesapprovalstatus_d = models.BooleanField(default=False)
    


    def save(self, *args, **kwargs):

        super(cloneInvofdiamond, self).save()


class Salesreturn_d(models.Model):
    class Meta:
        verbose_name_plural = "Diamond - Sales Return"
    date = models.DateField(auto_now_add=True)
    stockid = models.CharField(max_length=30,blank=True, null=True,)
    company_name = models.CharField(max_length=30,blank=True, null=True,)
    location = models.CharField(max_length=30,blank=True, null=True,)
    shape = models.CharField(max_length=30,blank=True, null=True,)
    weight=models.DecimalField(blank=True, null=True, verbose_name="Weight", decimal_places=2, max_digits=9)
    colour=models.CharField(max_length=30,blank=True, null=True,)
    clarity=models.CharField(max_length=30,null=True,blank=True)
    totalamount=models.DecimalField(blank=True, null=True, verbose_name="Total Value", decimal_places=2, max_digits=9)




class Diamond_media(models.Model):
    class Meta:
        verbose_name_plural = "Diamond - Media"
    Diamond_object = models.ForeignKey(
        Inventoryofdiamond, on_delete=models.CASCADE)
    image1 = models.ImageField(
        upload_to="DiamondMedia/", blank=True, null=True)
    image2 = models.ImageField(
        upload_to="DiamondMedia/", blank=True, null=True)
    image3 = models.ImageField(
        upload_to="DiamondMedia/", blank=True, null=True)
    image4 = models.ImageField(
        upload_to="DiamondMedia/", blank=True, null=True)
    image5 = models.ImageField(
        upload_to="DiamondMedia/", blank=True, null=True)
    image6 = models.ImageField(
        upload_to="DiamondMedia/", blank=True, null=True)
    image7 = models.ImageField(
        upload_to="DiamondMedia/", blank=True, null=True)
    image8 = models.ImageField(
        upload_to="DiamondMedia/", blank=True, null=True)
    image9 = models.ImageField(
        upload_to="DiamondMedia/", blank=True, null=True)
    image10 = models.ImageField(
        upload_to="DiamondMedia/", blank=True, null=True)
    video_embed_link = models.TextField(null=True, blank=True)
    certificate = models.FileField(
        upload_to="Certificates/Diamond/", blank=True, null=True)
    description = models.TextField(null=True, blank=True, max_length=5000, verbose_name="Description")
    jewellery_info = models.TextField(null=True, blank=True,  max_length=3000, verbose_name="Diamond Information")







# purchase of Colour Stones

class color_of_colorstone(models.Model):
    class Meta:
        verbose_name_plural = "ColourStone - Colour"

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


#yaha bakchodi kategi
class clonePurchaseOfColorStones(models.Model):
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
    discount = models.DecimalField(decimal_places = 2, max_digits= 9, blank=True, null=True)
    discount_amount = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    total_val = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    purchaseapv = models.BooleanField(default=False)
    currency = models.ForeignKey('currencies', on_delete=models.PROTECT)
    tag_price = models.DecimalField(decimal_places = 2, max_digits= 9,blank=True, null=True)
    rate = models.DecimalField(decimal_places = 2, max_digits= 9,blank=True, null=True)

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
        super(clonePurchaseOfColorStones, self).save(*args, **kwargs)
        obj1 = PurchaseOfColorStones.objects.create(date= self.date, company_name= self.company_name, location=self.location, shape=self.shape,
                                                     Clarity=self.Clarity, PCS=self.PCS, gem_type=self.gem_type, Weight=self.Weight, origin=self.origin, Treatment=self.Treatment, certificate_no=self.certificate_no, colour=self.colour, measurements=self.measurements, lab=self.lab, tag_price=self.tag_price, purchaseapv=self.purchaseapv,
                                                     Price = self.Price,units=self.units,amount=self.amount, discount = self.discount,
                                                     discount_amount=self.discount_amount,total_val=self.total_val, currency=self.currency, rate = self.rate,comment=self.comment)



class PurchaseOfColorStones(models.Model):
    class Meta:
        verbose_name_plural = "ColourStone - Purchase"
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
    discount = models.DecimalField(decimal_places = 2, max_digits= 9, blank=True, null=True)
    discount_amount = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    total_val = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    purchaseapv = models.BooleanField(default=False)
    currency = models.ForeignKey('currencies', on_delete=models.PROTECT)
    tag_price = models.DecimalField(decimal_places = 2, max_digits= 9,blank=True, null=True)
    rate = models.DecimalField(decimal_places = 2, max_digits= 9,blank=True, null=True)

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
                                                     Clarity=self.Clarity, PCS=self.PCS, gem_type=self.gem_type, Weight=self.Weight, origin=self.origin, treatment=self.Treatment, certificate_no=self.certificate_no, color=self.colour, measurements=self.measurements, lab=self.lab, tag_price=self.tag_price, purchaseapv=self.purchaseapv, units = self.units)


class Inventoryofcolorstones(models.Model):
    class Meta:
        verbose_name_plural = "ColourStone - Inventory"
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
    units = models.CharField(max_length=30, blank=True, null=True)
    Weight = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True, verbose_name="Weight")
    tag_price = models.DecimalField(decimal_places = 2, max_digits= 9,blank=True, null=True)
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
    stockid = models.CharField(max_length=30, verbose_name="Stock ID")
    company_name = models.ForeignKey('CompanyInfo', on_delete=PROTECT, verbose_name="Company Name")
    location = models.ForeignKey(
        'location', on_delete=models.PROTECT, null=True, verbose_name="Location")
    shape = models.ForeignKey(
        'shape_cs', on_delete=models.PROTECT, blank=True, verbose_name="Shape")
    gem_type = models.ForeignKey(
        'gemtype', on_delete=models.PROTECT, blank=True, verbose_name="Gem Type")
    origin = models.ForeignKey(
        'Origin_cs', on_delete=models.PROTECT, blank=True, verbose_name="Origin")
    treatment = models.ForeignKey(
        'Treatment_cs', on_delete=models.PROTECT, blank=True, verbose_name="Treatment")
    Clarity = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="Clarity")
    certificate_no = models.CharField(
        max_length=30, verbose_name="Certificate No.")
    color = models.ForeignKey('color_of_colorstone', on_delete=models.PROTECT, verbose_name="Color")
    measurements = models.CharField(
        max_length=30, blank=True, null=True, verbose_name="Measurement")
    lab = models.ForeignKey('Lab_cs', on_delete=models.PROTECT, blank=True, verbose_name="Lab")
    PCS = models.IntegerField(verbose_name="Pieces")
    Weight_cs = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True, verbose_name="Weight")
    price = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True, verbose_name="Price")
    units_cs = models.CharField(max_length=30, default="", verbose_name="Units")
    amount_cs = models.DecimalField(
        verbose_name="Amount", null=True, blank=True, decimal_places=2, max_digits=9)
    DIS_cs = models.DecimalField(
        verbose_name="Discount %", null=True, blank=True, decimal_places=2, max_digits=9)
    DIS_amount_cs = models.DecimalField(
        verbose_name="DISCOUNT Amount", null=True, blank=True, decimal_places=2, max_digits=9)
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
    class Meta:
        verbose_name_plural = "ColourStone - Cart"
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
        decimal_places=2, max_digits=9, blank=True, null=True, verbose_name="Discount %")
    DIS_amount_cs = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True, verbose_name="DISCOUNT Amount")
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
    class Meta:
        verbose_name_plural = "ColourStone - Sales Return"
    date = models.DateField(auto_now_add=True,blank=True, null=True,)
    stockid = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30,blank=True, null=True,)
    weight=models.DecimalField(blank=True, null=True, default=1, decimal_places=2, max_digits=9)
    total_amount=models.DecimalField(blank=True, null=True, default=1, decimal_places=2, max_digits=9)
    colour=models.CharField(max_length=30,blank=True, null=True,)
    location = models.ForeignKey(
        'location', on_delete=models.PROTECT, null=True, blank=True)
    gem_type = models.ForeignKey(
        'gemtype', on_delete=models.PROTECT, blank=True)
    clarity=models.CharField(max_length=30,blank=True,null=True)

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
    description = models.TextField(null=True, blank=True, max_length=5000, verbose_name="Description")
    colorstone_info = models.TextField(null=True, blank=True,  max_length=3000, verbose_name="Colour Stone Information")