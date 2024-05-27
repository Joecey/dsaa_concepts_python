from StructureClasses.Stack import Stack

def main():
    print("Stack Data Structure (LIFO)")
    newStack = Stack()
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
    
if __name__ == '__main__':
    main()