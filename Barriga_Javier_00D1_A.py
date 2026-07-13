from os import system
system("cls")


#juegos = {
#    "G001": ["eclipse", "pc", "accion", "T", True, "novastudio"]
#}

#inventario = {
#    "G001": [9990, 7]
#}
juegos = {}
inventario = {} 

def mostrar_menu():
    menu = """
    ========== MENÚ PRINCIPAL =========
    1. Stock por plataforma
    2. Busqueda de juegos por rango de precio
    3. Actualizazr precio de juego
    4. Agregar juego
    5. Eliminar juego
    6. salir
    """
    return menu

def leer_opcion():
    opcion_valida = False
    while opcion_valida == False:
        try:
            opcion = int(input("Seleccione una opción:"))
            if opcion >=1 and opcion <= 6:
                opcion_valida = True
            else:
                print ("Debe seleccionar una opción valida...")
        except ValueError:
            print("Debe ingresar un numero entero positivo... ")
        return opcion

def stock_plataforma(plataforma, juegos, inventario):
    stock_total = 0
    for codigo_guardado in juegos:
        plataforma_guardada = juegos[codigo_guardado][1]
        if plataforma_guardada.lower() == plataforma.strip().lower():
            stock_juego = inventario[codigo_guardado][1]
            stock_total = stock_total + stock_juego
        print("Stock total: ", stock_total)
            
def busqueda_precio(p_min, p_max, juegos, inventario, titulo_guardado):
    juegos_encontrados = []
    for codigo_guardado in inventario:
        precio_guardado = inventario[codigo_guardado][0]
        stock_guardado = inventario[codigo_guardado][1]
        
        if precio_guardado >= p_min and precio_guardado <= p_max and stock_guardado!= 0:
            titulo_guardado = juegos[codigo_guardado][0]
        juegos_encontrados.append(titulo_guardado + "-" + codigo_guardado)
        juegos_encontrados.sort()
        if len(juegos_encontrados) == 0:
            print("No hay juegos en este rango de precios.")
        else:
            for juegos_encontrados in juegos_encontrados:
                print("Juego_encontrado")

def buscar_codigo(codigo, diccionario):
    for codigo_guardado in diccionario:
        if codigo_guardado.lower() == codigo.strip().lower():
            return True
    return False

def actualizar_precio(codigo, nuevo_precio, inventario):
    codigo_existe = buscar_codigo(codigo, inventario)
    if codigo_existe == True:
        for codigo_guardado in inventario:
            if codigo_guardado.lower == codigo.strip().lower():
                inventario [codigo_guardado][0] = nuevo_precio
                return True
        return False
    
def validar_codigo(codigo, juegos, inventario):
    if codigo.strip() == "":
        return False
    
    if buscar_codigo(codigo, juegos) == True:
        return False
    
    return True

def validar_titulo(titulo):
    if titulo.strip() == "":
        return False
    else:
        return True
    
def validar_plataforma(plataforma):
    if plataforma.strip() == "":
        return False
    else:
        return True

def validar_genero(genero):
    if genero.strip() == "":
        return False
    else: 
        return True

def validar_calsificacion(clasificacion):
    if clasificacion == "E" or clasificacion == "T" or clasificacion == "M":
        return True
    else:
        return False

def validar_multiplayer(multiplayer):
    if multiplayer.lower() == "s" or multiplayer.lower() == "n":
        return True
    else:
        return False

def validar_editor(editor):
    if editor.strip() == "":
        return False
    else:
        return True

def validar_precio():
    pass
def validar_stock():
    pass

def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, juegos, inventario):
    if buscar_codigo(codigo, juegos) == True or buscar_codigo(codigo, inventario) == True:
        return False
    codigo_guardado = codigo.strip().upper()
    juegos[codigo_guardado] = [
        titulo.strip(),
        plataforma.strip(),
        genero.strip(),
        clasificacion,
        multiplayer,
        editor.strip()
    ]
    inventario[codigo_guardado] = [precio, stock]
    return True

def eliminar_juego(codigo, juegos, inventario):
    codigo_existe = buscar_codigo(codigo,inventario)
    
    if codigo_existe == False:
        return False
    
    codigo_encontrado = ""
    for codigo_guardado in inventario:
        if codigo_guardado.lower() == codigo.strip().lower():
            codigo_encontrado = codigo_guardado
        if codigo_encontrado != "":
            del inventario[codigo_encontrado]
            del juegos[codigo_encontrado]
            return True
        else:
            return False
def main():
    while True:
            print(mostrar_menu())
            opcion = leer_opcion()
            
            if opcion == 1:
                plataforma = input("Ingrese la plataforma: ")
                stock_plataforma(plataforma, juegos, inventario)
            
            elif opcion == 2:
                rango_valido = False
                while rango_valido == False:
                    p_min = int(input("Ingrese el precio minimo: "))
                    p_max = int(input("Ingrese el precio maximo: "))
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        rango_valido = True 
                    else:
                        print("Debe ingresar un rango valido")
                    busqueda_precio(p_min, p_max, juegos, inventario)
            
            elif opcion == 3:
                respuesta = "s"
                while respuesta == "s":
                    codigo = input("Ingrese el codigo del juego: ")
                    precio_valido = False
                    if precio_valido == False:
                        try:
                            nuevo_precio = int(input("Ingrese el nuevo precio: "))
                            if nuevo_precio > 0:
                                precio_valido = True
                            else:
                                print("Debe ingresar un precio valido: ")
                        except ValueError:
                            print("Debe ingresar solo valores numericos: ")
                        
            elif opcion == 4:
                codigo = input("Ingrese el codigo: ")
                titulo = input("Ingrese el titulo: ")
                plataforma = input("Ingrese la plataforma: ")
                genero = input("Ingrese el genero: ")
                clasificacion = input("Ingrese la clasificacion: ")
                multiplayer_ingresado = input("Es multiplayer s/n?: ")
                editor = input("Ingrese el editor: ")
                precio = int(input("Ingrese el precio: "))
                stock = int(input("Ingrese el stock: "))
                codigo_valido = validar_codigo(codigo, juegos, inventario)
                titulo_valido = validar_titulo(titulo)
                plataforma_valida = validar_plataforma(plataforma)
                genero_valido = validar_genero(genero)
                clasificaion_valida = validar_calsificacion(clasificacion)
                multiplayer_valido = validar_multiplayer(multiplayer_ingresado)
                #editor_valido = validar_editor(editor)
                #precio_valido = validar_precio(precio)
                #stock_valido = validar_stock(stock)
            
            elif opcion == 5:
                codigo = input("Ingrese el codigo del juego a eliminar: ")
                juego_eliminado = eliminar_juego(codigo, juegos, inventario)
                if juego_eliminado == True:
                    print("juego eliminado")
                else:
                    print("El codigo no existe")
                
            elif opcion == 6:
                print("Programa finalizado...")
                break
            input("Presione enter para continuar")

main()