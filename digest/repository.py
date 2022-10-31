from mysite.settings import AIRTABLE_TOKEN

from airtable import airtable

from random import randint
from operator import itemgetter

def shuffle(list):
    l = len(list)-1
    for i in range(1,2*l):
        i1 = randint(0, l)
        i2 = randint(0, l)
        list[i1], list[i2] = list[i2], list[i1]
    return list

def get_plain_events(raw_events):
    events = []
    for item in raw_events:
        if 'draft' not in item['fields']:
            events.append({
                "title": item['fields']['title'],
                "brief": item['fields']['brief'] if 'brief' in item['fields'] else 'опис недоступний',
                "balance": item['fields']['balance'],
                "startTime": item['fields']['startTime'],
                "weekday": item['fields']['weekday'],
                "w2": item['fields']['w2'],
                "price": item['fields']['price'],
                "link": item['fields']['link'] if "link" in item['fields'] else None,
                "address": item['fields']['address']
            })

    events = shuffle(events)
    events = sorted(events, key=itemgetter('w2'))
    return events

def fetch(filter="w2>=0"):
    at = airtable.Airtable('appW2upPBNl804iB1', AIRTABLE_TOKEN )
    raw_events =  at.get('events',filter_by_formula=filter)['records']
    return get_plain_events(raw_events)