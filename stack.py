# Creating stack
stack = []

def push(item):
    stack.append(item)
    print(item, "pushed into stack")

def pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print(stack.pop(), "popped from stack")
def display():
    print("Stack elements:", stack)

push(10)
push(20)
push(30)

display()

pop()
display()