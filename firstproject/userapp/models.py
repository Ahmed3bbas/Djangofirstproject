from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

	# make one to one relationship between user and its data
	user = models.OneToOneField(User,on_delete= models.CASCADE)

	portfolio_site = models.URLField(blank=True) #blank=True means not required field

	profile_picture = models.ImageField(upload_to='profile_pics', blank=True) #upload to porfile_pics in media folder

	def __str__(self):
		return self.user.username

