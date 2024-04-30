import Signature as sig


class Students:
    def __init__(self, age, name, gender, grade):
        self.age = age
        self.name = name
        self.gender = gender
        self.grade = grade

    def printAge(self):
        return f"El alumno {self.name} tienen {self.age} años de edad"
    ###la f antes indica que puede recibir las variables dentro del texto


myStudent = Students(age=21, name="Liss", gender="F", grade="9°A")

print(myStudent.printAge())

grades = {"unidad 1": 9, "unidad 2": 8, "unidad 3": 9, "unidad 4": 8, "unidad 5": 10}

mySignature = sig.Signature("Estructura de datos", "Max Carsi", 5, grades, True, 9)

print(mySignature.printUnits())
print(mySignature.printTeacher())
print(mySignature.printGrades())
print("Las calificaciones del estudiante son:")
for clave, valor in mySignature.grades.items():
    print(clave, ":", valor)
    print()

if mySignature.retunrAproved():
    print("Se aprobo la materia")
else:
    print("No aprobo la materia")
