# coding: UTF-8
from bs4 import BeautifulSoup
import urlparse
import urllib2

class get_list():

    def __init__(self):
        self.parse_url = 'http://www.cga.com/'


    def _join_url(self,url):
        if 'http://' not in url and 'https://' not in url and 'javascript' not in url:
            url.strip('/')
            urlparse.urljoin(self.parse_url,url)
            new_link = url
        else :
            if 'mailto:' not in url and 'javascript' not in url:
                new_link = url
        return new_link



    def _get_a_href(self,soup):
        a_herfs = []
        a_tags = soup.find_all('a')
        for a_tag in a_tags:
            a_href = a_tag['href'].encode('utf-8')
            a_text = a_tag.get_text().encode('utf-8')

            a_link = self._join_url(a_href)
            # print "a_link %s" % a_link
            if a_link is not None and a_link != '':
                code = self._get_url_code(a_link)
                if code is not None and code != 0:
                    a_list = {};
                    a_list['href'] = a_link
                    a_list['text'] = a_text
                    a_list['code'] = code
                    a_herfs.append(a_list)
            return a_herfs


    def _get_img_src(self,soup):
        img_srcs = []
        img_tags = soup.find_all('img');
        for img_tag in img_tags:
            img_src = img_tag['src'].encode('utf-8')
            if "http://" not in img_src and "https://" not in img_src:
                img_src.strip('/')
                img_src = urlparse.urljoin(self.parse_url,img_src)
            code = self._get_url_code(img_src)
            if code is not None and code != 0:
                image = {}
                image['src'] = img_src
                image['code'] = code
                img_srcs.append(image)
        return img_srcs

    def _get_email_list(self,soup):
        email_list = []
        a_tags = soup.find_all('a')
        for a_tag in a_tags:
            a_href = a_tag['href'].encode('utf-8')
            a_text = a_tag.get_text().encode('utf-8')
            if 'http://' in a_href:
                if 'mailto:' in a_href:
                    code = self._get_url_code(a_href)
                    if code is not None and code != 0 :
                        email = {}
                        email['href'] = a_href
                        email['text'] = a_text
                        email['code'] = code
                        email_list.append(email)

        return email_list

    def _get_url_code(self,url):
        if url is None or url == '':
            return None
        req = urllib2.Request(url)
        try:
            res = urllib2.urlopen(req,timeout=20)
            # print res.getcode()
            code = 0
        except urllib2.HTTPError, e:
            code = e.code
        except urllib2.URLError, e:
            # print url
            # print e.reason
            code = 0
        else:
            code = 0

        return code





    def parse(self,html_cont):
        if html_cont is None:
            return
        soup = BeautifulSoup(html_cont,"html.parser",from_encoding="utf-8")
        a_herf = self._get_a_href(soup)
        img_src = self._get_img_src(soup)
        mail_list  = self._get_email_list(soup)

        return a_herf,img_src,mail_list
