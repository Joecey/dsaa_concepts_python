from StructureClasses.Stack import Stack

def data_structure_example():
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

def main():
    print("Stack Data Structure (LIFO)")
    data_structure_example()
    
    
if __name__ == '__main__':
    main()