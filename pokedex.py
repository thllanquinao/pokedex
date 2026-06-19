# Sistema Pokedex - FPY1101
# Estudiante: [Thomas Llanquinao]
import os
# Lista principal donde se guardan todos los Pokemon
pokedex = []

# Lista de los 18 tipos oficiales de Pokemon
tipos_validos = ["Acero", "Agua", "Bicho", "Dragon", "Electrico", "Fantasma", "Fuego","Hada", "Hielo", "Lucha", "Normal", "Planta", "Psiquico", "Roca","Siniestro", "Tierra", "Veneno", "Volador"]

regiones_validas = ["Kanto", "Jhoto", "Hoenn", "Sinnoh", "Teselia", "Kalos", "Alola", "Galar", "Paldea"]
def registrar_pokemon():
    """
    Registra un nuevo Pokemon en la Pokedex.
    """
    print("\n--- Registrar Nuevo Pokemon ---")
    
    # Nombre
    while True:
        
        nombre = input("Ingresa el nombre del Pokemon: ").strip().capitalize()
        if nombre == "":
            print("Error: El nombre no puede estar vacio.")
            continue
        if any(p["nombre"] == nombre for p in pokedex):  #Verifica si el nombre del pokemon ya existe en la pokedex para evitar duplicados
            print(f"Error: {nombre} ya esta registrado.")
        else:
            break

    # Tipo principal (obligatorio y valido)
    while True:
        tipo1 = input("Ingresa el tipo principal: ").strip().capitalize()
        if tipo1 in tipos_validos:
            tipos = [tipo1]
            break
        else:
            print("Error: Tipo no valido.")
            print("Tipos permitidos:", ", ".join(tipos_validos))

    # Tipo secundario (opcional)
    if input("¿Tiene un segundo tipo? (s/n): ").lower() == 's':
        while True: 
            tipo2 = input("Ingresa el segundo tipo: ").strip().capitalize()
            if tipo2 == "":
                break
            if tipo2 in tipos_validos:
                if tipo2 != tipo1:
                    tipos.append(tipo2)
                    break
                else:
                    print("Error: El segundo tipo no puede ser igual al primero.")
            else:
                print("Error: Tipo no valido.")
        while True:
            tipo2 = input("Ingresa el segundo tipo: ").strip().capitalize()
            if tipo2 == "":
                break
            if tipo2 in tipos_validos:
                if tipo2 != tipo1:
                    tipos.append(tipo2)
                    break
                else:
                    print("Error: El segundo tipo no puede ser igual al primero.")
            else:
                print("Error: Tipo no válido.")

    # Etapa de evolucion
    while True:
        try:
            etapa = int(input("Etapa de evolucion (1-3): "))
            if 1 <= etapa <= 3:
                break
            print("Error: La etapa debe estar entre 1 y 3.")
        except ValueError:
            print("Error: Debes ingresar un numero entero.")

    # Generacion
    while True:
        try:
            generacion = int(input("Generacion (1-9): "))
            if 1 <= generacion <= 9:
                break
            print("Error: La generacion debe estar entre 1 y 9.")
        except ValueError:
            print("Error: Debes ingresar un numero entero.")

    # Region
    while True:
        region = input("Region de origen: ").strip().capitalize()
        if region in regiones_validas:
            region = [region]
            break
        else:
            print("Error: Region no valida.")
            print("Tipos permitidos:", ", ".join(regiones_validas))
        if region != "":
            print("Error: La region no puede estar vacia.")

    # Guardar el Pokemon
    pokedex.append({
        "nombre": nombre,
        "tipos": tipos,
        "etapa": etapa,
        "generacion": generacion,
        "region": region
    })
    print(f"{nombre} registrado con exito!")

def mostrar_pokedex():
    """
    Muestra todos los Pokémon que hay en la Pokedex.
    """
    print("\n--- Lista de Pokemon ---")
    if not pokedex:
        print("La Pokedex esta vacia.")
        return

    for i in range(len(pokedex)):
        p = pokedex[i]
        print(f"{i+1}. {p['nombre']} | Tipos: ", end="")
        # Imprimir tipos
        for j in range(len(p['tipos'])):
            print(p['tipos'][j], end="")
            if j < len(p['tipos']) - 1:
                print(" / ", end="")
        print(f" | Etapa: {p['etapa']} | Gen: {p['generacion']} | Region: {p['region']}")

def actualizar_pokemon():
    """
    Actualiza los datos de un Pokemon.
    """
    print("\n--- Actualizar Pokemon ---")
    nombre_buscado = input("Nombre del Pokemon a actualizar: ").strip().capitalize()
    
    for i in range(len(pokedex)):
        if pokedex[i]["nombre"] == nombre_buscado:
            p = pokedex[i]
            print("Deja en blanco si no quieres cambiar el dato.")
            
            # Actualizar etapa
            nueva_etapa = input(f"Nueva etapa ({p['etapa']}): ").strip()
            if nueva_etapa:
                try:
                    etapa_int = int(nueva_etapa)
                    if 1 <= etapa_int <= 3:
                        p['etapa'] = etapa_int
                    else:
                        print("Etapa fuera de rango. No se cambió.")
                except ValueError:
                    print("Error: Solo se permiten numeros.")

            # Actualizar generacion
            nueva_gen = input(f"Nueva generacion ({p['generacion']}): ").strip()
            if nueva_gen:
                try:
                    gen_int = int(nueva_gen)
                    if 1 <= gen_int <= 9:
                        p['generacion'] = gen_int
                    else:
                        print("Generacion fuera de rango. No se cambio.")
                except ValueError:
                    print("Error: Solo se permiten numeros.")
            
            # Actualizar region
            nueva_region = input(f"Nueva region ({p['region']}): ").strip().capitalize()
            if nueva_region:
                p['region'] = nueva_region
                
            print("Datos actualizados correctamente")
            return
            
    print("Pokemon no encontrado.")

def eliminar_pokemon():
    """
    Elimina un Pokemon de la Pokedex.
    """
    print("\n--- Eliminar Pokemon ---")
    nombre = input("Nombre del Pokemon a eliminar: ").strip().capitalize()
    
    for i in range(len(pokedex)):
        if pokedex[i]["nombre"] == nombre:
            confirmacion = input(f"¿Estas seguro de eliminar a {nombre}? (s/n): ").strip().lower()
            if confirmacion == 's':
                del pokedex[i]      
                print(f"{nombre} eliminado correctamente")
            else:
                print("Operacion cancelada.")
            return
            
    print("Pokemon no encontrado.")

def menu():
    """
    Muestra el menu principal y permite elegir las opciones.
    """
    while True:
        print("\n--- MENU POKEDEX ---")
        print("1. Registrar")
        print("2. Ver Pokedex")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Salir")
        opcion = input("Selecciona una opcion: ").strip()
        
        if opcion == '1':
            registrar_pokemon()
        elif opcion == '2':
            mostrar_pokedex()
        elif opcion == '3':
            actualizar_pokemon()
        elif opcion == '4':
            eliminar_pokemon()
        elif opcion == '5':
            print("Apagando Pokedex...")
            break
        else:
            print("Opcion invalida. Por favor elige del 1 al 5.")

if __name__ == "__main__":
    menu()