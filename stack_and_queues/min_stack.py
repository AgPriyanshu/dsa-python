class MinStack:
    def __init__(self):
        self.top_index = -1
        self.arr = [tuple()] * (3 * 10**4)

    def push(self, val: int) -> None:
        if self.top_index == -1:
            min_val = val
        else:
            min_val = min(self.arr[self.top_index][1], val)

        self.top_index += 1
        self.arr[self.top_index] = (
            val,
            min_val,
        )

    def pop(self) -> None:
        del self.arr[self.top_index]
        self.top_index -= 1
        return None

    def top(self) -> int:
        return self.arr[self.top_index][0]

    def getMin(self) -> int:
        return self.arr[self.top_index][1]

    def __str__(self):
        current = self.top_index
        result = ""
        while current != -1:
            result += f"{str(self.arr[current][0])},{str(self.arr[current][1])}"
            result += "\n" if current != 0 else ""
            current -= 1

        return result


if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    print(obj.push(2147483646))
    print(obj.push(2147483646))
    print(obj.push(2147483647))
    print(obj.top())
    print(obj.pop())
    print(obj.getMin())
    print(obj.pop())
    print(obj.getMin())
    print(obj.pop())
    print(obj.push(2147483647))
    print(obj.top())
    print(obj.getMin())
    print(obj.push(-2147483648))
    print(obj.top())
    print(obj.getMin())
    print(obj.pop())
    print(obj.getMin())
    # print(obj)
