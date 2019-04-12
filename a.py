import MySQLdb
try:
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="1234",
        db="news",
        charset='utf8')
except MySQLdb.Error as e:
    print('Error: %s' % e)
cursor = conn.cursor()
cursor.execute('SELECT * FROM `news` ;')
rest1 = cursor.fetchone()
print(rest1)