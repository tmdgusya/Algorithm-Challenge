
class DynamicArray:
    
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.count = 0
        self.array = [0] * capacity
    
    
    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.count == self.capacity:
            self.resize()
        self.array[self.count] = n
        self.count += 1

    def popback(self) -> int:
        ele = self.array[self.count - 1]
        self.array[self.count - 1] = 0
        self.count -= 1
        return ele

    def resize(self) -> None:
        new_array = [0] * (self.capacity * 2)
        self.memcopy(new_array, self.array, self.capacity)
        self.array = new_array
        self.capacity *= 2
    
    def memcopy(self, new_array: list, array: list, capacity: int) -> None:
        for i in range(capacity):
            new_array[i] = array[i]

    def getSize(self) -> int:
        return self.count
    
    def getCapacity(self) -> int:
        return self.capacity