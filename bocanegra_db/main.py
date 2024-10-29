from database.aula import Aula

def mostrar_menu():
    print("\n--- Menú de Aulas ---")
    print("1. Agregar Aula")
    print("2. Mostrar Aulas")
    print("3. Consultar Aula por ID")
    print("4. Actualizar Aula")
    print("5. Eliminar Aula")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ")

        if opcion == '1':
            numero = input("Número de aula: ")
            planta = input("Planta (default: 1): ") or '1'
            situacion = input("Situación (default: DISPONIBLE): ") or 'DISPONIBLE'
            nueva_aula = Aula(numero, planta, situacion)
            nueva_aula.insertar_aula()
            print("Aula agregada exitosamente.")

        elif opcion == '2':
            aulas = Aula.consultar_aulas()
            print("Todas las aulas:", aulas)

        elif opcion == '3':
            aula_id = input("Ingrese el ID del aula a consultar: ")
            aula = Aula.consultar_aula(aula_id)
            if aula:
                print(f"Aula con ID {aula_id}:", aula)
            else:
                print(f"No se encontró el aula con ID {aula_id}.")

        elif opcion == '4':
            aula_id = input("Ingrese el ID del aula a actualizar: ")
            aula_existente = Aula.consultar_aula(aula_id)
            if aula_existente:
                numero = input("Nuevo número de aula: ")
                planta = input("Nueva planta: ")
                situacion = input("Nueva situación: ")
                Aula.actualizar_aula(aula_id, numero, planta, situacion)
                print(f"Aula con ID {aula_id} actualizada.")
            else:
                print(f"No se puede actualizar. El aula con ID {aula_id} no existe.")

        elif opcion == '5':
            aula_id = input("Ingrese el ID del aula a eliminar: ")
            aula_existente = Aula.consultar_aula(aula_id)
            if aula_existente:
                Aula.eliminar_aula(aula_id)
                print(f"Aula con ID {aula_id} eliminada.")
            else:
                print(f"No se puede eliminar. El aula con ID {aula_id} no existe.")

        elif opcion == '6':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor elige una opción entre 1 y 6.")

if __name__ == "__main__":
    main()
