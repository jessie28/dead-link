# -*- coding: UTF-8 -*-
import my_sql
import HTMLParser

class check_url():
    def getContent(self,p=1):
        limit = 2
        if p == 1:
            page = 0
        else:
            page = limit * ( p -1 )
        page = bytes(page)
        limit = bytes(limit)
        sql = "select id,content_en,content_zh,status_en,status_zh from content where (status_en = 1 or status_zh = 1) and (content_zh <> '' or content_en <> '') order by id limit "+ page + "," + limit
        sql_obj = my_sql.mysql()
        sql_res = sql_obj.selectsql(sql)
        key = 0
        lists = []
        for index in sql_res:
            i = 0
            list_tmp = []
            for row in index:
                html_parse = HTMLParser.HTMLParser()
                if i == 1 or i == 2:
                    # print index[i]
                    index[i].encode('utf-8')
                    # list_tmp.append(html_parse.unescape(index[i]))
                else :
                    list_tmp.append(index[i])
                i += 1
            lists.append(list_tmp)
            key += 1

        print (lists)

obj_sql = check_url()
obj_sql.getContent()