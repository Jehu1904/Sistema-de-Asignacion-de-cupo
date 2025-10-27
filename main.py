from Proceso.Asignacion_cupo import AsignacionCupos 
from politicas.Politicas_asignacion import PoliticaMeritoAcademico 
from utils.generador_datos import (
    obtener_postulantes_desde_fichero, 
    obtener_carreras, 
    guardar_resultados_en_fichero
)
#main
if __name__ == '__main__':
    
    print("--- INICIANDO PROCESO SAC ---")

    postulantes = obtener_postulantes_desde_fichero()
    carreras = obtener_carreras() 

    if not postulantes or not carreras:
        print("Fallo al cargar datos. Terminando.")
        exit()

    print(f"Datos cargados: {len(postulantes)} postulantes y {len(carreras)} carreras.")

    politica = PoliticaMeritoAcademico()
    asignacion = AsignacionCupos(politica)

    print("Ejecutando asignación por Mérito Académico...")
    resultados = asignacion.ejecutar(postulantes, carreras)

    for nombre_carrera, seleccionados in resultados.items():
        print(f"\nCarrera: {nombre_carrera} ({len(seleccionados)} asignados)")
        if seleccionados:
            for p in seleccionados:
                print(f"   -> {p}") 
        else:
            print("   -> No hay postulantes asignados.")
            
    guardar_resultados_en_fichero(resultados)
    
    print("\n--- PROCESO FINALIZADO ---")