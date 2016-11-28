import MySQLdb

db = MySQLdb.connect("192.168.1.96","cga","cga123","cga_union")

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


