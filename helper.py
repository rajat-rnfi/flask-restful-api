import re
from flask import jsonify
from sqlalchemy import desc, asc

from .models import Articles


def datatable(queryset, data: dict, id_label):
    search = data['search']
    start = data['start']
    length = data['length']
    orderby = data['orderby']
    order = data['order']

    if start and re.match('^[0-9]+$', start) is None:
        raise Exception('All Data Points should be in Valid format!')

    if length and re.match('^[0-9a-zA-Z]+$', length) is None:
        raise Exception('All Data Points should be in Valid format!')

    if order and order != 'desc' and order != 'asc':
        raise Exception('All Data Points should be in Valid format!')

    if not all([orderby, order]):
        orderby = "article_id"
        order = "desc"
    
    queryset = get_sorted_articles(queryset, orderby, order)

    if not start:
        start = 0

    if not length:
        length = 20
    
    if search and id_label == 'article_id':
        queryset = queryset.filter((Articles.author.like(f"{search}%")) | Articles.content.like(f"{search}%") | Articles.title.like(f"{search}%") | Articles.publication_date.like(f"{search}%"))

    totalCount = queryset.count()

    if str(length).lower() != 'all':
        length = int(start)+int(length)
        queryset = queryset.offset(start).limit(length)
        
    queryset = queryset.all()

    response = {
        'data': queryset,
        'count': totalCount
    }
    return response


def get_sorted_articles(queryset, order_by, direction):
    column = getattr(Articles, order_by, None)
    if column is None:
        column = Articles.article_id
    if direction == 'desc':
        column = desc(column)
    else:
        column = asc(column)
    return queryset.order_by(column)


def mainHeaders(headers=[]):
    headers = [i for i in headers]
    updated_headers = []
    for k in headers:
        value = k.replace('_', ' ')
        value = re.sub("(^|\s)(\S)", convert_into_uppercase, value)
        result2 = {
            'name': k,
            'value': value,
            'is_show': 1,
            'is_sort': 1
        }
        updated_headers.append(result2)

    return updated_headers


def convert_into_uppercase(a):
    return a.group(1) + a.group(2).upper()


def success_resp(data: dict, statuscode: int = 200):
    data['status'] = True
    data['statuscode'] = statuscode
    resp = jsonify(data)
    resp.status_code = statuscode
    return resp


def error_resp(data: dict, statuscode: int = 400):
    data['status'] = False
    data['statuscode'] = statuscode
    resp = jsonify(data)
    resp.status_code = statuscode
    return resp


def validate_payload(input: str, payload: dict):
    if input in payload and payload[input]:
        return True
    return False
