# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import json
import requests


def get_resp_d(resp):
    if resp and resp.content:
        return json.loads(resp.content)
    else:
        return {}

def get_result_d(resp_d):
    if resp_d['response'] and resp_d['response']['docs']:
        result_d = resp_d['response']['docs']
        for c, row in enumerate(result_d):
            row['c'] = c
            row['name'] = row.pop('label')
            row['ontology_id'] = row.pop('id')
        return result_d
    else:
        return {}

def search_ontology_term(search_term):
    url = 'https://www.ebi.ac.uk/ols/api/search?q={}'.format(search_term)
    resp = requests.get(url)

    resp_d = get_resp_d(resp)
    if not resp_d:
        return {}

    return get_result_d(resp_d)



def search_ontology_term_shrt(shrt, ontology_prefix):
    url = 'https://www.ebi.ac.uk/ols/api/search?q={}&queryFields=short_form'.format(shrt)
    resp = requests.get(url)
    resp_d = get_resp_d(resp)
    if not resp_d:
        return {}

    result_d = get_result_d(resp_d)

    for row in result_d:
        if row['ontology_prefix'] == ontology_prefix:
            return row

    return {}