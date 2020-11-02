from django import forms
from secondapp.models import User
from django.core import validators

# def check_start_z(value):
# 	if value[0].lower() != 'z':
# 		raise forms.VaildationError("start with z")


class Form(forms.ModelForm):
	class Meta:
		model = User
		fields = '__all__'

		widgets = {
		'first_name': forms.TextInput(attrs={'class':'form-control'}),
		'last_name': forms.TextInput(attrs={'class':'form-control display-inline'}),
		'email': forms.EmailInput(attrs={'class':'form-control'})

		}
	# first_name = forms.CharField()
	# last_name = forms.CharField()
	# email = forms.EmailField(help_text='A valid email address, please.')
	# password = forms.PasswordInput()
	# password2 = forms.PasswordInput()
	botcatcher = forms.CharField(required=False,
								widget= forms.HiddenInput,
								validators=[validators.MaxLengthValidator(0)])
	# def clean_botchatcher(self):
	# 	botcatcher = self.cleaned_data['botcatcher']
	# 	if len(botcatcher) > 0:
	# 		raise forms.VaildationError("GOTCHa BOT!")
	# 	return botcatcher

	# def clean(self):
	# 	all_cleaned_data = super().clean()
	# 	email = all_cleaned_data['email']
	# 	verify_email = all_cleaned_data['verify_email']

	# 	if email != verify_email:
	# 		raise forms.ValidionError("Make sure emails are matched")

