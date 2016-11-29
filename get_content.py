# -*- coding: UTF-8 -*-
import my_sql
import get_list
import HTMLParser
import sys

class check_url():
    def getContent(self,p=1):
        limit = 2
        if p == 1:
            page = 0
        else:
            page = limit * ( p -1 )
        # page = bytes(page)
        # limit = bytes(limit)
        sql = "select id,content_en,content_zh,status_en,status_zh from content where (status_en = 1 or status_zh = 1) and (content_zh <> '' or content_en <> '') order by id limit %d , %d " % (page,limit)
        sql_obj = my_sql.mysql()
        sql_res = sql_obj.selectsql(sql)
        lists = []
        reload(sys)
        sys.setdefaultencoding('utf-8')
        for index in sql_res:
            i = 0
            list_tmp = []
            for row in index:
                html_parser = HTMLParser.HTMLParser()
                if i == 1 or i == 2:
                    txt = self.replace_html(index[i])
                    # print txt
                    # print index[i]
                    # index[i].encode('utf-8')
                    # sys.setdefaultencoding('utf-8')
                    # html_parser.unescape(txt)
                    # unicode(index[i], "utf-8")
                    # list_tmp.append(html_parse.unescape(index[i]))
                    list_tmp.append(html_parser.unescape(txt))
                else :
                    list_tmp.append(index[i])
                i += 1
            lists.append(list_tmp)

        return lists

    def replace_html(self,s):
        s = s.replace('&quot;', '"')
        s = s.replace('&amp;', '&')
        s = s.replace('&lt;', '<')
        s = s.replace('&gt;', '>')
        s = s.replace('&nbsp;', ' ')
        return s




obj_sql = check_url()
sql_list = obj_sql.getContent()
get_list = get_list.get_list()

for row in sql_list:
    all_list = []
    content_id = row[0]
    print content_id
    list = get_list.parse(row[1])
    if list[0]:
        for a in list[0]:
            print a
            a_tag = {};
            a_tag['content_id'] = content_id
            a_tag['src'] = ''
            a_tag['code'] = a['code']
            a_tag['href'] = a['href']
            a_tag['text'] = a['text']
            all_list.append(a_tag)
    if list[1]:
        for i in list[1]:
            print i
            img = {};
            img['content_id'] = content_id
            img['src'] = i['src']
            img['code'] = i['code']
            img['href'] = ''
            img['text'] = ''
            all_list.append(img)
    if list[2]:
        for e in list[2]:
            print e
            e_tag = {};
            e_tag['content_id'] = content_id
            e_tag['src'] = ''
            e_tag['code'] = a['code']
            e_tag['href'] = a['href']
            e_tag['text'] = a['text']
            all_list.append(e_tag)

    print all_list