from django import template

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group):
    groups = user.groups.all().values_list('name', flat=True)
    return group in groups
