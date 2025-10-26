from asignacion_cupos import AsignacionCupos
from politicas_asignacion import PoliticaMeritoAcademico
from registro_postulantes import obtener_postulantes
from gestion_carreras import obtener_carreras


politica = PoliticaMeritoAcademico()


asignacion = AsignacionCupos(politica)

# Obtiene datos desde otros módulos del sistema
postulantes = obtener_postulantes()  # del módulo de registro (SIPU)
carreras = obtener_carreras()        # del módulo de gestión (SAC)

# Ejecutar el proceso de asignación
resultados = asignacion.ejecutar(postulantes, carreras)

# Mostrar los resultados
for nombre_carrera, seleccionados in resultados.items():
    print(f"\nCarrera: {nombre_carrera}")
    if seleccionados:
        for p in seleccionados:
            print(f" - {p.nombre} ({p.puntaje})")
    else:
        print("No hay postulantes asignados.")
