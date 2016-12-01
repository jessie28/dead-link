# coding:utf-8
import urllib2
import datetime
text = 'adad'
if 'a' not in text:
    print 'ok';
else :
    print "not ok"

url3 = 'https://www.beaconevents.com/?regsite=36&form=1&dm_i=1RTV%2C239LN%2CDQ1ATH%2C7JJ9M%2C1'
url1 = 'http://static1.squarespace.com/static/557dd429e4b035c8591b78e0/t/5745ee0ee32140a28f3a6e9b/1464200719637/Traditional_Remittances.pdf'
url2 = 'http://www.ukcba.com/2014/04/the-1st-china-uk-business-leaders-summit/'
url4 = 'http://www.chinagoabroad.com/zh/recent_transaction/anbang-insurance-s-unit-completes-the-300m-acquisition-of-south-korean-woori-bank'
url5 = 'https://es.linkedin.com/in/m-mercè-pujadas-casas-47b68216'
url6 = 'http://www.baidu.com'


req = urllib2.Request(url6)

try:
    res = urllib2.urlopen(req,timeout=20)
    # code = res.getcode()
except urllib2.HTTPError, e:
    print e.reason
    print e.code
    code = e.code
except urllib2.URLError, e:
    print e.reason

list = []

list.append('1')
list.append('2')

print list

list.pop()

print list

print datetime.date.today()
time = str(datetime.date.today())
print  time
print isinstance(time,str)

lists = []
data1 = {'name':'zz','sex':2}
lists.append(data1)
data2 = {'name':'zz','sex':2}
if data2 in lists :
    pass
else :
    lists.append(data2)
print data1 == data2
print lists

test_list1 = {}
if test_list1:
    print 'ok'
else :
    print  'no'

print "\xe5\x8a\xa0\xe5\x85\xa5\xe6\x88\x91\xe4\xbb\xac".decode('uft-8')



