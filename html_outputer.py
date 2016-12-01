# coding:utf-8
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')
class HtmlOutputer():
    def __init__(self):
        # self.firsttime = True
        self.linenum = 0
        self.data = []
        self.old_data = []

    def collect_data(self,content):
        self.data.append(content)

    def output(self):
        filename = './%s_link.xls ' % (str(datetime.date.today()))
        if self.linenum == 0 :
            self.makeOutput(filename)
        for content in self.data :
            if content in self.old_data :
                pass
            else:
                self.linenum += 1
                print 'linenum : %d' % self.linenum
                print content
                self.old_data.append(content)
                rb = open_workbook(filename)
                sh = rb.sheet_by_index(0)
                wb = copy(rb)
                ws = wb.get_sheet(0)
                print content['text']
                try:
                    txt = content['text'].decode('utf-8')
                except:
                    txt = 'None'
                print txt
                ws.write(self.linenum, 0, content['content_id'])
                ws.write(self.linenum, 1, content['lang'])
                ws.write(self.linenum, 2, content['code'])
                ws.write(self.linenum, 3, content['href'])
                ws.write(self.linenum, 4, txt)
                ws.write(self.linenum, 5, content['src'])
                wb.save(filename)

        self.data = []

    def hasData(self):
        return len(self.data) != 0

    def makeOutput(self,filename):
        workbook = xlwt.Workbook(encoding = 'utf-8')
        sheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=False)
        sheet1.write(0, 0, 'content_id')
        sheet1.write(0, 1, 'lang')
        sheet1.write(0, 2, 'code')
        sheet1.write(0, 3, 'href')
        sheet1.write(0, 4, 'text')
        sheet1.write(0, 5, 'src')
        workbook.save(filename)


    def test1(self,filename1):
        rb = open_workbook(filename1)
        sh = rb.sheet_by_index(0)
        wb = copy(rb)
        ws = wb.get_sheet(0)
        ws.write(0,1,'\xb5\xcf\xe5\xc8\xb0\xc2\xcc\xd8\xc2\xfc\xc8\xab\xbc\xaf'.decode('gb2312').decode('utf-8'))
        wb.save(filename1)

if __name__ == '__main__':
    output = HtmlOutputer()
    filename1 = './%s_test.xls ' % (str(datetime.date.today()))
    output.makeOutput(filename1)
    output.test1(filename1)
