import pymysql


db = pymysql.connect('localhost', 'root', 'lisixiang945', 'SimonDB')
cursor = db.cursor()
query = """
CREATE TABLE books (
id int NOT NULL AUTO_INCREMENT,
name varchar(50) NOT NULL,
category varchar(50) NOT NULL,
price decimal(10,2) DEFAULT NULL,
publish_time date DEFAULT NULL,
PRIMARY KEY (id)
) ENGINE = MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;
"""

cursor.execute(query)
db.close()