class Stack:
    def __init__(self):
        self.top = -1
        self.max_size = 1000
        self.arr = [0] * self.max_size

    def push(self, value):
        self.top += 1
        self.arr[self.top] = value

    def pop(self):
        popped_value = self.arr[self.top]
        del self.arr[self.top]
        self.top -= 1
        return popped_value

    def __str__(self):
        current = self.top
        result = ""
        while current != -1:
            result += str(self.arr[current])
            result += "\n" if current != 0 else ""
            current -= 1

        return result

    def top_value(self):
        return self.arr[self.top]

    def size(self):
        return self.top + 1


if __name__ == "__main__":
    stack = Stack()
    stack.push("1")
    stack.push(56)
    stack.push(11231)
    stack.push(1304)
    stack.push(54)
    stack.push(112310)
    print(stack)
    print("--------------")
    print(stack.pop())
    print("--------------")
    print(stack)
