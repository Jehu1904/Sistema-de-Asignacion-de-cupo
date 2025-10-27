import csv
import os
from typing import List, Dict
from modelos.postulante import Postulante
from modelos.carrera import Carrera

# Define la ruta base para que los ficheros se encuentren correctamente
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 

# ----------------------------------------------------------------------
# FUNCIÓN DE LECTURA (Entrada de Datos al SAC)
# ----------------------------------------------------------------------

def obtener_postulantes_desde_fichero(nombre_fichero: str = 'datos_postulantes.csv') -> List[Postulante]:
    """Lee datos del fichero CSV y crea objetos Postulante."""
    
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
    """Simula obtener la data de carreras con sus cupos (podría venir de otro fichero)."""
    # Usamos datos codificados por simplicidad, pero el principio es el mismo
    return [
        Carrera("Ingeniería de Software", cupos_disponibles=2),
        Carrera("Ingeniería Civil", cupos_disponibles=1),
        Carrera("Medicina", cupos_disponibles=1)
    ]

# ----------------------------------------------------------------------
# FUNCIÓN DE ESCRITURA (Persistencia de Resultados)
# ----------------------------------------------------------------------

def guardar_resultados_en_fichero(resultados_asignacion: Dict[str, List[Postulante]], nombre_fichero: str = 'resultados_sac.csv'):
    """Guarda el resultado del SAC en un nuevo fichero CSV."""
    
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
            # DictWriter sabe cómo escribir diccionarios en filas CSV
            writer = csv.DictWriter(file, fieldnames=campos)
            
            writer.writeheader() 
            writer.writerows(datos_salida)
            
        print(f"\n✅ Resultados guardados en: {nombre_fichero}")
        
    except Exception as e:
        print(f"Error al escribir el fichero de resultados: {e}")

#hola