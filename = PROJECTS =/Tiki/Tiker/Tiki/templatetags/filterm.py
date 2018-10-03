from django import template

register = template.Library()

@register.filter(name='boom')
def fiji(value, arg):
    return value + arg

# register.filter('fiji', fiji)
