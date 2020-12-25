import time
import os
import pandas as pd
from sklearn import tree

def slp(a):
    time.sleep(a)

def copyright():
    print(time.ctime())
    print("(c) 2020 Kelompok 3 . All rights reserved.")

def opsi1():
    data = pd.read_csv("hasil.csv")
    print("")
    print("="*53," DATA DISTRIBUSI JARINGAN  ","="*53)
    print(data)
    print("="*135)

    y = data.iloc[:, 0]
    X = data.iloc[:,1:12:2]
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X,y)

    print("\n[*] Analisis tipe gangguan")
    Ea = float(input("\n[?] Masukan nilai Ea : "))
    Eb = float(input("[?] Masukan nilai Eb : "))
    Ec = float(input("[?] Masukan nilai Ec : "))
    Ia = float(input("[?] Masukan nilai Ia : "))
    Ib = float(input("[?] Masukan nilai Ib : "))
    Ic = float(input("[?] Masukan nilai Ic : "))
    predicition = clf.predict([[Ea,Eb,Ec,Ia,Ib,Ic]])

    def a():
        tulis = ("[-] Menurut data yang telah di input, data tersebut termasuk ke dalam gangguan : ")
        return tulis

    print("\n[*] Output Metode Machine Learning")
    print(a(),predicition)
    print("\n[*] Output Metode Kondisi")
    if Ea<Eb<Ec and Eb-Ea>0.5 and Ea-Eb>0.001 or Ib<Ic<=Ia:
        print(a(),"SLGFa")
    elif Eb<Ec<Ea and Ec-Eb>0.5 and Eb-Ea>0.001 or Ic<Ia<=Ib:
        print(a(),"SLGFb")
    elif Ec<Ea<Eb and Ea-Ec>0.5 and Eb-Ea>0.001 or Ia<Ib<Ic:
        print(a(),"SLGFc")
    elif Eb<Ea<Ec and Ea-Eb<1.0 and Ec-Ea<10 or Ic<Ia<Ib or Ic<Ib<Ia:
        print(a(),"DLGFab")
    elif Ea<Ec<Eb and Ec-Ea<1.0 and Eb-Ec<10 or Ib<Ic<Ia or Ib<Ia<Ic:
        print(a(),"DLGFac")
    elif Ec<Eb<Ea and Eb-Ec<10.0 and Ea-Eb<10 or Ia<Ib<Ic or Ia<Ic<Ib:
        print(a(),"DLGFbc")
    elif Eb<Ea<Ec or Eb<Ec<Ea and Ec-Eb<5.0 and Ea-Ec<5.0 or Ic<Ib<Ia or Ic<Ia<Ib:
        print(a(),"DLFab")
    elif Ec<Eb<Ea or Ec<Ea<Eb and Ea-Ec<5.0 and Eb-Ea<5.0 or Ia<Ic<Ib or Ia<Ib<Ic:
        print(a(),"DLFbc")
    elif Ea<Eb<Ec or Ea<Ec<Eb and Eb-Ea<5.0 and Ec-Eb<5.0 or Ib<Ia<Ic or Ib<Ic<Ia:
        print(a(),"DLFac")
    elif Ea==Eb==Ec or Ia==Ib==Ic:
        print(a(),"TPF")
    slp(1)
    ulang1()

def opsi2():
    print("  _  __    _                             _       ____  ")
    print(" | |/ /   | |                           | |     |___ \ ")
    print(" | ' / ___| | ___  _ __ ___  _ __   ___ | | __    __) |")
    print(" |  < / _ \ |/ _ \| '_ ` _ \| '_ \ / _ \| |/ /   |__ < ")
    print(" | . \  __/ | (_) | | | | | | |_) | (_) |   <    ___) |")
    print(" |_|\_\___|_|\___/|_| |_| |_| .__/ \___/|_|\_\  |____/ ")
    print("                            | |                        ")
    print("                            |_|                        ")
    print("\n[*] Anggota\n")
    print("[1] Adrian Jonathan      (162012433060)")
    print("[2] Ola Claudia          (162012433064)")
    print("[3] Muhammad Cory        (162012433073)")
    print("[4] Febriano Andhika M   (162012433074)")
    print("[5] Adnan Purnama        (162012433078)")
    print("\n[*] Special Thanks To : Bu Lilik Jamilatul Awalin")
    slp(1)
    ulang2()

def keluar():
    print("[*] Terima kasih telah menggunakan Program ini")
    slp(2)
    exit()

def ulang1():
    pilih = input("\n[?] Keluar (y/n) : ").lower()
    if pilih == "y":
        keluar()
    elif pilih == "n":
        os.system("CLS")
        copyright()
        slp(2)
        menu()
    else:
        print("[-] Pilihan salah, ulangi program")
        slp(1)
        os.system("CLS")
        copyright()
        menu()

def ulang2():
    pilih = input("\n[?] Keluar (y/n) : ").lower()
    if pilih == "y":
        keluar()
    elif pilih == "n":
        os.system("CLS")
        copyright()
        slp(2)
        menu()
    else:
        print("[-] Pilihan salah, ulangi")
        slp(1)
        os.system("CLS")
        copyright()
        opsi2()
        
def opsi():
    pilih = input("[?] Pilih : ")
    if pilih == "1":
        os.system("CLS")
        copyright()
        slp(1)
        opsi1()
    elif pilih == "2":
        os.system("CLS")
        copyright()
        slp(1)
        opsi2()
    elif pilih == "3":
        os.system("CLS")
        copyright()
        slp(1)
        keluar()
    else:
        print("[-] Pilihan salah, ulangi")
        slp(1)
        os.system("CLS")
        copyright()
        menu()

def menu():
    print("")
    print("="*4," Menu ","="*4)
    print("\n[1] Run Program")
    print("[2] Info")
    print("[3] Exit\n")
    opsi()

def main():
    copyright()
    slp(1)
    menu()

if __name__ == "__main__":
    main()