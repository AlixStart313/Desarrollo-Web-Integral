class Signature:
    def __init__(self, name, teacher,units,grades,aproved,finalGrade):
        self.name = name
        self.teacher = teacher
        self.units = units
        self.grades = grades
        self.aproved = aproved
        self.finalGrade = finalGrade



    def printUnits(self):
        return f"La materia {self.name} tiene {self.units} unidades tematicas"

    def printTeacher(self):
        return f"La materia {self.name} es impartida por el profesor {self.teacher}"

    def printGrades(self):
        return f"En la materia {self.name} tienes {self.finalGrade} de promedio Final"

    def retunrGrades(self):
        return self.grades

    def retunrAproved(self):
        return self.aproved

