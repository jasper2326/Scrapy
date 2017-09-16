# author = Jasper_Jiao@ele.me
# -*- coding: cp936 -*-
# coding: cp936

import re
from bs4 import BeautifulSoup
import lxml.html

FIELDS = ('area', 'population', 'country', 'capital',
          'continent', 'tld', 'currency_code', 'currency_name',
          'phone', 'postal_code_format', 'postal_code_regex',
          'languages', 'neighbours')

def re_scraper(html):
    result = {}
    for field in FIELDS:
        result[field] = re.search('<tr id="places_%s__row">.*?td class="w2p_fw">(.*?)</td>' % field, html).groups()[0]
        return result


def bs_scraper(html):
    soup = BeautifulSoup(html, 'html.parser')
    result = {}
    for field in FIELDS:
        result[field] = soup.find('table').find('tr',
                                                id='places_%s__row' % field).find('td',
                                                                                  class_='w2p_fw').text
        return result


def lxml_scraper(html):
    tree = lxml.html.fromstring(html)
    result = {}
    for field in FIELDS:
        result[field] = tree.cssselect('table > tr#places_%s__row > td.w2p_fw' % field)[0].text_content()
    return result