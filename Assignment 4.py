import random  # Importing random module for generating random numbers

# Define a new class 'CustomHashTable' for our new version of hash table
class CustomHashTable:
    def __init__(self, capacity=8):
        """
        Initialize the custom hash table with a default capacity of 8.
        Use an array of empty lists to store key-value pairs.
        """
        self.capacity = capacity  # Total number of buckets in the hash table
        self.table = [[] for _ in range(capacity)]  # Create empty buckets
        self.total_elements = 0  # Track the number of key-value pairs

    def compute_hash(self, key):
        """
        Generate the hash index for a given key using the hash function.
        The modulo operation ensures that the index stays within bounds.
        """
        return hash(key) % self.capacity

    def add(self, key, value):
        """
        Insert or update the key-value pair in the hash table.
        If the key already exists, update the value.
        """
        idx = self.compute_hash(key)  # Compute the index for this key
        for i, (k, v) in enumerate(self.table[idx]):  # Check if key exists
            if k == key:  # If key is found, update the value
                self.table[idx][i] = (key, value)
                return  # Exit after updating the key-value pair
        self.table[idx].append((key, value))  # If key not found, append the new pair
        self.total_elements += 1  # Increase element count

        # Resize if the table is more than 80% full
        if self.calculate_load_factor() > 0.8:
            self.expand_table()

    def search(self, key):
        """
        Search for a key in the hash table and return its value.
        If the key is not found, return None.
        """
        idx = self.compute_hash(key)  # Compute the index for this key
        for k, v in self.table[idx]:  # Look for the key in the correct bucket
            if k == key:
                return v  # Return the value if the key is found
        return None  # Return None if the key is not present

    def remove(self, key):
        """
        Delete a key-value pair from the hash table.
        Return True if successful, False if the key does not exist.
        """
        idx = self.compute_hash(key)  # Compute the index for this key
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:  # If the key is found, delete it
                del self.table[idx][i]  # Remove the key-value pair
                self.total_elements -= 1  # Decrease the element count
                return True  # Return success
        return False  # Return False if the key was not found

    def calculate_load_factor(self):
        """
        Calculate the load factor of the hash table, defined as
        the ratio of elements to the capacity of the hash table.
        """
        return self.total_elements / self.capacity

    def expand_table(self):
        """
        Double the capacity of the hash table and rehash all the existing elements.
        This helps maintain efficiency as the table grows.
        """
        new_capacity = self.capacity * 2  # Double the size of the table
        new_table = [[] for _ in range(new_capacity)]  # Create new empty buckets

        # Rehash all the elements into the new table
        for bucket in self.table:
            for key, value in bucket:
                new_idx = hash(key) % new_capacity  # Recompute the index
                new_table[new_idx].append((key, value))  # Place in new bucket

        self.capacity = new_capacity  # Update the capacity
        self.table = new_table  # Replace the old table with the new one

    def show(self):
        """
        Display the current state of the hash table, showing
        all the key-value pairs in each bucket.
        """
        for idx, bucket in enumerate(self.table):
            print(f"Bucket {idx}: {bucket}")

import random  # Importing random module to generate random numbers

# Define a new class 'QuickSortComparison' for comparing the sorting algorithms
class QuickSortComparison:
    def __init__(self, size):
        """
        Initialize the class with an array of a given size. The array
        can be filled with random numbers for testing.
        """
        self.array = [random.randint(0, 1000) for _ in range(size)]  # Create random array

    def random_quicksort(self, low, high):
        """
        Implement Randomized Quicksort with random pivot selection.
        The array is sorted by selecting a random pivot and partitioning.
        """
        if low < high:
            pivot_idx = self.random_partition(low, high)
            self.random_quicksort(low, pivot_idx - 1)  # Sort left of pivot
            self.random_quicksort(pivot_idx + 1, high)  # Sort right of pivot

    def random_partition(self, low, high):
        """
        Select a random pivot and partition the array around the pivot.
        """
        random_idx = random.randint(low, high)  # Select a random index for the pivot
        self.array[high], self.array[random_idx] = self.array[random_idx], self.array[high]  # Swap pivot
        return self.partition(low, high)  # Perform partitioning

    def partition(self, low, high):
        """
        Partition the array such that elements less than the pivot
        are on the left, and elements greater are on the right.
        """
        pivot = self.array[high]  # Pivot is the last element
        i = low - 1  # Pointer for elements smaller than pivot
        for j in range(low, high):
            if self.array[j] <= pivot:  # Move smaller elements to the left
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]  # Swap pivot to correct position
        return i + 1  # Return pivot index

    def iterative_deterministic_quicksort(self, low, high):
        """
        Implement Iterative Quicksort using the first element as pivot.
        This avoids recursion by using an explicit stack.
        """
        stack = [(low, high)]  # Initialize stack with initial subarray

        while stack:
            low, high = stack.pop()  # Get subarray boundaries from the stack
            if low < high:
                pivot_idx = self.partition(low, high)  # Partition using first element as pivot

                # Add left and right subarrays to the stack for sorting
                if pivot_idx - 1 > low:
                    stack.append((low, pivot_idx - 1))
                if pivot_idx + 1 < high:
                    stack.append((pivot_idx + 1, high))

    def display_array(self):
        """
        Display the current state of the array being sorted.
        """
        print(self.array)

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child
    right = 2 * i + 2  # right child

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swap and continue heapifying if root is not the largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Heapify the root

def heapsort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)  # Heapify the reduced heap

# Example usage
arr = [12, 11, 13, 5, 6, 7]
heapsort(arr)
print("Sorted array is:", arr)

class Task:
    def __init__(self, task_id, priority):
        self.task_id = task_id
        self.priority = priority

    def __repr__(self):
        return f"Task(ID={self.task_id}, Priority={self.priority})"

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move the last element to the root
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index].priority > self.heap[parent].priority:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left].priority > self.heap[largest].priority:
            largest = left
        if right < len(self.heap) and self.heap[right].priority > self.heap[largest].priority:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def is_empty(self):
        return len(self.heap) == 0

# Example Usage
pq = PriorityQueue()
pq.insert(Task("Task1", 2))
pq.insert(Task("Task2", 5))
pq.insert(Task("Task3", 1))

print("Max priority task extracted:", pq.extract_max())
print("Max priority task extracted:", pq.extract_max())
print("Max priority task extracted:", pq.extract_max())