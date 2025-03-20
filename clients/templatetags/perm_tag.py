from django import template

register = template.Library()

@register.filter
def has_perm(user, perm_name):
    """ Проверяет, есть ли у пользователя указанное право. """
    return user.has_perm(perm_name) if user.is_authenticated else False
