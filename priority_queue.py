class Task:
    """
    Represents a task in the scheduler.
    Higher priority value = higher priority.
    """
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __repr__(self):
        return (
            f"Task(id={self.task_id}, priority={self.priority}, "
            f"arrival={self.arrival_time}, deadline={self.deadline})"
        )


class PriorityQueue:
    """
    Max-heap based priority queue using a Python list.
    """
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if self.is_empty():
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def increase_key(self, task_id, new_priority):
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                if new_priority < task.priority:
                    raise ValueError("New priority must be greater than current priority.")
                task.priority = new_priority
                self._heapify_up(i)
                return
        raise ValueError("Task not found.")

    def decrease_key(self, task_id, new_priority):
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                if new_priority > task.priority:
                    raise ValueError("New priority must be lower than current priority.")
                task.priority = new_priority
                self._heapify_down(i)
                return
        raise ValueError("Task not found.")

    def _heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)].priority < self.heap[i].priority:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def _heapify_down(self, i):
        largest = i
        left = self.left(i)
        right = self.right(i)

        if left < len(self.heap) and self.heap[left].priority > self.heap[largest].priority:
            largest = left

        if right < len(self.heap) and self.heap[right].priority > self.heap[largest].priority:
            largest = right

        if largest != i:
            self.swap(i, largest)
            self._heapify_down(largest)