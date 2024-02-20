
class DynamicArray:
    
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.count = 0
        self.array = [0] * capacity # this class will be initialize with capacity of capacity
        
    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n
        
    def resize(self):
        """
        It will be macking the array twice as big
        """
        self.array = self.array + ([0] * len(self.array))
        self.capacity *= 2
        
    def pushback(self, n: int):
        """
        it will push the element `n` to the end of the array

        Args:
            n (int): the element what you put in this array
        """
        if self.is_full():
            self.resize()
        
        self.array[self.count] = n
        self.count += 1
        
    def popback(self) -> int:
        poped = self.array[self.count - 1]
        self.array[self.count - 1] = 0 # make the element at the end of the array is zero (empty)
        self.count -= 1
        return poped
    
    def is_full(self) -> bool:
        return self.count == self.capacity
    
    def getSize(self) -> int:
        return self.count
    
    def getCapacity(self) -> int:
        return self.capacity