# coding:utf-8
import my_sql
import HTMLParser
import sys
class UrlGet():

    def __init__(self):
        self.iscon = True
        self.new_lists = []
        self.page = 0
        self.content_member_page = 0
        self.isempty = False
        self.is_content = True

    def replace_html(self,s):
        s = s.replace('&quot;', '"')
        s = s.replace('&amp;', '&')
        s = s.replace('&lt;', '<')
        s = s.replace('&gt;', '>')
        s = s.replace('&nbsp;', ' ')
        return s

    def _get_content_by_sql(self):
        self.isempty = False
        self.page += 1
        print self.page
        limit = 2
        if self.page == 1:
            p = 0
        else:
            p = limit * (self.page - 1)
        if self.iscon == True:
            self.is_content = True
            sql = "select id,content_en,content_zh,status_en,status_zh from content where (status_en = 1 or status_zh = 1) and (content_zh <> '' or content_en <> '') order by id limit %d , %d " % (
            p, limit)
            sql_obj = my_sql.mysql()
            sql_res = sql_obj.selectsql(sql)
            if len(sql_res) < limit:
                self.iscon = False
                self.page = 0
        else:
            self.is_content = False
            sql = "select content_id,sidebar_en,sidebar_zh,member_publications_en,member_publications_zh,member_outteam_en,member_outteam_zh from content_member order by id limit %d,%d" % (
            p, limit)
            sql_obj = my_sql.mysql()
            sql_res = sql_obj.selectsql(sql)

        return sql_res

    def _get_content_member_by_sql(self,p):
        self.isempty = False
        limit = 2
        if p == 1:
            page = 0
        else:
            page = limit * (p - 1)
        sql = "select content_id,sidebar_en,sidebar_zh,member_publications_en,member_publications_zh,member_outteam_en,member_outteam_zh from content_member order by id limit %d,%d"% (page,limit)
        sql_obj = my_sql.mysql()
        sql_res = sql_obj.selectsql(sql)
        return sql_res

    def getContent(self,content_list):
        html_parser = HTMLParser.HTMLParser()
        for content in content_list:
            list_tmp = {}
            # content[2].encode('utf-8')
            txt_en = self.replace_html(content[1])
            txt_zh = self.replace_html(content[2])
            list_tmp['content_id'] = content[0]
            # list_tmp['content_en'] = html_parser.unescape(txt_en)
            # list_tmp['content_zh'] = html_parser.unescape(txt_zh)
            list_tmp['content_en'] = txt_en
            list_tmp['content_zh'] = txt_zh
            self.new_lists.append(list_tmp)

    def getContentMember(self,content_list):
        html_parser = HTMLParser.HTMLParser()
        for content in content_list:
            list_tmp = {}
            sidebar_en = self.replace_html(content[1])
            sidebar_zh = self.replace_html(content[2])
            list_tmp['content_id'] = content[0]
            list_tmp['content_en'] = html_parser.unescape(sidebar_en)
            list_tmp['content_zh'] = html_parser.unescape(sidebar_zh)
            self.new_lists.append(list_tmp)
            list_tmp = {}
            member_publications_en = self.replace_html(content[3])
            member_publications_zh = self.replace_html(content[4])
            list_tmp['content_id'] = content[0]
            list_tmp['content_en'] = html_parser.unescape(member_publications_en)
            list_tmp['content_zh'] = html_parser.unescape(member_publications_zh)
            self.new_lists.append(list_tmp)
            list_tmp = {}
            member_outteam_en = self.replace_html(content[5])
            member_outteam_zh = self.replace_html(content[6])
            list_tmp['content_id'] = content[0]
            list_tmp['content_en'] = html_parser.unescape(member_outteam_en)
            list_tmp['content_zh'] = html_parser.unescape(member_outteam_zh)
            self.new_lists.append(list_tmp)

    def haveContentArr(self):
        return len(self.new_lists) != 0



    def add_content_list(self):

        content_list = self._get_content_by_sql()
        if len(content_list) > 0 :
            if self.is_content == True:
                self.getContent(content_list)
            else:
                self.getContentMember(content_list)








    def get_new_list(self):
        new_list = self.new_lists.pop()
        return new_list