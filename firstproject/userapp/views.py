from django.shortcuts import render
from userapp.forms import UserForm, UserProfileInfoForm

# for login
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
	return render(request, 'userapp/index.html',{})

@login_required
def special(request,username):
	return HttpResponse("Hi {}".format(username))

def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileInfoForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			
			user = user_form.save()
			# encrpt password
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user # This one to one relationship

			if 'profile_picture' in request.FILES:
				print('found it')
				profile.profile_picture = request.FILES['profile_picture']
			print(request.FILES)

			profile.save()

			registered = True
		else:
			# Data enter is invaild
			print(user_form.errors, profile_form.errors)

	else:
		# This is not a post method
		user_form = UserForm()
		profile_form =UserProfileInfoForm()


	forms={'registerd': registered,'user_form':user_form,'profile_form':profile_form}
	return render(request, 'userapp/register.html',context= forms)
	

def user_login(request):
	invalid = False
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username= username, password= password)

		if user is not None:
			if user.is_active:
				print("User is logged in")
				login(request, user)
				# return special(request, username)
				return HttpResponseRedirect(reverse('userapp:index'))
			else:
				return HttpResponse("Your account is not active.")

		else:
			invalid = True
			print("Someone tried to login and failed")
			print("username: {}, password: {}".format(username,password))
			return HttpResponse("Invalid Login details")
	else:
		return render(request, 'userapp/login.html',{})

@login_required
def user_logout(request):
	logout(request)

	return HttpResponseRedirect(reverse('userapp:index'))