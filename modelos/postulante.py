class Postulante:
    def __init__(self, cedula: str, nombre: str, puntaje: float, carrera_postulada: str):
        self._cedula = cedula
        self._nombre = nombre
        self._puntaje = puntaje
        self._carrera = carrera_postulada
        self._asignado = False
        self._resultado = None

    @property
    def cedula(self):
        return self._cedula

    @property
    def nombre(self):
        return self._nombre

    @property
    def puntaje(self):
        return self._puntaje

    @property
    def carrera(self):
        return self._carrera
    
    @property
    def asignado(self):
        return self._asignado

    def marcar_como_asignado(self, carrera_asignada: str):
        self._asignado = True
        self._resultado = carrera_asignada

    def __str__(self):
        estado = "Asignado" if self._asignado else "Pendiente"
        carrera_res = self._resultado if self._resultado else self._carrera
        return f"P. {self._nombre} | Cédula: {self._cedula} | Puntaje: {self._puntaje} | Postuló a: {self._carrera} | Estado: {estado}"