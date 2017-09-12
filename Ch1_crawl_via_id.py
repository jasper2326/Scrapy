# author = Jasper_Jiao@ele.me
# -*- coding: cp936 -*-
# coding: cp936

import itertools
import re
import Ch1_download

def crawl_via_id_0():
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/places/default/view/-%d' % page
        html = Ch1_download.download_3(url)
        if html is None:
            break
        else:
            pass


def crawl_via_id_1():
    max_errors = 5
    num_errors = 0
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/places/default/view/-%d' % page
        html = Ch1_download.download_3(url)
        if html is None:
            num_errors += 1
            if num_errors == max_errors:
                break
        else:
            num_errors = 0