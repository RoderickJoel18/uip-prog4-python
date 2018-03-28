import time
import sqlite3
import os

# Se establece una conexion con la BD, para esto se debe colocar la ruta de dicha BD.
db = sqlite3.connect("C:\\Users\\roder\\OneDrive\\Documentos\\uip-prog4-python-master\\uip-prog4-python-master\\Taller#1_Libro\\Libro.db")

Opcion = 0

while True:
    print("\n\t\t\tLibros")
    print("\nSeleccione una de las siguientes acciones: ") # Menu de seleccion
    Opcion = int(input("\t1. Buscar un libro \n \t2. Agregar un libro \n \t3. Eliminar un libro \n\t4. Salir \n\nInserte lo que desea realizar: "))

    cursor = db.cursor()


    # Esta opcion es para buscar un libro por medio del ISBN.
    if Opcion == 1:
        ISBN = input("\nPara buscar un libro, favor ingresar su ISBN: ")
        cursor.execute('''SELECT Nombre, Autor FROM Libro WHERE ISBN = ?''', (ISBN,))

        Salida = cursor.fetchall()
        print("\t", Salida, "\n")
        db.commit()
        os.system("pause")

    # Esta opcion es para añadir un libro a la BD.
    elif Opcion == 2:
        while True:
            print("\nIntroduzca los siguientes datos solicitados: ")
            ISBN = input("\tISBN: ")
            Nombre = input("\tNombre del libro: ")
            Autor = input("\tNombre del autor: ")
            Publicacion = input("\tAño de publicacion: ")
            CantPag = input("\tCantidad de paginas:")

            try:
                cursor.execute('''INSERT INTO Libro(ISBN, Nombre, Autor, Publicacion, CantPag) 
                         VALUES(?,?,?,?,?)''', (ISBN, Nombre, Autor, Publicacion, CantPag))
                print("\n--------------------------------------\nEl libro ha sido agregado exitosamente."
                      "\n--------------------------------------\n")
                break

            except:
                print("En la BD ya se encuentra un libro con esta ISBN...")
                time.sleep(3)
            db.commit()
            os.system("pause")


    # Esta opcion es para eliminar un libro por medio del ISBN.
    elif Opcion == 3:
        while True:
            ISBN = input("Introduzca el ISBN del libro que quiere eliminar: ")
            try:
                cursor.execute('''DELETE FROM Libro WHERE ISBN = ?''', (ISBN,))
                print("\n--------------------------------------\nEl libro "+ ISBN +" ha sido eliminado"
                      "\n--------------------------------------\n")
                break
            except:
                print("No existe un libro con este ISBN en la BD.")

        """Se le pone coma despues de ISBN por que no puede elimaniar sola esa columna debe eliminar
        todo lo que esta en esa fila. La coma permite incluir todas las columnas restantes sin tener que nombrarlas."""

        db.commit()
        os.system("pause")


    elif Opcion == 4:
        break

    else:
        print("\n--------------------------------------\nOpcion invalida... Intente nuevamente."
              "\n--------------------------------------\n")
        time.sleep(3)

db.close()