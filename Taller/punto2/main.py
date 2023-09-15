'''
    2. crear 40 nodos con la siguiente información:
    ID, 
    Name_Student, 
    LastName_Studente, 
    Favorite_teacher, 
    Age, 
    Semestre, 
    carrera
'''
import random

from Student.Student import Student
from Nodes.Student_node import Student_node
from LinkedList.Linked_list import Linked_list

# Datos
from data import *

def main():
    linked_list = Linked_list()

    for i in range(40):
        new_student = Student(i, 
                              random.choice(names), 
                              random.choice(surnames),
                              int((random.random() * 10) + 18), 
                              random.choice(teachers_names),  
                              int((random.random() * 10) + 1), 
                              random.choice(careers)
                            )
        new_student_node = Student_node(new_student)
        linked_list.add_end(new_student_node)

    linked_list.draw()


if __name__ == '__main__':
    main()