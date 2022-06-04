from django import template


register = template.Library()


@register.filter
def add_class(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter
def times(number):
    return range(number)


@register.filter
def rating_counter(counter, rating):
    return round((rating - counter) * 100)


@register.filter
@register.simple_tag
def declension(cnt: int, first: str, second: str, third: str):
    s = str(cnt)
    if s[-1:] == '1' and s[-2:] != '11':
        return first
    elif (s[-1:] == '2' or s[-1:] == '3' or s[-1:] == '4') and s[-2:] != '12' and s[-2:] != '13' and s[-2:] != '14':
        return second
    else:
        return third


@register.filter
def get_type(value):
    return type(value)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
