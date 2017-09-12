# author = Jasper_Jiao@ele.me
# -*- coding: cp936 -*-
# coding: cp936

import urllib2
import re
import Ch1_download

def crawl_sitemap(url):
    sitemap = Ch1_download.download_3(url)
    links = re.findall('/places/default/view/[a-zA-Z-]+-\d+', sitemap)
    for link in links:
        link = 'http://example.webscraping.com' + link
        html = Ch1_download.download_3(link)

print crawl_sitemap('http://example.webscraping.com/sitemap.xml')
