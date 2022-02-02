import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="perpustakaan"
)

mycursor=mydb.cursor()
sql = """CREATE TABLE customers (
  customers_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  address Varchar(255)
)
"""
mycursor.execute(sql)

print("Tabel pengunjung berhasil dibuat!")
