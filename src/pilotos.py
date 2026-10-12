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

def ratio_tiempo_boxes_total(carreras:list[Carrera])->list[tuple[str,date, float]]:
    tiempos_por_dias = {}
    lista = []
    for carrera in carreras:
        if carrera.fecha_carrera not in tiempos_por_dias:
            tiempos_por_dias[carrera.fecha_carrera] = 0
        tiempos_por_dias[carrera.fecha_carrera] += carrera.tiempo_boxes
    for carrera in carreras:
        tupla = (carrera.nombre, str(carrera.fecha_carrera), round(carrera.tiempo_boxes/tiempos_por_dias[carrera.fecha_carrera], 3))
        lista.append(tupla)
    res = sorted(lista, key=lambda x:x[2])
    return res

def puntos_piloto_anyos(carreras:list[Carrera])->dict[str, list[int]]:
    res = {}
    res2 = {}
    for carrera in carreras:
        tupla = (carrera.nombre, carrera.fecha_carrera.year)
        if tupla not in res:
            res[tupla] = 0
        res[tupla] += calcular_puntos(carrera)
    for (nombre, anyo), suma in res.items():
        if nombre not in res2:
            res2[nombre] = []
        res2[nombre].append(suma)
    return res2


def calcular_puntos(carrera:Carrera):
    if carrera.posicion_final == 1:
        return 50
    elif carrera.posicion_final == 2:
        return 25
    elif carrera.posicion_final == 3:
        return 10
    else:
        return 0


def mejor_escuderia_anyo(carreras:list[Carrera], anyo:int)->str:
    res = {}                                                    
    res2 = {}                                                   
    for carrera in carreras:                                    
        if carrera.fecha_carrera.year==anyo:
            if carrera.escuderia not in res:
                res[carrera.escuderia] = 0
            res[carrera.escuderia] += calcular_victoria(carrera)
    mejor_escuderia = max(res.items(), key=lambda n:n[1])
    print(res)
    return mejor_escuderia[0]
        
def calcular_victoria(carrera:Carrera):
    if carrera.posicion_final == 1:
        return 1
    else:
        return 0






