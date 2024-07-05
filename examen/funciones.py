import random
import os
import json

def limpiar_pantalla():
    os.system("cls")

def pausar():
    os.system("pause")

def cargar_archivo_csv(nombre_archivo_data, lista):
    """cargo un archivo CSV"""
    try:
        with open(nombre_archivo_data, "r", encoding="utf-8") as archivo:
            encabezado = archivo.readline().strip("\n").split(",")
            for linea in archivo.readlines():
                post = {}
                linea = linea.strip("\n").split(",")
                id_post, user, likes, dislikes, followers = linea
                post["id"] = int(id_post)
                post["user"] = user
                post["likes"] = int(likes)
                post["dislikes"] = int(dislikes)
                post["followers"] = int(followers)
                lista.append(post)
        print("archivo cargado")
    except FileNotFoundError:
        print("no existe el archivo con ese nombre. veerifica el nombre por fa")



def menu():
    """muestra el menu de opciones y retorna la opcio"""
    limpiar_pantalla()
    print("//////// mi aburrida vida en las redes ////////")
    print("1-cargar archivo CSV")
    print("2-Imprimir lista")
    print("3-asignar estadisticas")
    print("4-filtrar por mejores posts")
    print("5-filtrar por haters")
    print("6-informar promedio de followers")
    print("7-ordenar los datos por nombre de user ascendente")
    print("8-mostrar mad popular")
    print("9-salir")
    return input("ingrese opcion: ")

def imprimir_lista(lista):
    """imprime la lista de posts"""
    if isinstance(lista, list):
        print("ID  USER    LIKES  DISLIKES  FOLLOWERS")
        print("--------------------------------------")
        for post in lista:
            print(f"{post['id']:2d}  {post['user']:7}  {post['likes']:5d}  {post['dislikes']:8d}  {post['followers']:9d}")
    else:
        raise ValueError("Eso no es una lista")

def asignar_estadisticas(lista):
    """asigna estadisticas aleatorias a cadeaa post"""
    for post in lista:
        post["likes"] = random.randint(500, 3000)
        post["dislikes"] = random.randint(300, 3500)
        post["followers"] = random.randint(10000, 20000)

def filtrar_mejores_posts(lista, nombre_archivo):
    """Filtra los posts con más de 2000 likes y los guarda en un archivo CSV"""
    mejores_posts = []
    for post in lista:
        if post["likes"] > 2000:
            mejores_posts.append(post)
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("id,user,likes,dislikes,followers\n")
        for post in mejores_posts:
            archivo.write(f"{post['id']},{post['user']},{post['likes']},{post['dislikes']},{post['followers']}\n")

def filtrar_haters(lista, nombre_archivo):
    """Filtro los posts donde los dislikes son mayores que los likes y los guardo en un archivo CSV"""
    haters_posts = []
    for post in lista:
        if post["dislikes"] > post["likes"]:
            haters_posts.append(post)
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("id,user,likes,dislikes,followers\n")
        for post in haters_posts:
            archivo.write(f"{post['id']},{post['user']},{post['likes']},{post['dislikes']},{post['followers']}\n")

def calcular_promedio_followers(lista):
    """Calcula y devuelve el promedio de followers de una lista de posts."""
    total_followers = 0
    if len(lista) > 0:
        for post in lista:
            total_followers += post["followers"]
        promedio = total_followers / len(lista)
    else:
        promedio = 0
    
    return promedio

def ordenar_por_user(lista):
    """ordeno la lista de posts por el nombre del usuario ascendentemente"""
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j]["user"] > lista[j+1]["user"]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def guardar_en_json(lista, nombre_archivo):
    """guardo la lista de posts en un archivo JSON"""
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, ensure_ascii=False, indent=4)

def mostrar_mas_popular(lista):
    """informoo el nombre del usuario con el post mas likeado"""
    if not lista:
        return [], 0
    max_likes = -1
    for post in lista:
        if post["likes"] > max_likes:
            max_likes = post["likes"]
    populares = []
    for post in lista:
        if post["likes"] == max_likes:
            populares.append(post)
    return populares, max_likes


