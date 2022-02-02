import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="perpustakaan"
)

def insert_pinjaman(mydb):
    kelas = input("\nMasukan Kelas: ")
    Judul_Buku = input("Masukan Judul Buku: ")
    val = (kelas, Judul_Buku)
    mycursor = mydb.cursor()
    sql = "INSERT INTO pengunjung (kelas, Judul_Buku ) VALUES (%s, %s)"
    mycursor.execute(sql, val)
    mydb.commit()
    print("{} data berhasil disimpan".format(mycursor.rowcount))
    
def insert_data(mydb):
    name = input("\nMasukan nama: ")
    address = input("Masukan absen: ")
    val = (name, address)
    mycursor = mydb.cursor()
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    mycursor.execute(sql, val)
    mydb.commit()
    print("{} data berhasil disimpan".format(mycursor.rowcount))
    insert_pinjaman(mydb)
    




def show_data(mydb):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM customers"
    mycursor.execute(sql)
    results = mycursor.fetchall()

    if mycursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)

    mycursor = mydb.cursor()
    sql = "SELECT * FROM pengunjung"
    mycursor.execute(sql)
    results = mycursor.fetchall()

    if mycursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)

def update_pinjaman(mydb):
    mycursor = mydb.cursor()
    show_data(mydb)
    customer_id = input("\npilih id pengunjung> ")
    kelas = input("\nMasukan Kelas: ")
    Judul_Buku = input("Masukan Judul Buku: ")

    sql = "UPDATE customers SET kelas=%s, Judul_Buku=%s WHERE pengunjung_id=%s"
    val = (kelas, Judul_Buku, pengunjung_id)
    mycursor.execute(sql, val)
    mydb.commit()
    print("{} data berhasil diubah".format(mycursor.rowcount))

def update_data(mydb):
    mycursor = mydb.cursor()
    show_data(mydb)
    customers_id = input("pilih id customers> ")
    name = input("Nama baru: ")
    address = input("Absen Baru: ")

    sql = "UPDATE customers SET name=%s, address=%s WHERE customers_id=%s"
    val = (name, address, customers_id)
    mycursor.execute(sql, val)
    mydb.commit()
    print("{} data berhasil diubah".format(mycursor.rowcount))
    update_pinjaman(mydb)

def delete_pinjaman(mydb):
    mycursor = mydb.cursor()
    print("\n")
    show_data(mydb)
    print("hapus juga data pinjaman")
    customer_id = input("pilih id pengunjung> ")
    sql = "DELETE FROM pengunjung WHERE pengunjung_id=%s"
    val = (customer_id,)
    mycursor.execute(sql, val)
    mydb.commit()
    print("{} data berhasil dihapus".format(mycursor.rowcount))


def delete_data(mydb):
    mycursor = mydb.cursor()
    show_data(mydb)
    customer_id = input("pilih id customers> ")
    sql = "DELETE FROM customers WHERE customers_id=%s"
    val = (customer_id,)
    mycursor.execute(sql, val)
    mydb.commit()
    print("{} data berhasil dihapus".format(mycursor.rowcount))
    delete_pinjaman(mydb)

def search_pinjaman(mydb):
    mycursor = mydb.cursor()
    keyword = input("Kata kunci: ")
    sql = "SELECT * FROM pengunjung WHERE kelas LIKE %s OR Judul_Buku LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword))
    mycursor.execute(sql, val)
    results = mycursor.fetchall()

    if mycursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)


def search_data(mydb):
    mycursor = mydb.cursor()
    keyword = input("Kata kunci: ")
    sql = "SELECT * FROM customers WHERE name LIKE %s OR address LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword))
    mycursor.execute(sql, val)
    results = mycursor.fetchall()

    if mycursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)


def show_menu(mydb):
    print("\n=== APLIKASI DATABASE PYTHON ===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("6. Cari Pinjaman")
    print("7. Hapus Pinjaman")
    print("8. Hapus Nama Pengunjung")
    print("0. Keluar")
    print("------------------")
    menu = input("Pilih menu> ")

   

    if menu == "1":
        insert_data(mydb)
    elif menu == "2":
        show_data(mydb)
    elif menu == "3":
        update_data(mydb)
    elif menu == "4":
        delete_data(mydb)
    elif menu == "5":
        search_data(mydb)
    elif menu == "6":
        search_pinjaman(mydb)
    elif menu == "7":
        delete_pinjaman(mydb)
    elif menu == "8":
        delete_data(mydb)
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")


if __name__ == "__main__":
    while (True):
        show_menu(mydb)



