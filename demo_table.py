import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

create_demo_table = """
CREATE TABLE demo (
    s charvar(1),
    x INT,
    y INT
)
"""
curs.execute(create_demo_table)

insert_demo = """
INSERT INTO demo
(s,
x,
y
)
VALUES
('s',
 5,
 7),
('v',
5,
7),
('f',
8,
7);"""

#insert_demo = """
##INSERT INTO demo
#(s, x, y)
#VALUES """

curs.execute(insert_demo)

conn.commit()

query = 'SELECT COUNT(*) FROM demo;'
result = curs.execute(query).fetchall()[0][0]
print(result)

query2 = """SELECT COUNT(*) FROM demo
WHERE x >= 5 AND y >= 5;"""
result2 = curs.execute(query2).fetchall()[0][0]
print(result2)

query3 = """SELECT COUNT(DISTINCT (y)) FROM demo;"""
result3 = curs.execute(query3).fetchall()[0][0]
print(result3)
