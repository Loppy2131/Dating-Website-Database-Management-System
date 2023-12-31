from django import forms
from .import models
from captcha.fields import CaptchaField
class DateInput(forms.DateInput):
	input_type = 'date'
class MarriageForm(forms.ModelForm):
	class Meta:
		model = models.Marriage
		fields = ['note','ddate']
		widgets = {'ddate' : DateInput(),}

	def __init__(self, *args, **kwargs):
		super(MarriageForm, self).__init__(*args, **kwargs)

		self.fields['note'].label 		='contect'
		self.fields['ddate'].label 		='date'
class SignupForm(forms.ModelForm):
	captcha = CaptchaField()
	class Meta:
		model = models.UserRigister
		fields =  ['userid', 'password','email','name' ]
	def __init__(self, *args, **kwargs):
		super(SignupForm, self).__init__(*args, **kwargs)
		
		self.fields['userid'].label 	= 'set ID'
		self.fields['password'].label 	= 'set passwprd'
		self.fields['email'].label 	= 'email'
		self.fields['name'].label 	= 'your username'
		self.fields['captcha'].label 	='pleas insert'

class LoginForm(forms.Form):
	userid = forms.CharField(label = 'id', max_length=20)
	password = forms.CharField(label = 'password',widget = forms.PasswordInput())
class ProfileForm(forms.ModelForm):

	class Meta:

		model = models.UserRigister
		fields =  ['name', 'height','weight','gender','pair_gender' ]
		widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),

			}
	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)

		self.fields['name'].label 	= 'username'
		self.fields['height'].label 	= 'height'
		self.fields['weight'].label 	= 'weight'
		self.fields['gender'].label 	='sex'
		self.fields['pair_gender'].label 	='pair sex'
class UploadForm(forms.ModelForm):
    class Meta:
        model = models.UserRigister
        fields = ('photo',)
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }