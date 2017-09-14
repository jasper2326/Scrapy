# author = Jasper_Jiao@ele.me
# -*- coding: cp936 -*-
# coding: cp936

import re
import urllib2
import lxml.html

FIELDS = ('area', 'population', 'country', 'capital',
          'continent', 'tld', 'currency_code', 'currency_name',
          'phone', 'postal_code_format', 'postal_code_regex',
          'languages', 'neighbours')

def scraper_callback(url, html):
    if re.search('view', url):
        tree = lxml.html.fromstring(html)
        row = [tree.cssselect('table > tr#places_%s__row > td.w2p_fw' % field)[0].text_content() for field in FIELDS]
        print url, row


url = 'http://example.webscraping.com/places/default/view/united-kingdom-239'
html = urllib2.urlopen(url).read()
scraper_callback(url, html)