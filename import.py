import csv
import sqlite3

archivo = open(r"C:\Users\52999\Documents\Coding Python\importData\coding.tsv", newline = '')
filas = csv.reader(archivo, delimiter='\t')
lista = list(filas)
del (lista[0])
tupla = tuple(lista)

print(tupla)

# insertar

conexion = sqlite3.connect("talents_code.db")
cursor = conexion.cursor()
cursor.executemany("INSERT INTO registros ('comprador','descripcion','precio','total_items','direccion_vendedor','vendedor') VALUES (?,?,?,?,?,?)",tupla)

conexion.commit()
conexion.close()