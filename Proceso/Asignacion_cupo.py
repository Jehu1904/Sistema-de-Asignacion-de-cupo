from politicas.politica_asignacion import PoliticaAsignacion
from typing import List, Dict
from modelos.postulante import Postulante
from modelos.carrera import Carrera


class AsignacionCupos:
    def __init__(self, politica):
        self.politica = politica

    def ejecutar(self, postulantes, carreras):
        resultados = {}

        for carrera in carreras:
            postulantes_carrera = [p for p in postulantes if p.carrera == carrera.nombre]
            seleccionados = self.politica.asignar(postulantes_carrera, carrera)
            resultados[carrera.nombre] = seleccionados

        return resultados

#eso
'''
class AsignacionCupos:
    """
    Motor del SAC que ejecuta la asignación.
    Utiliza Inyección de Dependencias para aplicar la política.
    """
    
    def __init__(self, politica: PoliticaAsignacion):
        # Inyección de Dependencias (Constructor Injection): 
        # El motor NO crea la política; la recibe desde fuera.
        self.politica = politica 

    def ejecutar(self, postulantes: List[Postulante], carreras: List[Carrera]) -> Dict[str, List[Postulante]]:
        resultados = {}
        
        for carrera in carreras:
            # 1. Filtrar postulantes por carrera
            postulantes_carrera = [p for p in postulantes if p.carrera == carrera.nombre]
            
            # 2. Delegar la asignación a la política inyectada (Polimorfismo en acción)
            seleccionados = self.politica.asignar(postulantes_carrera, carrera)
            
            # 3. Almacenar resultados
            resultados[carrera.nombre] = seleccionados
            
        return resultados'''