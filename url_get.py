# coding:utf-8
import my_sql
import HTMLParser
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class UrlGet():

    def __init__(self):
        self.iscon = True
        self.new_lists = []
        self.old_lists = []
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
        print "sql_page: %d " % self.page
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
            # txt_en = self.replace_html(content[1])
            # txt_zh = self.replace_html(content[2])


            html_parser = HTMLParser.HTMLParser()
            txt_en = html_parser.unescape(content[1])
            txt_zh = html_parser.unescape(content[2])

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
            html_parser = HTMLParser.HTMLParser()

            # sidebar_en = self.replace_html(content[1])
            # sidebar_zh = self.replace_html(content[2])

            sidebar_en = html_parser.unescape(content[1])
            sidebar_zh = html_parser.unescape(content[2])

            list_tmp['content_id'] = content[0]
            list_tmp['content_en'] = sidebar_en
            list_tmp['content_zh'] = sidebar_zh
            self.new_lists.append(list_tmp)
            list_tmp = {}
            # member_publications_en = self.replace_html(content[3])
            # member_publications_zh = self.replace_html(content[4])
            member_publications_en = html_parser.unescape(content[3])
            member_publications_zh = html_parser.unescape(content[4])
            list_tmp['content_id'] = content[0]
            list_tmp['content_en'] = member_publications_en
            list_tmp['content_zh'] = member_publications_zh
            self.new_lists.append(list_tmp)
            list_tmp = {}
            # member_outteam_en = self.replace_html(content[5])
            # member_outteam_zh = self.replace_html(content[6])
            member_outteam_en = html_parser.unescape(content[5])
            member_outteam_zh = html_parser.unescape(content[6])
            list_tmp['content_id'] = content[0]
            list_tmp['content_en'] = member_outteam_en
            list_tmp['content_zh'] = member_outteam_zh
            self.new_lists.append(list_tmp)



    def haveContentArr(self):
        print self.new_lists
        return len(self.new_lists) != 0



    def add_content_list(self):

        content_list = self._get_content_by_sql()
        print 'sqldata_nums : %d'% len(content_list)
        if len(content_list) > 0 :
            if self.is_content == True:
                self.getContent(content_list)
            else:
                self.getContentMember(content_list)




    def get_new_list(self):
        new_list = self._judge_list()
        return new_list

    def _judge_list(self):
        if self.haveContentArr():
            list = self.new_lists.pop()
            if list in self.old_lists :
                self._judge_list()
            else:
                self.old_lists.append(list)
        else :
            list = {}
        return list

    def test(self):
        list = self._get_content_by_sql()
        print list[0]
        html_parser = HTMLParser.HTMLParser()
        title = list[0][2]
        new = html_parser.unescape(title)
        print new

if __name__ == '__main__':

    getdata = UrlGet()
    getdata.test()
