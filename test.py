import random
import time
from heapsort import heapsort, randomized_quicksort, merge_sort
from priority_queue import Task, PriorityQueue


def test_sorting_algorithms():
    sizes = [1000, 3000, 5000]

    for size in sizes:
        print(f"\nArray Size: {size}")

        arr = [random.randint(0, 10000) for _ in range(size)]
        sorted_arr = sorted(arr)
        reverse_arr = sorted(arr, reverse=True)

        datasets = {
            "Random": arr,
            "Sorted": sorted_arr,
            "Reverse": reverse_arr
        }

        for name, data in datasets.items():
            print(f"\n{name} Data:")

            start = time.time()
            heapsort(data.copy())
            print("Heapsort Time:", time.time() - start)

            start = time.time()
            randomized_quicksort(data.copy())
            print("Quicksort Time:", time.time() - start)

            start = time.time()
            merge_sort(data.copy())
            print("Merge Sort Time:", time.time() - start)


def test_priority_queue():
    print("\n--- Priority Queue / Task Scheduler Test ---")

    pq = PriorityQueue()

    tasks = [
        Task("T1", 4, 0, 10),
        Task("T2", 8, 1, 7),
        Task("T3", 3, 2, 12),
        Task("T4", 10, 3, 5),
    ]

    for task in tasks:
        pq.insert(task)

    print("\nTasks inserted into priority queue:")
    for item in pq.heap:
        print(item)

    print("\nExtract highest priority task:")
    print(pq.extract_max())

    print("\nIncrease priority of T3 to 12:")
    pq.increase_key("T3", 12)
    for item in pq.heap:
        print(item)

    print("\nDecrease priority of T2 to 2:")
    pq.decrease_key("T2", 2)
    for item in pq.heap:
        print(item)

    print("\nProcess remaining tasks in priority order:")
    while not pq.is_empty():
        print(pq.extract_max())


if __name__ == "__main__":
    test_sorting_algorithms()
    test_priority_queue()