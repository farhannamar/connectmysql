import pymysql

# Koneksi ke Database My SQL
db = pymysql.connect(host="localhost",
                     user="root",
                     password="",
                     db="mahasiswa" )

#memanggil fungsi kursor
cursor = db.cursor()

#Menampilkan isi tabel  menggunakan fungsi fecth()

cursor.execute("SELECT * FROM datamahasiswa")
row = cursor.fetchone()
while row is not None:
  print(row)
  row = cursor.fetchone()
  
#Melakukan perintah Insert

cursor.execute("INSERT INTO datamahasiswa (id, nim, nama, alamat) VALUES ('17','113223','richard','newyork')")

#Melakukan perintah Update 
cursor.execute("UPDATE datamahasiswa SET nama = 'Farhanna' where id='17'")

#hasil
cursor.execute("SELECT * FROM datamahasiswa where id='17'")
row = cursor.fetchone()
print(row)

# memutuskan koneksi
db.close()
