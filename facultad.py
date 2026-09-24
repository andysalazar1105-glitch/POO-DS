import random


class Decano:
    """
    Representa al Decano de una facultad.
    Su función principal (con uso real) es aprobar becas
    según el rendimiento académico del estudiante.
    """

    def __init__(self, nombre, apellido, facultad, presupuesto_anual):
        self.id = random.randint(1000, 9999)
        self.nombre = nombre
        self.apellido = apellido
        self.facultad = facultad
        self.presupuesto_anual = presupuesto_anual

    def obtener_nombre_completo(self):
        return self.nombre + " " + self.apellido

    def aprobar_beca(self, estudiante, nota_minima=90):
        """
        Evalúa la nota del estudiante y decide si aprueba una beca.
        Retorna True/False según el resultado.
        """
        if estudiante.nota >= nota_minima:
            print(
                f"[Decanato] Beca APROBADA para {estudiante.obtener_nombre_completo()} "
                f"por el Decano {self.obtener_nombre_completo()}."
            )
            return True
        else:
            print(
                f"[Decanato] Beca NO aprobada para {estudiante.obtener_nombre_completo()} "
                f"(nota {estudiante.nota} menor a {nota_minima})."
            )
            return False

    def mostrar_informacion(self):
        print("Decano:", self.obtener_nombre_completo())
        print("Facultad:", self.facultad)
        print("Presupuesto anual: Q" + str(self.presupuesto_anual))
        print("-------------------------")


class Secretaria:
    """
    Representa a la Secretaria académica.
    Su función principal (con uso real) es generar un reporte
    en archivo con el estado de todos los estudiantes.
    """

    def __init__(self, nombre, apellido, departamento, turno):
        self.id = random.randint(1000, 9999)
        self.nombre = nombre
        self.apellido = apellido
        self.departamento = departamento
        self.turno = turno

    def obtener_nombre_completo(self):
        return self.nombre + " " + self.apellido

    def generar_reporte_estudiantes(self, estudiantes, nombre_archivo="reporte_estudiantes.txt"):
        """
        Crea un archivo de texto con el listado de estudiantes y su estado.
        Retorna True si se generó correctamente, False si hubo un error.
        """
        try:
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                archivo.write(f"Reporte generado por: {self.obtener_nombre_completo()}\n")
                archivo.write(f"Departamento: {self.departamento}\n")
                archivo.write("=========================================\n")
                for estudiante in estudiantes:
                    archivo.write(
                        f"{estudiante.obtener_nombre_completo()} - "
                        f"Nota: {estudiante.nota} - "
                        f"Estado: {estudiante.obtener_estado()}\n"
                    )
            print(f"[Secretaría] Reporte generado por {self.obtener_nombre_completo()}: {nombre_archivo}")
            return True
        except OSError:
            print("[Secretaría] No fue posible generar el reporte.")
            return False

    def mostrar_informacion(self):
        print("Secretaria:", self.obtener_nombre_completo())
        print("Departamento:", self.departamento)
        print("Turno:", self.turno)
        print("-------------------------")


class Profesor:
    """
    Representa a un Profesor.
    Su función principal (con uso real) es calificar/actualizar
    la nota de un estudiante en su materia.
    """

    def __init__(self, nombre, apellido, materia, anios_experiencia):
        self.id = random.randint(1000, 9999)
        self.nombre = nombre
        self.apellido = apellido
        self.materia = materia
        self.anios_experiencia = anios_experiencia

    def obtener_nombre_completo(self):
        return self.nombre + " " + self.apellido

    def calificar_estudiante(self, estudiante, nueva_nota):
        """
        Actualiza la nota de un estudiante y muestra el cambio realizado.
        """
        nota_anterior = estudiante.nota
        estudiante.nota = nueva_nota
        print(
            f"[{self.materia}] Prof. {self.obtener_nombre_completo()} actualizó la nota de "
            f"{estudiante.obtener_nombre_completo()}: {nota_anterior} -> {nueva_nota}"
        )

    def mostrar_informacion(self):
        print("Profesor:", self.obtener_nombre_completo())
        print("Materia:", self.materia)
        print("Años de experiencia:", self.anios_experiencia)
        print("-------------------------")
