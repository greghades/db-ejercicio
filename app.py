import sqlite3

try:
    conection = sqlite3.connect('crud-loopgk.DB')
    cursor = conection.cursor()
    #cursor.execute("CREATE TABLE users (name TEXT, lastname TEXT, job_title TEXT,mail TEXT, password TEXT)")
except:
    print("Error en conexion")



def createRegister(name, lastname, job_title, mail,password):
    
    query = f"INSERT INTO users VALUES (NULL,'{name}','{lastname}','{job_title}','{mail}','{password}')"
    cursor.execute(query)
    conection.commit()

def readRegister():
    query = "SELECT * FROM users"
    elemets = cursor.execute(query).fetchall()

    return elemets


def updateRegister(pk,name, lastname, job_title, mail,password):
    query = f"""
    UPDATE users
    SET name = '{name}', lastname = '{lastname}', job_title = '{job_title}', mail = '{mail}', password = '{password}'
    WHERE pk = {pk}; 
    """ 
    cursor.execute(query)
    conection.commit()

def deleteRegister(id):
    query = f"DELETE FROM users WHERE pk = {id}"
    cursor.execute(query)
    conection.commit()



def menu():
    opcion = True
    while(opcion):
        print("Digite la opcion a realizar")
        print("1. Crear Registro: ")
        print("2. Leer registros")
        print("3. Actualizar Registros")
        print("4. Borrar Registro")
        print("0. Para salir")
        opcion = int(input("Opcion: "))

        if(opcion == 1):
            name = input("Digite su nombre: ")
            lastname = input("Digite su apellido: ")
            jobtitle = input("Diga su trabajo: ")
            mail = input("Diga su mail: ")
            password = input("Diga su password: ")
            createRegister(name,lastname,jobtitle,mail,password)
        
        elif(opcion == 2):
            print(readRegister())
        
        elif(opcion == 3):
            print("Digite los campos que desea actualizar")
            print(readRegister())
            pk = int(input("Id del campo a actualizar"))
            name = input("Digite su nombre: ")
            lastname = input("Digite su apellido: ")
            jobtitle = input("Diga su trabajo: ")
            mail = input("Diga su mail: ")
            password = input("Diga su password: ")
            updateRegister(pk,name,lastname,jobtitle,mail,password)
        elif(opcion == 4):
            pk = int(input("Id del campo a eliminar"))
            deleteRegister(pk)

menu()
