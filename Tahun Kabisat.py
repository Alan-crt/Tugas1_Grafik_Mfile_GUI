# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 23:39:39 2021

@author: prasetyo

Lalan Agung Prasetyo
123150049
Praktikum SCPK
IF-E
"""

tahun = int(input("Masukkan Tahun: "))

if tahun % 400 == 0:
    print("{} merupakan tahun kabisat".format(tahun))
elif tahun % 100 == 0:
    print("{} bukan tahun kabisat".format(tahun))
elif tahun % 4 == 0:
    print("{} merupakan tahun kabisat".format(tahun))
else:
    print("{} bukan tahun kabisat".format(tahun))