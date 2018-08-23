import math, urllib

from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

from jinja2 import Environment, contextfilter

@contextfilter
def number_format(context, value, thousand_sep=' ', point=',', digits=1):
    return ('{0:,.' + str(digits) + 'f}').format(value).replace(',', thousand_sep).replace('.', point)

@contextfilter
def date_format(context, value):
    return '{:%d.%m.%Y в %H:%M:%S}'.format(value)

def query(entries):
    res = '?' + urllib.parse.urlencode(entries)
    return res


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'query': query,
    })

    env.filters.update({
        'number_format': number_format,
        'date_format': date_format,
    })
    
    return env