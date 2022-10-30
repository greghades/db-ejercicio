from ctypes import create_unicode_buffer
import sqlite3
from xml.dom.minidom import Element

from colorama import Cursor

try:
    conection = sqlite3.connect('crud-loopgk')
    cursor = conection.cursor()
    #cursor.execute("CREATE TABLE users (name TEXT, lastname TEXT, job_title TEXT,mail TEXT, password TEXT)")
except:
    print("Error en conexion")



def createRegister(name, lastname, job_title, mail,password):
    
    query = f"INSERT INTO users VALUES ('{name}','{lastname}','{job_title}','{mail}','{password}')"
    cursor.execute(query)
    conection.commit()

def readRegister():
    query = "SELECT * FROM users"
    elemets = cursor.execute(query).fetchall()

    return elemets


# def updateRegister(name="", lastname="", job_title="", mail="",password=""):
#     query = "ALTER TABLE users "

def deleteRegister(id):
    query = f"DELETE FROM users WHERE users_pk = {id}"
    cursor.execute(query)
    conection.commit()


# createRegister('Alejandra','Palacios','Maestra','aleja@gmail.com','543124')
deleteRegister(1)
print(readRegister())