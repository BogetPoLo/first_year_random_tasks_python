class MinStack:
    def __init__(self) -> None:
        self.stack = []
        self.minn = []


    def push(self, value: int) -> None:
        """Добавляет элемент в стек (и делает стек минимальных чисел)"""
        self.stack.append(value)
        if not self.minn:
            self.minn.append(value)
        elif self.stack[-1] <= self.minn[-1]:
            self.minn.append(value)


    def pop(self) -> None:
        """Удаляет из стека минимальное число"""
        if self.stack[-1] == self.minn[-1]:
            del self.minn[-1]
        self.stack.pop()


    def top(self) -> int:
        """Возвращает самое последнее вхождение"""
        return self.stack[-1]


    def get_min(self) -> None:
        """Возвращает минимальное число"""
        return self.minn[-1]


stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
print(stack.get_min())  # -3
stack.pop()
print(stack.top())  # 0
print(stack.get_min())  # -2
print()