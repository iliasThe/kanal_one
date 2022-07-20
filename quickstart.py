import psycopg2

con = psycopg2.connect(
    database='PostgreSQL',
    user='user',
    password='054053',
    host='127.0.0.1',
    port='5354'
)

cur = con.cursor()
cur.execute('SELECT * FROM sample')
one = cur.fetchone()
all = cur.fetchall()

cur.execute('''
    CREATE TABLE values(
    id integer PRIMARY KEY,
    заказ  integer,
    стоимость$ integer,
    срокпоставки date,
    стоимость integer, 
)
''')


