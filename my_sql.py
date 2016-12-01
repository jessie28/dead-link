# coding:utf-8
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pymssql
# db = MySQLdb.connect("192.168.1.96","cga","cga123","cga_union",charset='utf8')
# db = pymssql.connect(server='192.168.1.96',user='cga', password='cga123',database='cga_union',charset='utf8')
db = MySQLdb.connect(host='192.168.1.96',user='cga', passwd='cga123',db='cga_union',charset='utf8')

class mysql():
    def selectsql(self,sql):
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            res = cursor.fetchall()
            return res
        except:
            print "Error: unable to fecth data"

    def changesql(self,sql):
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

    def closedb(self):
        db.close()


