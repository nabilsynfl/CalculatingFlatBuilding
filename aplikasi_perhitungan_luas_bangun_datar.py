# -*- coding: utf-8 -*-
"""
Created on Sun May  1 14:12:31 2022

@author: User
"""

def segiempat():
    print("Menghitung luas segi empat")
    panjang = int(input("Panjang = "))
    lebar = int(input("lebar = "))
    print("luas = " + str(panjang * lebar))

def segitiga():
    print("Menghitung luas segitiga")
    alas = int(input("Alas = "))
    tinggi = int(input("Tinggi = "))
    print("Luas = " + str(alas*tinggi/2))
    
def layang2():
    print("Menghitung luas layang-layang")
    diagonal1 = int(input("Diagonal 1 = "))
    diagonal2 = int(input("Diagonal 2 = "))
    print("Luas = " + str(diagonal1*diagonal2/2))
    
def trapesium():
    print("Menghitung Luas Trapesium")
    atap = int(input("Atap = "))
    lantai = int(input("Lantai = "))
    tinggi = int(input("Tinggi = "))
    print("Luas = " + str((atap + lantai) * (tinggi/2)))
    
def exit():
    print("Terima kasih sudah menggunakan program ini")
    
def show_menu():
    print("\n")
    print("-------- MENU ----------")
    print("[1] Menghitung luas Segiempat")
    print("[2] Mengitung luas segitiga")
    print("[3] Mengitung luas layang - layang")
    print("[4] Menghitung Luas trapesium")
    print("[5] Exit")
    
    menu = int(input("Pilih menu >> "))
    print("\n")
    
    if menu == 1:
        segiempat()
    elif menu == 2:
        segitiga()
    elif menu == 3:
        layang2()
    elif menu == 4:
        trapesium()
    elif menu == 5:
        exit()
    else:
        print("Menu tidak tersedia")


print("Aplikasi menghitung luas bangun datar")
jawab = 'y'
while(jawab == 'y'):
    show_menu()
    jawab = input("Ingin mengulang program (y/n) ? ")
    if jawab != 'y':
        break
        
        
