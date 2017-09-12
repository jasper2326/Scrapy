# author = Jasper_Jiao@ele.me
# -*- coding: cp936 -*-
# coding: cp936

import builtwith
import whois
import urllib2
import re

def download_0(url):
    return urllib2.urlopen(url).read()


def download_1(url):
    print 'Downloading: ', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error: ', e.reason
        html = None
    return html


def download_2(url, num_retries = 2):
    print 'Downloading: ', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error: ', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download_1(url, num_retries - 1)
    return html


def download_3(url, user_agent = 'wswp', num_retries = 2):
    print 'Downloading: ', url
    headers = {'User_agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download error: ', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download_1(url, user_agent, num_retries - 1)
    return html

