# author = Jasper_Jiao@ele.me
# -*- coding: cp936 -*-
# coding: cp936

import time
import re
import Ch2_compare
import Scrapy.Ch1.Ch1_download

NUM_ITERATIONS = 1000
html = Scrapy.Ch1.Ch1_download.download_3('http://example.webscraping.com/places/default/view/united-kingdom-239')

for name, scraper in [('Regular expressions', Ch2_compare.re_scraper),
                      ('BeautifulSoup', Ch2_compare.bs_scraper),
                      ('Lxml', Ch2_compare.lxml_scraper)]:
    start = time.time()
    for i in range(NUM_ITERATIONS):
        if scraper == Ch2_compare.re_scraper(html):
            re.purge()
        result = scraper(html)
        assert(result['area'] == '244,820 square kilometres')
    end = time.time()
    print '%s: %.2f seconds' % (name, end - start)
