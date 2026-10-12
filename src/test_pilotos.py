from pilotos import *

def test_lee_carreras(fichero):
    print("1. Test de lee_carreras:")
    print("Total registros leídos: ", len(fichero), ". Mostrando los dos primeros registros: ")
    print(fichero[:2])

def test_media_tiempo_boxes(carreras:list[Carrera], ciudad:str, fecha:date | None =None):
    print("\n 2. Test de media_tiempo_boxes:")
    if not fecha:
        print(f"La media de tiempo en boxes en la ciudad de {ciudad} es de", media_tiempo_boxes(carreras, ciudad, fecha), "segundos")
    else:
        print(f"La media de tiempo en boxes en la ciudad de {ciudad} en  el {fecha} es de", media_tiempo_boxes(carreras, ciudad, fecha), "segundos")

def test_pilotos_menor_tiempo_medio_vueltas_top(carreras:list[Carrera], n)->list[tuple[str,date]]:
    print("\n 3. Test pilotos_menor_tiempo_medio_vueltas_top.")
    print(f"Los {n} pilotos con menor tiempo medio son: ", pilotos_menor_tiempo_medio_vueltas_top(carreras, n))

def test_ratio_tiempo_boxes_total(carreras:list[Carrera])->list[tuple[str,date, float]]:
    print("\n 4. Test ratio_tiempo_boxes_total.")
    print("Los ratios del tiempo en boxes son: ", ratio_tiempo_boxes_total(carreras))

def test_puntos_piloto_anyos(carreras:list[Carrera])->dict[str, list[int]]:
    print("\n 5. Test puntos_piloto_anyos.")
    print(puntos_piloto_anyos(carreras))

def test_mejor_escuderia_anyo(carreras:list[Carrera], anyo:int)->str:
    print("\n 6. Test mejor_escuderia_anyo.")
    print(f"La mejor escudería en el año {anyo} ha sido", mejor_escuderia_anyo(carreras, anyo))

if __name__ == "__main__":
    fichero = lee_carreras('data/f1.csv')
    test_lee_carreras(fichero)
    test_media_tiempo_boxes(fichero, "Barcelona", date(2023,5,7))
    test_pilotos_menor_tiempo_medio_vueltas_top(fichero, 4)
    test_ratio_tiempo_boxes_total(fichero)
    test_puntos_piloto_anyos(fichero)
    test_mejor_escuderia_anyo(fichero, date(2022, 1, 1).year)
    

