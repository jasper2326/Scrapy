# author = Jasper_Jiao@ele.me
# -*- coding: cp936 -*-
# coding: cp936

import lxml.html
import urllib2

broken_html = '<ul class=country><li>Area<li>Population</ul>'
tree = lxml.html.fromstring(broken_html)
fixed_html = lxml.html.tostring(tree, pretty_print=True)
#print fixed_html


url = 'http://example.webscraping.com/places/default/view/united-Kingdom-239'
html = urllib2.urlopen(url).read()
tree_new = lxml.html.fromstring(html)
td = tree_new.cssselect('tr#places_area__row > td.w2p_fw')[0]
area = td.text_content()
print area