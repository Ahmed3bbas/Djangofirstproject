from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import AccesRecord

# Create your views here.

def index(req):
	# my_dict = {'add_text': "Ahmed added you"}
	access_data = AccesRecord.objects.all()
	insert_dates = {'access_data': access_data}
	return render(req, 'firstapp/index.html', context=insert_dates)

def home(request):
	return render(request, "firstapp/home.html")

def help(request):
	help_instructions = {"help": "Please help me!"}
	return render(request, "help.html", context= help_instructions)


