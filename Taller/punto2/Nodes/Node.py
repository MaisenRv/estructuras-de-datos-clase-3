class Node:
    def __init__(self, next:'Node' = None) -> None:
        self.next = next
    
    def draw(self,info):
        print(info)