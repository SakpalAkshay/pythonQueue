class Queue:
    #based upon the concept of First In First Out
    
    def __init__(self):
        self.__array = []
        self.__count = 0
        self.__front = 0 
        
    def enqueue(self,data):
        self.__array.append(data)
        self.__count+=1
    
    def dequeue(self):
        if self.__count==0:
            return -1
        
        element = self.__array[self.__front]
        self.__front+=1
        self.__count-=1
        return element

    def size(self):
        return self.__count
    
    def front(self):
        if self.size() == 0:
            return -1
        return self.__array[self.__front]
    
    def isEmpty(self):
        
        return self.size() == 0
    
    
queue = Queue()
queue.enqueue(1)
print(queue.front()) #1
queue.enqueue(2)
queue.enqueue(3)
print(queue.size()) #3
print(queue.dequeue()) #1
print(queue.front()) #2
print(queue.size())#2
        
