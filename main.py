from StructureClasses.Stack import Stack
from queue import Queue

def stack_example():
    newStack = Stack()
    print(newStack.empty())
    newStack.push("Minecraft")
    newStack.push("Final Fantasy")
    newStack.push("Halo")
    newStack.push("Helldivers 2")
    print(newStack.stack, newStack.empty())
    newStack.pop()
    print(newStack.stack)
    newStack.pop()
    print(newStack.peek())
    print(newStack.search("Minecraft"))
    print(newStack.search("Helldivers 2"))

def queue_built_in_example():
    built_in_queue = Queue(maxsize = 5) # create a queue with a max size of 5
    print("Is this queue empty?", built_in_queue.empty())
    built_in_queue.put("Karen")
    built_in_queue.put("Liam")
    built_in_queue.put("Margret")
    built_in_queue.put("John Bone")
    built_in_queue.put("Meself")
    print("Is this queue empty?", built_in_queue.empty(), built_in_queue, built_in_queue.full())
    
    if built_in_queue.full():
        print("queue is full")
    else:
        built_in_queue.put("this shouldn't be possible")
    

    print(list(built_in_queue.queue), built_in_queue.qsize())
    while built_in_queue.empty() == False:
        print(built_in_queue.get())
        print(list(built_in_queue.queue), built_in_queue.qsize())
    
    # ! note, built in Queue is non iterable. You either have to extend it or create your own one
    class UniqueQueue:

        def __init__(self):
            self.__item_pool = []

        def push(self, item):
            if item not in self.__item_pool:
                self.__item_pool.append(item)

        def pop(self):
            return self.__item_pool.pop()



def main():
    print("Stack Data Structure (LIFO)")
    stack_example()
    
    print("Queue Data Structure (FIFO)")
    queue_built_in_example()
    
    
    
if __name__ == '__main__':
    main()