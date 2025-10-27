class PoliticaMeritoAcademico:
    def asignar(self, postulantes, carrera):
        ordenados = sorted(postulantes, key=lambda p: p.puntaje, reverse=True)
        seleccionados = ordenados[:carrera.cupos_disponibles]
        return seleccionados


