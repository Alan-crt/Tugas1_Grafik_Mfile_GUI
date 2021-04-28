# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 23:55:56 2021

@author: prasetyo

Lalan Agung P
123150049
Praktikum SCPK
IF-E
"""
print("Menghitung luas dan volume Balok")
panjang = int(input("Masukkan Panjang balok: "))
lebar= int(input("Masukkan lebar balok: "))
tinggi= int(input("Masukkan tinggi balok: "))

volume = panjang * lebar * tinggi
luas = 2*(panjang*lebar + panjang*tinggi + lebar*tinggi)
print("Total volume balok: ", volume)
print("Total luas balok: ", luas)