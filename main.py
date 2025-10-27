from Proceso.Asignacion_cupo import AsignacionCupos 
from politicas.Politicas_asignacion import PoliticaMeritoAcademico 

# ¡Importación de las funciones de I/O del fichero!
from utils.generador_datos import (
    obtener_postulantes_desde_fichero, 
    obtener_carreras, 
    guardar_resultados_en_fichero
)

# ...

if __name__ == '__main__':
    
    # 1. El SAC PIDE los datos (Lectura del fichero)
    postulantes = obtener_postulantes_desde_fichero()
    carreras = obtener_carreras() 

    if not postulantes or not carreras:
        print("Fallo al cargar datos. Terminando el programa.")
        exit()

    # 2. Configuración y ejecución del SAC
    politica = PoliticaMeritoAcademico()
    asignacion = AsignacionCupos(politica)
    resultados = asignacion.ejecutar(postulantes, carreras)

    # 3. Guardar Resultados (Escritura en el fichero)
    guardar_resultados_en_fichero(resultados)

    # 4. Mostrar Resultados en pantalla (tu código original)
    # ...