# coding:utf-8
from bs4 import BeautifulSoup
import urlparse
import urllib2
import html_outputer

# import requests
import socket
import httplib
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class UrlManager():


    def __init__(self):
        self.parse_url = 'http://www.cga.com/'
        self.content_list = []
        self.content_old_list = []
        self.count = 1
        self.outputer = html_outputer.HtmlOutputer

    def _join_url(self,url):
        new_link = ''
        if url.find("/") == 0 :
            url.strip('/')
            new_link = urlparse.urljoin(self.parse_url, url)
        elif url.find("mailto:") == 0:
            pass
        elif url.find("javascript") == 0 :
            pass
        elif url.find("http://") < 0 and url.find("https://") < 0 :
            url.strip('/')
            new_link = urlparse.urljoin(self.parse_url, url)
        else:
            new_link = url
        return new_link



    def _get_a_href(self,soup,content_id,lang):
        a_herfs = []
        a_tags = soup.find_all('a')
        for a_tag in a_tags:
            # print a_tag
            try :
                a_href = a_tag['href'].encode('utf-8')
            except:
                a_href = a_tag['href']
            try :
                a_text = a_tag.get_text().encode('utf-8')
            except:
                a_text = a_tag.get_text()


            a_link = self._join_url(a_href)
            # print "a_link %s" % a_link
            if a_link is not None and a_link != '':
                code = self._get_url_code(a_link)
                if code is not None and code != 0:
                    a_list = {};
                    a_list['href'] = a_link
                    a_list['text'] = a_text
                    a_list['code'] = code
                    a_list['content_id'] = content_id
                    a_list['src'] = ''
                    a_list['lang'] = lang
                    # self.outputer.output(a_list)
                    self.content_list.append(a_list)


    def _get_img_src(self,soup,content_id,lang):
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
                image['href'] = ''
                image['text'] = ''
                image['content_id'] = content_id
                image['lang'] = lang
                self.content_list.append(image)

    def _get_email_list(self,soup,content_id):
        email_list = []
        a_tags = soup.find_all('a')
        for a_tag in a_tags:
            a_href = a_tag['href'].encode('utf-8')
            a_text = a_tag.get_text().encode('utf-8')
            if 'http://' not in a_href:
                if 'mailto:' in a_href:
                    code = self._get_url_code(a_href)
                    if code is not None and code != 0 :
                        email = {}
                        email['href'] = a_href
                        email['text'] = a_text
                        email['code'] = code
                        email['content_id'] = content_id
                        email['src'] = ''
                        self.content_list.append(email)

        return email_list

    def _get_url_code(self,url):
        if url is None or url == '':
            return None
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }
        print self.count
        print url
        try:
            req = urllib2.Request(url, headers=headers)
            res = urllib2.urlopen(req,timeout=20)
            # print res.getcode()
            print 'code : %d' % (res.getcode())
            code = 0
        except urllib2.HTTPError, e:
            code = e.code
        except urllib2.URLError, e:
            # print url
            print 'reason : %s' % e.reason
            code = 0
        except socket.error,e:
            print 'socket : %s' % e.message
            code = 0
        except httplib.error,e:
            print 'httplib: %s' % e.message
            code = 0
        except :
            print 'other except'
            code = 0
        else:
            code = 0
        print code
        self.count += 1
        return code

    def add_url_list(self,content_data):
        soup = BeautifulSoup(content_data['content_en'], "html.parser", from_encoding="utf-8")
        self._get_a_href(soup,content_data['content_id'],'en')
        self._get_img_src(soup,content_data['content_id'],'en')
        # self._get_email_list(soup,content_data['content_id'])
        soup1 = BeautifulSoup(content_data['content_zh'], "html.parser", from_encoding="utf-8")
        self._get_a_href(soup1, content_data['content_id'],'zh')
        self._get_img_src(soup1, content_data['content_id'],'zh')
        # self._get_email_list(soup1, content_data['content_id'])




    def have_url_list(self):
        return len(self.content_list) != 0

    def get_url(self):
        new_list = self._judge_url()
        return new_list

    def _judge_url(self):
        if self.have_url_list():
            url = self.content_list.pop()
            if url in self.content_old_list :
                self._judge_url()
            else:
                self.content_old_list.append(url)
        else :
            url = {}
        return url





