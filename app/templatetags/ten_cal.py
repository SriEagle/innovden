from django import template
import math
register = template.Library()

@register.simple_tag
def tenth_calculation(total_rating,number_rating):
    if number_rating is None or number_rating is 0:
        return 0
    var_cent = total_rating
    var_cent = ((total_rating / number_rating)*100.0)
    return float(var_cent)