from django import template
register = template.Library()


@register.simple_tag()
def customer_price(value):
    # return value with 2 decimal places
    price = int(value) * 1.20
    return "{:.2f}".format(price)


@register.simple_tag()
def broker_price(value):
    # return value with 2 decimal places
    price = int(value) * 1.15
    return "{:.2f}".format(price)


@register.simple_tag()
def wholesaler_price(value):
    # return value with 2 decimal places
    price = int(value) * 1.10
    return "{:.2f}".format(price)
