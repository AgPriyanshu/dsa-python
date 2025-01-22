class Queue:
    def __init__(self):
        self.start = -1
        self.end = -1
        self.currSize = 0
        self.maxSize = 16
        self.arr = [0] * self.maxSize

    def push(self, newElement: int) -> None:
        if self.currSize == self.maxSize:
            print("Queue is full\nExiting...")
            exit(1)
        if self.end == -1:
            self.start = 0
            self.end = 0
        else:
            self.end = (self.end + 1) % self.maxSize
        self.arr[self.end] = newElement
        print("The element pushed is", newElement)
        self.currSize += 1

    def pop(self) -> int:
        if self.start == -1:
            print("Queue Empty\nExiting...")
        popped = self.arr[self.start]
        if self.currSize == 1:
            self.start = -1
            self.end = -1
        else:
            self.start = (self.start + 1) % self.maxSize
        self.currSize -= 1
        return popped

    def top(self) -> int:
        if self.start == -1:
            print("Queue is Empty")
            exit(1)
        return self.arr[self.start]

    def size(self) -> int:
        return self.currSize

    def __str__(self):
        current = self.start
        result = ""
        while current <= self.end:
            result += str(self.arr[current])
            result += "\n" if current != self.end else ""
            current += 1
        return result


if __name__ == "__main__":
    queue = Queue()
    queue.push(1)
    queue.push(56)
    queue.push(11231)
    queue.push(1304)
    queue.push(54)
    queue.push(112310)
    print(queue)
    print("--------------")
    print(queue.pop())
    print("--------------")
    print(queue)
