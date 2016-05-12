from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

class CellCarrier(models.Model):
	name=models.CharField(max_length=255)
	sms_gateway=models.CharField(max_length=255)


class Voter(models.Model):
	phone_regex=RegexValidator(
			regex=r'^\+?1?\d{9,15}$',
			 message=
			 	"""
				 Phone number must be entered in the format: '+999999999'.
				 Up to 15 digits allowed.
				 """
		)

	user = models.ForeignKey(User)
	phone = models.CharField(max_length=255, validators=[phone_regex])
	phone_key = models.IntegerField(blank=True, default=00000)
	phone_key_generated_at = models.DateTimeField(blank=True, auto_now_add=True)
	carrier = models.ForeignKey(CellCarrier)

	phone_validated=models.BooleanField(default=False)