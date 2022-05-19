from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Accounts(models.Model):
    access_token = models.CharField(max_length=64)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # new
        on_delete=models.CASCADE
    )
    item_id = models.CharField(max_length=64)
    institution_id = models.CharField(max_length=64)
    ACCOUNT_TYPES = (
        ("C", "Credit"),
        ("D", "Debit")
    )
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPES)
    checking_active = models.BooleanField(default=True, blank=False, null=True)
    savings_active = models.BooleanField(default=True, blank=False, null=True)


class Lanes(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=64)
    raw_value = models.DecimalField(max_digits=11, decimal_places=2, blank=False, null=True)
    percentage_value = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MaxValueValidator(1), MinValueValidator(0)],
        blank=False,
        null=True
    )


class Pool(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    lanes = models.ManyToManyField(Lanes)
    name = models.CharField(max_length=32)
