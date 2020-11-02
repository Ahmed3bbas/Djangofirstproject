from django.shortcuts import render
from django.http import HttpResponse
from secondapp.models import User
from secondapp import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
	users_list = User.objects.all()
	# temp = []
	# for user in users_list:
	# 	name = user.first_name + ' ' + user.last_name
	# 	temp.append({'name': name,'email':user.email})
	# users_list = temp
	user_dict = {'users': users_list}
	return render(request, 'secondapp/home.html', context= user_dict)


def signup(request):
	my_dict = {'form':forms.Form()}

	if request.method == 'POST':
		form = forms.Form(request.POST)
		if form.is_valid():
			print("Data that you entered")
			print("first_name: ", form.cleaned_data['first_name'])
			print("last_name: ", form.cleaned_data['last_name'])
			print("Email: ", form.cleaned_data['email'])

			print('\n saiving data to DataBase \n')
			form.save()
			return home(request)
		else:
			print('ERROR FORM INVALID')

	return render(request, "secondapp/signup.html",context=my_dict)