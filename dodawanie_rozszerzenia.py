#!/usr/bin/python
import os

os.chdir('E:\\CL_moduls')
lista_podkatalogow=os.listdir('E:\CL_moduls')

for podkatalog in lista_podkatalogow:
    sciezka_podkatalogu = os.path.join('E:\\CL_moduls\\', podkatalog)
    os.chdir(sciezka_podkatalogu)
    for plik in os.listdir(sciezka_podkatalogu):
        os.rename(plik, plik +'.pdf')

