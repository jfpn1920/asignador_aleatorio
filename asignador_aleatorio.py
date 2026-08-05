import random
ids = []
nombres = []
categorias = []
responsables = []
prioridades = []
estados = []
fechas = []
descripciones = []
observaciones = []
#----------------------------------------#
#--|menu_principal_asignador_aleatorio|--#
#----------------------------------------#
while True:
    print("menu principal asignador aleatorio")
    print("1) registrar elemento")
    print("2) editar elemento")
    print("3) eliminar elemento")
    print("4) buscar elemento")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #------------------------#
    #--|registrar_elemento|--#
    #------------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_elemento = 1
        else:
            id_elemento = ids[-1] + 1
        nombre = input("nombre: ")
        categoria = input("categoría: ")
        responsable = input("responsable: ")
        prioridad = input("prioridad (alta, media, baja): ")
        estado = input("estado (disponible o asignado): ")
        fecha = input("fecha de registro: ")
        descripcion = input("descripción: ")
        observacion = input("observación: ")
        ids.append(id_elemento)
        nombres.append(nombre)
        categorias.append(categoria)
        responsables.append(responsable)
        prioridades.append(prioridad)
        estados.append(estado)
        fechas.append(fecha)
        descripciones.append(descripcion)
        observaciones.append(observacion)
        print("elemento registrado correctamente.")
        print("id:", id_elemento)
    #---------------------#
    #--|editar_elemento|--#
    #---------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen elementos registrados.")
        else:
            print("editar elemento")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]} | {estados[i]}")
            id_buscar = int(input("ingrese la id del elemento: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {nombres[posicion]} | {categorias[posicion]}")
                nombres[posicion] = input("nuevo nombre: ")
                categorias[posicion] = input("nueva categoría: ")
                responsables[posicion] = input("nuevo responsable: ")
                prioridades[posicion] = input("nueva prioridad: ")
                estados[posicion] = input("nuevo estado: ")
                fechas[posicion] = input("nueva fecha: ")
                descripciones[posicion] = input("nueva descripción: ")
                observaciones[posicion] = input("nueva observación: ")
                print("elemento actualizado correctamente.")
            else:
                print("id no encontrada.")
    #-----------------------#
    #--|eliminar_elemento|--#
    #-----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen elementos registrados.")
        else:
            print("eliminar elemento")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]}")
            id_buscar = int(input("ingrese la id del elemento: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del elemento")
                print(f"{ids[posicion]} | {nombres[posicion]} | {categorias[posicion]}")
                respuesta = input("¿desea eliminar este elemento? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    categorias.pop(posicion)
                    responsables.pop(posicion)
                    prioridades.pop(posicion)
                    estados.pop(posicion)
                    fechas.pop(posicion)
                    descripciones.pop(posicion)
                    observaciones.pop(posicion)
                    print("elemento eliminado correctamente.")
                else:
                    print("el elemento no fue eliminado.")
            else:
                print("id no encontrada.")
    #---------------------#
    #--|buscar_elemento|--#
    #---------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen elementos registrados.")
        else:
            print("buscar elemento")
            id_buscar = int(input("ingrese la id del elemento: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("categoría:", categorias[posicion])
                print("responsable:", responsables[posicion])
                print("prioridad:", prioridades[posicion])
                print("estado:", estados[posicion])
                print("fecha:", fechas[posicion])
                print("descripción:", descripciones[posicion])
                print("observación:", observaciones[posicion])
            else:
                print("id no encontrada.")
    #--------------------#
    #--|lista_de_datos|--#
    #--------------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen elementos registrados.")
        else:
            disponibles = 0
            asignados = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]} | {estados[i]}")
                if estados[i].lower() == "disponible":
                    disponibles += 1
                elif estados[i].lower() == "asignado":
                    asignados += 1
            print("estadísticas asignador aleatorio")
            print("cantidad de elementos:", len(ids))
            print("disponibles:", disponibles)
            print("asignados:", asignados)
            posicion = random.randint(0, len(ids) - 1)
            estados[posicion] = "Asignado"
            print("elemento asignado aleatoriamente")
            print("id:", ids[posicion])
            print("nombre:", nombres[posicion])
            print("categoría:", categorias[posicion])
            print("responsable:", responsables[posicion])
            print("prioridad:", prioridades[posicion])
            print("estado:", estados[posicion])
            print("fecha:", fechas[posicion])
            print("descripción:", descripciones[posicion])
            print("observación:", observaciones[posicion])
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el asignador aleatorio.")
        break
    else:
        print("opción no válida.")