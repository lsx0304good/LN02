import pymysql

db = pymysql.connect('localhost', 'root', 'pwd', 'SimonDB')
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('database version: %s' % data)
db.close()
