import time

MAX_SIZE = 1000


class Node:
    def __init__(self, data: str):
        self.data = data
        self.next = None


# --- A) STATIC STACK (Fixed-size pre-allocated list) ---
class StaticStack:
    def __init__(self, capacity: int = MAX_SIZE):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.top = -1

    def is_empty(self) -> bool:
        return self.top == -1

    def push(self, c: str):
        if self.top < self.capacity - 1:
            self.top += 1
            self.arr[self.top] = c

    def pop(self) -> str:
        if self.is_empty():
            return ""
        c = self.arr[self.top]
        self.arr[self.top] = None
        self.top -= 1
        return c


# --- A) DYNAMIC QUEUE (Linked List) ---
class DynamicQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self) -> bool:
        return self.front is None

    def enqueue(self, c: str):
        new_node = Node(c)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self) -> str:
        if self.is_empty():
            return ""
        c = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return c


# --- B) DYNAMIC STACK (Linked List) ---
class DynamicStack:
    def __init__(self):
        self.top = None

    def is_empty(self) -> bool:
        return self.top is None

    def push(self, c: str):
        new_node = Node(c)
        new_node.next = self.top
        self.top = new_node

    def pop(self) -> str:
        if self.is_empty():
            return ""
        c = self.top.data
        self.top = self.top.next
        return c


# --- B) STATIC QUEUE (Circular pre-allocated list) ---
class StaticQueue:
    def __init__(self, capacity: int = MAX_SIZE):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.count = 0

    def is_empty(self) -> bool:
        return self.count == 0

    def enqueue(self, c: str):
        if self.count < self.capacity:
            self.arr[self.rear] = c
            self.rear = (self.rear + 1) % self.capacity
            self.count += 1

    def dequeue(self) -> str:
        if self.is_empty():
            return ""
        c = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return c


def check_method_a(word: str) -> tuple[bool, int, int]:
    start = time.perf_counter_ns()
    cycles = 0
    result = True

    s = StaticStack()
    q = DynamicQueue()

    for c in word.lower():
        cycles += 1
        s.push(c)
        q.enqueue(c)

    while not s.is_empty() and not q.is_empty():
        cycles += 1
        if s.pop() != q.dequeue():
            result = False
            break

    duration = time.perf_counter_ns() - start
    return result, cycles, duration


def check_method_b(word: str) -> tuple[bool, int, int]:
    start = time.perf_counter_ns()
    cycles = 0
    result = True

    s = DynamicStack()
    q = StaticQueue()

    for c in word.lower():
        cycles += 1
        s.push(c)
        q.enqueue(c)

    while not s.is_empty() and not q.is_empty():
        cycles += 1
        if s.pop() != q.dequeue():
            result = False
            break

    duration = time.perf_counter_ns() - start
    return result, cycles, duration


if __name__ == "__main__":
    word = input("Enter a word: ").strip()

    res_a, cycles_a, time_a = check_method_a(word)
    res_b, cycles_b, time_b = check_method_b(word)

    print("\n--- Option A (Static Stack + Dynamic Queue) ---")
    print(f"Result: {'Palindrome' if res_a else 'Not a palindrome'}")
    print(f"Cycles: {cycles_a}")
    print(f"Time:   {time_a} ns ({time_a / 1000.0:.3f} us)")

    print("\n--- Option B (Dynamic Stack + Static Queue) ---")
    print(f"Result: {'Palindrome' if res_b else 'Not a palindrome'}")
    print(f"Cycles: {cycles_b}")
    print(f"Time:   {time_b} ns ({time_b / 1000.0:.3f} us)")