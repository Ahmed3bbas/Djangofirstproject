from django.urls import path, include
from secondapp import views

app_name = 'secondapp'
urlpatterns = [
	path('', views.home, name='home'),
	path('signup/',views.signup, name="signup")
	
]