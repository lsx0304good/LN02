import pymysql

db = pymysql.connect('localhost', 'root', 'lisixiang945', 'SimonDB', charset='utf8')
cursor = db.cursor()

data = [
    ('book1', 'Python', '79.80', '2018-5-20'),
    ('book2', 'Java', '59.90', '2017-3-12'),
    ('book3', 'PHP', '88.50', '2018-8-16'),
    ('book4', 'C++', '69.80', '2018-12-26'),
]
try:
    cursor.executemany('INSERT INTO books(name, category, price, publish_time) VALUES (%s,%s,%s,%s)', data)
    db.commit()
except:
    db.rollback()

db.close()
