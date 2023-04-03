from django.db import models
from django.core.exceptions import ValidationError

class New_table(models.Model):
    models_f =models.BigIntegerField()
    bool_f = models.BooleanField()
    data_f = models.DateField(auto_now=True)
    char_f = models.CharField(max_length=25, unique=True)
    datetime_f = models.DateTimeField(auto_now_add=True)
    Decimal_f = models.DecimalField(max_digits=10, decimal_places= 2)
    flot_f = models.FloatField(null=True)
    int_f = models.IntegerField(default=2010)
    tesxt_f=models.TextField() 

class product(models.Model):
    Sizes=(
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
    )
    sku = models.CharField(max_length=10)
    name=models.CharField(max_length=25)
    price=models.PositiveBigIntegerField()
    size=models.CharField(max_length=1,choices=Sizes)
    qty=models.PositiveBigIntegerField(default=0)
    Available = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    def validate_qty(self):
        if self.qty > 100:
            raise ValidationError('Quantity cannot be greater than 100')
