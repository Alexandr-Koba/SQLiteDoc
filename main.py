import sqlite3

db = sqlite3.connect('kobaDB')

c = db.cursor()
#c.execute(""" CREATE TABLE product (
#    name text,
#   price integer,
#   id_product integer,
#    vendor_name text,
#    manufacture text,
#    category text
#)""")

#c.execute("INSERT INTO product VALUES ('Газонокосилка ЗУБР', 10700, 12344448, 'Барыги Бля', 'ОАО ПИЗО', 'Для Дачи')")

c.execute("SELECT rowid, * FROM product")

#c.execute("DELETE FROM product WHERE rowid = 2")
print(c.fetchall())

db.commit()

db.close()