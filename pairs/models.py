from django.db import models
from django.core.validators import validate_comma_separated_integer_list
from phone_field import PhoneField
class UserRigister(models.Model):
	GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
	userid = models.CharField(max_length=20,null=False)

	password = models.CharField(max_length = 20, null=False)
	email = models.EmailField()

	name = models.CharField(max_length=20)
	height = models.PositiveIntegerField(default = 170)
	weight = models.PositiveIntegerField(default = 70)
	gender = models.CharField(max_length=20,choices=GENDER_CHOICES,default='Male')
	pair_gender = models.CharField(max_length=20,choices=GENDER_CHOICES,default='Male')


	photo = models.ImageField(upload_to='image/')
	phone = models.CharField(max_length=10)
	intro = models.CharField(max_length=20,default='')
	def __str__(self):
		return self.name

class Pairid(models.Model):
	person = models.ForeignKey(UserRigister, on_delete = models.CASCADE)
	pairid = models.PositiveIntegerField()

	def __str__(self):
		return str(self.pairid)
class NotPairid(models.Model):
	person = models.ForeignKey(UserRigister, on_delete = models.CASCADE)
	notpairid = models.PositiveIntegerField()

	def __str__(self):
		return str(self.notpairid)
class Marriage(models.Model):
	user 	= models.ForeignKey(UserRigister,on_delete=models.CASCADE)
	enabled  = models.BooleanField(default=False)
	note 	= models.TextField()
	ddate 	= models.DateField()
	def __str__(self):
		return "{}({})".format(self.ddate, self.user)
class Inrelationship(models.Model):
	user 	= models.ForeignKey(UserRigister,on_delete=models.CASCADE)

	note 	= models.TextField()
	enabled  = models.BooleanField(default=False)
	ddate 	= models.DateField()
	def __str__(self):
		return "{}({})".format(self.ddate, self.user)