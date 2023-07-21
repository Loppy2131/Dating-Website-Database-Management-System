from django.shortcuts import render
from pairs import models
from . import forms
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.sessions.models import Session
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def marriage(request):
	posts = models.Marriage.objects.filter(enabled=True).order_by('-ddate')[:30]
	userid=request.session['userid']
	username=request.session['username']
	return render(request,'pairs/marriage.html', locals())
def inrelationship(request):
	posts = models.Inrelationship.objects.filter(enabled=True).order_by('-ddate')[:30]
	userid=request.session['userid']
	username=request.session['username']
	return render(request,'pairs/relationship.html', locals())

def security(request):
	userid=request.session['userid']
	username=request.session['username']
	return render(request,'pairs/security.html', locals())
def learn(request):
	userid=request.session['userid']
	username=request.session['username']
	return render(request,'pairs/information.html', locals())
def pair_profile(request,pairname=""):
	if 'username' in request.session==None:
		return HttpResponseRedirect('/')
	username=request.session['username']
	userid=request.session['userid']
	pairuser = models.UserRigister.objects.get(name=pairname)

	return render(request,'pairs/pair_profile.html', locals())
def pairing(request):
	userid=request.session['userid']
	username=request.session['username']
	user = models.UserRigister.objects.get(userid = userid)
	users = models.UserRigister.objects.all()

	message='來選'

	a = []
	b=[]
	c=[]
	d=[]
	if request.method=='POST':
		for use in users:
			if request.POST.get(str(use.id)):
				try:
					models.Pairid.objects.get(person=use,pairid=use.id)
					return HttpResponseRedirect('.')
				except:
					models.Pairid.objects.create(person=user,pairid=use.id)
					
					
			if request.POST.get('n'+str(use.id)):
				try:
					models.NotPairid.objects.get(person=use,notpairid=use.id)
					
					return HttpResponseRedirect('.')
				except:
					models.NotPairid.objects.create(person=user,notpairid=use.id)
					
					
			# 叉叉
	notnumbers = models.NotPairid.objects.filter(person = user)
	for notnum in notnumbers:
		b=[notnum.notpairid]+b

		
	numbers = models.Pairid.objects.filter(person = user)
	for num in numbers:
		a=[num.pairid]+a
	
	choiceid = models.Pairid.objects.filter(person=user)
	for choiceid_solo in choiceid:
		c=[choiceid_solo.pairid]+c
	unpair=models.UserRigister.objects.filter(id__in=c)
	for unpair_solo in unpair:
		unpair_pairid=models.Pairid.objects.filter(person = unpair_solo)
		for unpair_pairid_solo in unpair_pairid:
			if unpair_pairid_solo.pairid==user.id:
				d=[unpair_solo.id]+d
				message='Pair Successfully'

	pair=models.UserRigister.objects.filter(id__in=d)	
	# 需要排除掉的 包括 自己,沒選的性別,按叉叉的人,按過愛心的人
	
	exuser=models.UserRigister.objects.filter(gender=user.pair_gender).exclude(id=user.id).exclude(id__in=a+b)
	
		
				

		
	return render(request,'pairs/pairing.html', locals())
def uploadFile(request):
	userid=request.session['userid']
	user = models.UserRigister.objects.get(userid = userid)
	if request.method=='POST':
		img=request.FILES.get('img')
		user.photo=img
		user.save()
		return HttpResponseRedirect('/profile')
	return render(request,'pairs/upload.html', locals())

def updated(request):
	if 'username' in request.session==None:
		return HttpResponseRedirect('/')
	userid=request.session['userid'] 
	username=request.session['username']
	user = models.UserRigister.objects.get(userid = userid)
	form = forms.UploadForm()

	if user.gender=='Female':
		g=1
	if user.gender=='Male':
		g=None
	if user.pair_gender=='Female':
		p=1
	if user.pair_gender=='Male':
		p=None
	if request.method =='POST':
		
		username  = request.POST.get('username')
		user.height  = request.POST.get('height')
		user.weight  = request.POST.get('weight')
		user.gender  = request.POST.get('gender')
		user.pair_gender  = request.POST.get('pair_gender')
		user.intro  = request.POST.get('intro')
		user.phone  = request.POST.get('phone')
		user.name=username
		
		user.save()
		request.session['username']=username
		message = 'saved'
		return HttpResponseRedirect('/profile')

	return render(request,'pairs/updated.html', locals())

def index(request):
	if 'username' in request.session:
		username=request.session['username']
	return render(request,'pairs/index.html', locals())

def signup(request):

	signup_form=forms.SignupForm()
	if 'username' in request.session:
		username=request.session['username']
		return HttpResponseRedirect('/')

	if request.method =='POST':
		signup_form = forms.SignupForm(request.POST)
		if signup_form.is_valid():
			try: 
				models.UserRigister.objects.get(userid=request.POST.get('userid'))
				message = 'userid repeat'
				
			except:
				message = 'Saved successfully'
				signup_form.save()
				return HttpResponseRedirect('/')
		else:
			message = 'Fields are required!!'
	else:
		signup_form = forms.SignupForm()
	


	return render(request, 'pairs/signup.html',locals())
def login(request):
	if 'username' in request.session:
		username=request.session['username']
		return HttpResponseRedirect('/')
	if request.method =='POST':
		login_form = forms.LoginForm(request.POST)
		if login_form.is_valid():
			userid = request.POST['userid'].strip()
			password = request.POST['password']
			try:
				user = models.UserRigister.objects.get(userid = userid)
				if user.password == password:
					request.session['userid']=user.userid
					request.session['username']=user.name
					return HttpResponseRedirect('/')
				else:
					message = 'wrong password'
			except:
				message = 'no user'
		else:
			message='pleasw check it again'
	else:
		login_form = forms.LoginForm()
	return render(request,'pairs/login.html',locals())
# def signin(request):
# 	return render(request, 'pairs/signin.html',locals())
def logout(request):
	if 'username' in request.session:
		Session.objects.all().delete()
		return HttpResponseRedirect('/')

def profile(request):
	if 'username' in request.session==None:
		return HttpResponseRedirect('/')
	username=request.session['username']
	userid=request.session['userid']
	user = models.UserRigister.objects.get(userid = userid)
	profile_form=forms.ProfileForm()
	if request.method =='POST':
		profile_form = forms.ProfileForm(request.POST)
		if profile_form.is_valid():
			message = 'Saved successfully'


			username=user.name
			request.session['username']=user.name
		else:
			message = 'Fields are required!!'
	else:
		profile_form = forms.ProfileForm()
		message = 'Fields are required!!'


	return render(request,'pairs/profile.html',locals())