# author = Jasper_Jiao@ele.me
# -*- coding: cp936 -*-
# coding: cp936

import re

from bs4 import BeautifulSoup

from eleme.Scrapy.Ch1 import Ch1_download

url = 'http://example.webscraping.com/places/default/view/united-kindom-239'
html = Ch1_download.download_3(url)
#print re.findall('<td class="w2p_fw">(.*?)</td>', html)
#print re.findall('<td class="w2p_fw">(.*?)</td>', html)[1]
#print re.findall('<tr id="places_area__row"><td class="w2p_fl"><label class="readonly" for="places_area" id="places_area__label">Area:</label></td><td class="w2p_fw">(>*?)</td><td class="w2p_fc"/></tr>', html)
print re.findall('<tr id="places_area__row">.*?<td\s*class=["\']w2p_fw["\']>(.*?)</td>', html)

# Beautiful soup
broken_html = '<ul class=country><li>Area<li>Population</ul>'
soup = BeautifulSoup(broken_html, 'html.parser')

