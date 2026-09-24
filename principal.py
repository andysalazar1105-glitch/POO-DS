from estudiante import Estudiante
from facultad import Decano, Secretaria, Profesor


# Crear objetos o instancias de estudiantes
estudiante1 = Estudiante("Ana", "López", 85)
estudiante2 = Estudiante("Carlos", "Pérez", 58)
estudiante3 = Estudiante("María", "Gómez", 92)

# Guardar los objetos en una lista
estudiantes = [
    estudiante1,
    estudiante2,
    estudiante3
]


# Crear personal de la facultad
decano1 = Decano("Roberto", "Méndez", "Ingeniería en Sistemas", 500000)
secretaria1 = Secretaria("Laura", "Ramírez", "Control Académico", "Matutino")
profesor1 = Profesor("Jorge", "Castillo", "Programación I", 12)


# Mostrar todos los estudiantes
print("--- LISTADO DE ESTUDIANTES ---")
for estudiante in estudiantes:
    estudiante.mostrar_informacion()


# Mostrar personal de la facultad
print("--- PERSONAL DE LA FACULTAD ---")
decano1.mostrar_informacion()
secretaria1.mostrar_informacion()
profesor1.mostrar_informacion()


# CASO DE USO 1: el profesor corrige/actualiza la nota de un estudiante
print("--- ACTUALIZACIÓN DE NOTAS (Profesor) ---")
profesor1.calificar_estudiante(estudiante2, 65)
print("-------------------------")


# CASO DE USO 2: el decano evalúa a cada estudiante para aprobar becas
print("--- EVALUACIÓN DE BECAS (Decano) ---")
for estudiante in estudiantes:
    decano1.aprobar_beca(estudiante, nota_minima=90)
print("-------------------------")


# CASO DE USO 3: la secretaria genera un reporte oficial en archivo
print("--- GENERACIÓN DE REPORTE (Secretaria) ---")
secretaria1.generar_reporte_estudiantes(estudiantes)
print("-------------------------")


# Guardar los estudiantes en un archivo (funcionalidad original)
try:
    with open("calificaciones.txt", "w", encoding="utf-8") as archivo:

        for estudiante in estudiantes:
            linea = estudiante.convertir_a_texto()
            archivo.write(linea + "\n")

    print("Los estudiantes fueron guardados.")

except OSError:
    print("No fue posible escribir en el archivo.")
