class LinkedList:
    
    def __init__(self):
        self.l_list : List[int] = []

    
    def get(self, index: int) -> int:
        if index < len(self.l_list):
            return self.l_list[index]
        return -1
        

    def insertHead(self, val: int) -> None:
        self.l_list = [val] + self.l_list
        

    def insertTail(self, val: int) -> None:
        self.l_list = self.l_list + [val]
        

    def remove(self, index: int) -> bool:
        if index < len(self.l_list):
            self.l_list = self.l_list[:index ] + self.l_list[index + 1:]
            return True
        return False
        

    def getValues(self) -> List[int]:
        return self.l_list
        
