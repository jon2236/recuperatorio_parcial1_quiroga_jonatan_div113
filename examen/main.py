from funciones import *

def main():
    lista_posts = []
    while True:
        opcion = menu()
        if opcion == '1':
            nombre_archivo = input("ingrese el nombre del archivo CSV con su extension .csv alfinal del nombre: ")
            cargar_archivo_csv(nombre_archivo, lista_posts)
        elif opcion == '2':
            imprimir_lista(lista_posts)
        elif opcion == '3':
            asignar_estadisticas(lista_posts)
            print("estadisticas asignadas")
        elif opcion == '4':
            nombre_archivo = input("ingrese el nombre del archivo para guardar los mejores posts: ")
            filtrar_mejores_posts(lista_posts, nombre_archivo)
            print("aarchivo de mejores posts generado con exito.")
        elif opcion == '5':
            nombre_archivo = input("ingrese el nombre del archivo para guardar los posts de haters: ")
            filtrar_haters(lista_posts, nombre_archivo)
            print("archivo de haters generado con exito.")
        elif opcion == '6':
            promedio = calcular_promedio_followers(lista_posts)
            print(f"el promedio de followers es: {promedio:.2f}")
        elif opcion == '7':
            lista_ordenada = ordenar_por_user(lista_posts)
            nombre_archivo = input("ingrese el nombre del archivo JSON para guardar la lista ordenada: ")
            guardar_en_json(lista_ordenada, nombre_archivo)
            print("lista ordenada y guardada en el archivo JSON con exito.")
        elif opcion == '8':
            populares, max_likes = mostrar_mas_popular(lista_posts)
            if populares:
                print(f"el/los user(s) con el posteo mas likeado ({max_likes} likes):")
                for post in populares:
                    print(post['user'])
            else:
                print("no hay posts disponibles.")
        elif opcion == '9':
            print("nos vimos")
            break
        else:
            print("Opción no valida.")
        pausar()

if __name__ == "__main__":
    main()
