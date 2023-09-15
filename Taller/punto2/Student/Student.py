class Student:
    def __init__(self, ID, name_student, lastName_student, age, favorite_teacher, semester, career) -> None:
        self.ID = ID
        self.name_student = name_student
        self.lastName_student = lastName_student
        self.age = age
        self.favorite_teacher = favorite_teacher
        self.semester = semester
        self.career = career
    
    def __str__(self) -> str:
        return (f' ID: {self.ID}\n'
                f' Nombre: {self.name_student}\n'
                f' Apellido: {self.lastName_student}\n'
                f' Edad: {self.age}\n'
                f' Profesor favorito: {self.favorite_teacher}\n'
                f' Semestre: {self.semester}\n'
                f' Carrera: {self.career}\n'
                )

        
        