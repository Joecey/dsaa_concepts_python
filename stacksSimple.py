def push(stack : list, item : str) -> list:
    return stack.append(item)
    
def pop(stack : list) -> list:
    # python has a built in pop method, but here we will use the slice method
    return stack[:-1]

def peek(stack : list) -> str:
    return stack[-1]
def empty(stack : list) -> bool:
    if len(stack) == 0:
        return True
    return False
    
def search(stack : list , item : str ) -> int:
    for i in range(len(stack)):
        if stack[i] == item:
            return i
    return -1

def main():
    print("Stacks")
    newStack = [];    
    print("Here, we have a new stack", newStack, empty(newStack))
    print("Now, let's add some items")
    push(newStack, "Minecraft")
    push(newStack, "Final Fantasy")
    push(newStack, "Helldivers 2")
    
    print(newStack, empty(newStack))
    
    print("Now, let's pop the latest item (in this case, Helldivers 2)")
    newStack = pop(newStack)
    print(newStack)
    
    print("What is the item on the top?", peek(newStack))
    print(search(newStack, "Final Fantasy"))
    print(search(newStack, "Minecraft"))
    print(search(newStack, "Risk of Rain 2"))

    
if __name__ == '__main__':
    main()