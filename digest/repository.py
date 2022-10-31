from mysite.settings import AIRTABLE_TOKEN

from airtable import airtable

from random import randint
from operator import itemgetter


def shuffle(list):
    l = len(list) - 1
    for i in range(1, 2 * l):
        i1 = randint(0, l)
        i2 = randint(0, l)
        list[i1], list[i2] = list[i2], list[i1]
    return list


def get_plain_even_from_item(item):
    if 'draft' in item['fields']:
        return None

    return {
        "id": item['id'],
        "title": item['fields']['title'],
        "brief": item['fields']['brief'] if 'brief' in item['fields'] else 'опис недоступний',
        'description': item['fields']['description'],
        "balance": item['fields']['balance'],
        "startTime": item['fields']['startTime'],
        "weekday": item['fields']['weekday'],
        "w2": item['fields']['w2'],
        "price": item['fields']['price'],
        "link": item['fields']['link'] if "link" in item['fields'] else None,
        "address": item['fields']['address'],
        "pic": item['fields']['pic'] if 'pic' in item['fields'] else None,
    }


def get_plain_events(raw_events):
    events = []
    for item in raw_events:
        # print(str(item))
        # print(str(item['id']))
        # return events
        if 'draft' not in item['fields']:
            events.append({
                "id": item['id'],
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
    at = airtable.Airtable('appW2upPBNl804iB1', AIRTABLE_TOKEN)
    raw_events = at.get('events', filter_by_formula=filter)['records']
    return get_plain_events(raw_events)


def fetch_by_id(id: str):
    at = airtable.Airtable('appW2upPBNl804iB1', AIRTABLE_TOKEN)
    raw_event = at.get('events', record_id=id)
    event = get_plain_even_from_item(raw_event)
    return event


if __name__ == '__main__':
    e = fetch_by_id('rect1FgRJLsrM0cuL')
    print(str(e['pic'][0]['url']))
