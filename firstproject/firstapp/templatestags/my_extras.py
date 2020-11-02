from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, args):
	'''
	cut function uses to remove args from value
	'''
	return value.replace(args,'')

