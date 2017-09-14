# author = Jasper_Jiao@ele.me
# -*- coding: cp936 -*-
# coding: cp936

from bs4 import BeautifulSoup

import Scrapy.Ch1.Ch1_download as C1

url = 'http://example.webscraping.com/places/default/view/united-kindom-239'
#html = C1.download_3(url)
#print re.findall('<td class="w2p_fw">(.*?)</td>', html)
#print re.findall('<td class="w2p_fw">(.*?)</td>', html)[1]
#print re.findall('<tr id="places_area__row"><td class="w2p_fl"><label class="readonly" for="places_area" id="places_area__label">Area:</label></td><td class="w2p_fw">(>*?)</td><td class="w2p_fc"/></tr>', html)
#print re.findall('<tr id="places_area__row">.*?<td\s*class=["\']w2p_fw["\']>(.*?)</td>', html)



# Beautiful soup
broken_html = '<ul class=country><li>Area<li>Population</ul>'
soup = BeautifulSoup(broken_html, 'html.parser')
fixed_html = soup.prettify()
#print fixed_html



ul = soup.find('ul', attrs={'class':'country'})
#print ul.find('li')
#print ul.find_all('li')



def extract_area(url):
    html = C1.download_3(url)
    soup = BeautifulSoup(html, 'html.parser')
    tr = soup.find(attrs={'id':'places_area__row'})
    td = tr.find(attrs={'class':'w2p_fw'})
    area = td.text
    print area

extract_area('http://example.webscraping.com/places/default/view/united-kindom-239')