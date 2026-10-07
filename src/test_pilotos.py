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



if __name__ == "__main__":
    fichero = lee_carreras('data/f1.csv')
    test_lee_carreras(fichero)
    test_media_tiempo_boxes(fichero, "Barcelona", date(2023,5,7))
    test_pilotos_menor_tiempo_medio_vueltas_top(fichero, 4)
    

