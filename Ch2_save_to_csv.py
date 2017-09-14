# author = Jasper_Jiao@ele.me
# -*- coding: cp936 -*-
# coding: cp936

import re
import urllib2
import lxml.html
import csv
import Ch2_link_crawler

class ScrapeCallback:
    def __init__(self):
        self.writer = csv.writer(open('countries.csv', 'w'))
        self.fields = ('area', 'population', 'country', 'capital',
                       'continent', 'tld', 'currency_code', 'currency_name',
                       'phone', 'postal_code_format', 'postal_code_regex',
                       'languages', 'neighbours')
        self.writer.writerow(self.fields)


    def __call__(self, url, html):
        if re.search('/view/', url):
            tree = lxml.html.fromstring(html)
            row = []
            for field in self.fields:
                row.append(tree.cssselect('table > tr#places_%s__row > td.w2p_fw' % field)[0].text_content())
            self.writer.writerow(row)

Ch2_link_crawler.link_crawler('http://example.webscraping.com/places/default', '/(index|view)', max_depth=1, scrape_callback=ScrapeCallback())