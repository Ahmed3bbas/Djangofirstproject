import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')

import django
# Import settings
django.setup()

import random
from firstapp.models import Topic,Webpage,AccesRecord
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t



def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Get Topic for Entry
        top = add_topic()

        # Create Fake Data for entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create new Webpage Entry
        webpg = Webpage.objects.get_or_create(topic=top,site=fake_url,name=fake_name)[0]

        # Create Fake Access Record for that page
        # Could add more of these if you wanted...
        accRec = AccesRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
