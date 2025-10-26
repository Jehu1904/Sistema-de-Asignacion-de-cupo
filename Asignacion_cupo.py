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
