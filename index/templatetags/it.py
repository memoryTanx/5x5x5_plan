from django import template

register = template.Library()


def isdict(obj):
    return isinstance(obj, dict)


def re(obj, it):
    obj.remove(it)
    return ''


register.filter('isdict', isdict)
register.filter('re', re)
