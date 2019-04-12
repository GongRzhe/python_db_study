import MySQLdb
class MysqlSearch(object):
    def __init__(self):
        self.get_conn()
    def get_conn(self):
        try:
            self.conn = MySQLdb.connect(
                host="localhost",
                port=3306,
                user="root",
                passwd="1234",
                db="news",
                charset='utf8')        
        except MySQLdb.Error as e:
            print('Error: %s' % e)
    def close_conn(self):
        try:
            if self.conn:
                self.conn.close()
        except MySQLdb.Error as e:
            print('Error: %s' % e)
    def get_one(self):
        sql='select * from `news` where `id`=%s;'
        cursor=self.conn.cursor()
        cursor.execute(sql,('2',))
        print(cursor.rowcount)
        print(dir(cursor))
        rest =cursor.fetchone()
        print(rest)
        cursor.close()
        self.close_conn()
def main():
    obj=MysqlSearch()
    obj.get_one()
if __name__ == "__main__":
    main()
