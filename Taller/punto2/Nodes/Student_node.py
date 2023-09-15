from Student.Student import Student
from Nodes.Node import Node

class Student_node(Node):
    def __init__(self, student: Student ,next: 'Student_node' = None) -> None:
        super().__init__(next)
        self.student = student
    
    def draw(self):

        super().draw(str(self.student))
        if self.next:
            print('    |')
            print('    V')
            self.next.draw()
