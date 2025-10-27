import csv
import os
from typing import List, Dict
from modelos.postulante import Postulante
from modelos.carrera import Carrera

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 


def obtener_postulantes_desde_fichero(nombre_fichero: str = 'datos_postulantes.csv') -> List[Postulante]:
    
    postulantes = []
    ruta_fichero = os.path.join(BASE_DIR, nombre_fichero)
    
    try:
        with open(ruta_fichero, mode='r', encoding='utf-8') as file:
            # DictReader permite leer cada fila como un diccionario (clave: encabezado)
            reader = csv.DictReader(file) 
            for fila in reader:
                # Creación del objeto Postulante, convirtiendo el puntaje a float
                p = Postulante(
                    cedula=fila['cedula'],
                    nombre=fila['nombre'],
                    puntaje=float(fila['puntaje']),
                    carrera_postulada=fila['carrera']
                )
                postulantes.append(p)
    except FileNotFoundError:
        print(f"Error: El fichero de datos de entrada '{ruta_fichero}' no fue encontrado.")
        return []
        
    return postulantes

def obtener_carreras() -> List[Carrera]:
    # Usamos datos codificados por simplicidad, pero el principio es el mismo
    return [
        Carrera("Ingeniería de Software", cupos_disponibles=2),
        Carrera("Ingeniería Civil", cupos_disponibles=1),
        Carrera("Medicina", cupos_disponibles=1)
    ]


def guardar_resultados_en_fichero(resultados_asignacion: Dict[str, List[Postulante]], nombre_fichero: str = 'resultados_sac.csv'):
    
    ruta_fichero = os.path.join(BASE_DIR, nombre_fichero)
    campos = ['cedula', 'nombre', 'puntaje', 'carrera_postulada', 'carrera_asignada', 'estado']
    datos_salida = []
    
    # Recorrer los resultados para estructurar los datos a guardar
    for carrera_asignada, postulantes_seleccionados in resultados_asignacion.items():
        for p in postulantes_seleccionados:
            datos_salida.append({
                'cedula': p.cedula,
                'nombre': p.nombre,
                'puntaje': p.puntaje,
                'carrera_postulada': p.carrera,
                'carrera_asignada': carrera_asignada,
                'estado': 'ASIGNADO'
            })

    try:
        with open(ruta_fichero, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=campos)
            
            writer.writeheader() 
            writer.writerows(datos_salida)
            
        print(f"\n Resultados guardados en: {nombre_fichero}")
        
    except Exception as e:
        print(f"Error al escribir el fichero de resultados: {e}")

#holaaa