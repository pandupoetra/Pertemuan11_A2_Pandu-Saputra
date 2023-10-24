def tambah():
    a=int(input("masukan nilai pertama = "))
    b=int(input("masukan nilai kedua = "))
    hasil=a+b
    print("hasil penjumlahannya adalah =",hasil)

def kurang():
    a=int(input("masukan nilai pertama = "))
    b=int(input("masukan nilai kedua = "))
    hasil=a-b
    print("hasil pengurangannya adalah =",hasil)

def bagi():
    a=int(input("masukan nilai pertama= "))
    b=int(input("masukan nilai kedua= "))
    hasil=a/b
    print("hasil pembagiannya adalah =",hasil)

def kali():
    a=int(input("masukan nilai pertama="))
    b=int(input("masukan nilai kedua="))
    hasil=a*b
    print("hasil perkaliannya adalah =",hasil)

def menu():
    teks="Kalkulator kita"
    while True:
        print("=================================")
        print("|"+teks.center(31," ")+"|")
        print("=================================")
        print("1. Penambahan")
        print("2. Pengurangan")
        print("3. Pembagian")
        print("4. Perkalian")
        print("5. Keluar")
        pilihan=input("Pilih menu dulu deck= ")
        print("=================================")
        if pilihan=="1":
            tambah()
        elif pilihan=="2":
            kurang()
        elif pilihan=="3":
            bagi()
        elif pilihan=="4":
            kali()
        elif pilihan=="5":
            break
        else:
            print("nomor yang anda masukan tidak sesuai, silahkan coba kembali!!")

menu()
  


