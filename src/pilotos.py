from datetime import *
from typing import NamedTuple
import csv

Carrera = NamedTuple("Carrera", 
            [("nombre", str),
             ("escuderia", str),
             ("fecha_carrera", date) ,
             ("temperatura_min", int),
             ("vel_max", float),
             ("duracion",float),
             ("posicion_final", int),
             ("ciudad", str),
             ("top_6_vueltas", list[float]),
             ("tiempo_boxes",float),
             ("nivel_liquido", bool)
            ])

def lee_carreras(fichero):
    with open(fichero, "rt", encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=";")
        next(lector)
        pilotos = []
        for nombre, escuderia, fecha_carrera, temperatura_min, vel_max, duracion, posicion_final, ciudad, top_6_vueltas, tiempo_boxes, nivel_liquido in lector:
            nombre = str(nombre).strip()
            escuderia = str(escuderia).strip()
            fecha_carrera = parseaFecha(fecha_carrera)
            temperatura_min = int(temperatura_min)
            vel_max = float(vel_max)
            duracion = float(duracion)
            posicion_final = int(posicion_final)
            ciudad = str(ciudad)
            top_6_vueltas = parseaVueltas(top_6_vueltas)
            tiempo_boxes = float(tiempo_boxes)
            nivel_liquido = parseaBoolean(nivel_liquido)
            tupla = Carrera(nombre, escuderia, fecha_carrera, temperatura_min, vel_max, duracion, posicion_final, ciudad, top_6_vueltas, tiempo_boxes, nivel_liquido)
            pilotos.append(tupla)
        return pilotos

def parseaBoolean(b):
    if b == "1":
        return True
    elif b == "no":
        return False
    else:
        print("Algo está mal")

def parseaFecha(texto:str):
    fecha = datetime.strptime(texto, "%d-%m-%y").date()
    return fecha

def parseaVueltas(vueltas:str):
    vueltas_preparadas = vueltas.replace("[", "").replace("]", "").strip()
    vueltas_limpio = []
    for vuelta in vueltas_preparadas.split("/"):
        if vuelta.strip() == "-":
            vueltas_limpio.append(0.)
        else:
            vueltas_limpio.append(float(vuelta))
    return vueltas_limpio

def media_tiempo_boxes(carreras:list[Carrera], ciudad:str, fecha:date | None =None)->float:
    lista = []
    for carrera in carreras:
        if ciudad == carrera.ciudad and (fecha is None or fecha == carrera.fecha_carrera):
            lista.append(carrera.tiempo_boxes)
    if len(lista)>0:
        return sum(lista)/len(lista)
    else:
        return 0

def pilotos_menor_tiempo_medio_vueltas_top(carreras:list[Carrera], n)->list[tuple[str,date]]:
    lista = []
    res = []
    for carrera in carreras:
        if 0.0 not in carrera.top_6_vueltas:
            tupla = (carrera.nombre, carrera.fecha_carrera, sum(carrera.top_6_vueltas))
            lista.append(tupla)
    lista2 = sorted(lista, key=lambda n: n[2])
    for r in lista2:
        res.append((r[0], r[1]))
    return res[:n]

            
        
    







