from django import template
import math
register = template.Library()

@register.simple_tag
def rate_calculation(abc,abcd):
    if abcd is None or abcd is 0:
        return 0
    star_cent = abc
    star_cent = ((abc / abcd)/20.0)
    return float(star_cent)