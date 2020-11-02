import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')

import django
# Import settings
django.setup()

from secondapp.models import User
from faker import Faker

fakegen = Faker()

def add_fake_data(N=6):

	for i in range(N):
		user = fakegen.simple_profile()
		name = user['name'].split()
		first_name = name[0]
		last_name = name[-1]
		email = user['mail']
		x = User.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)[0]



if __name__ == '__main__':
	print("Populating the databases...Please Wait")
	add_fake_data(20)
	print('Populating Complete')

