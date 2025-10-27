class Carrera:
    def __init__(self, nombre: str, cupos_disponibles: int, puntaje_referencial: float = 0.0):
        self._nombre = nombre
        self._cupos_ofertados = cupos_disponibles
        self._puntaje_referencial = puntaje_referencial
        self._cupos_asignados = 0

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def cupos_ofertados(self) -> int:
        return self._cupos_ofertados

    @property
    def puntaje_referencial(self) -> float:
        return self._puntaje_referencial

    @property
    def cupos_asignados(self) -> int:

        return self._cupos_asignados

    def asignar_cupo(self) -> bool:

        if self._cupos_asignados < self._cupos_ofertados:
            self._cupos_asignados += 1
            return True
        return False
    
    def cupos_restantes(self) -> int:
        return self._cupos_ofertados - self._cupos_asignados
    
    def esta_llena(self) -> bool:
        return self._cupos_asignados == self._cupos_ofertados

    def obtener_puntaje_corte(self, postulantes_asignados: List[Postulante]) -> float:
        if not postulantes_asignados:
            return 0.0

        puntajes = [p.puntaje for p in postulantes_asignados]
        return min(puntajes)

    def __str__(self) -> str:
        return (f"Carrera: {self.nombre} | Cupos: {self.cupos_ofertados} "
                f"(Asignados: {self.cupos_asignados})")