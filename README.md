# Advanced Priority Queue and Heapsort with Edge Case Handling

## Project Overview

This project includes an advanced implementation of Heapsort and a Priority Queue that supports additional operations like increasing and decreasing task priorities. Both implementations are based on a max-heap, represented as a list in Python. Special emphasis is placed on handling edge cases and supporting dynamic changes to task priorities.

### Heapsort Implementation with Edge Case Handling

The Heapsort algorithm in this project includes error handling for cases where the input array may be empty or contain only one element. After building the max-heap, the algorithm sorts the array in-place by repeatedly extracting the maximum element, ensuring the array is sorted in descending order.

#### Key Features:
- **Edge Case Handling:** Checks for empty and single-element arrays.
- **Heapify:** Maintains the heap property for subtrees.
- **Heapsort:** Builds the max-heap and performs in-place sorting.

### Priority Queue with Increase/Decrease Key Operations

The priority queue implementation is extended to include operations that allow dynamically adjusting the priority of tasks that are already in the queue. This version also ensures proper heap property maintenance when task priorities change.

#### Key Features:
- **Insert:** Adds a new task to the queue, maintaining the max-heap property.
- **Extract Max:** Removes the task with the highest priority.
- **Increase/Decrease Key:** Adjusts the priority of an existing task, either increasing or decreasing it.
- **Is Empty:** Checks if the queue is empty.

---

## How to Run the Code

### Heapsort with Edge Case Handling
1. Clone the repository.
2. Navigate to the project directory.
3. Run the Heapsort implementation with edge case handling:
    ```python
    arr = [19, 2, 31, 45, 6, 11]
    heapsort(arr)
    print("Sorted array:", arr)
    ```

### Priority Queue with Dynamic Priority Adjustment
1. Instantiate the `PriorityQueue` class.
2. Insert tasks with a task ID and priority.
3. Adjust the priority of tasks using `increase_key()` or `decrease_key()`:
    ```python
    pq = PriorityQueue()
    pq.insert(Task("Task1", 3))
    pq.insert(Task("Task2", 7))
    pq.increase_key("Task1", 8)
    print(pq.extract_max())
    ```

## File Structure

- **heapsort_advanced.py:** Contains the enhanced implementation of the Heapsort algorithm with edge case handling.
- **priority_queue_advanced.py:** Contains the priority queue with additional operations like `increase_key` and `decrease_key`.
- **README.md:** This file.

---

## Time Complexity Analysis

- **Heapsort:**
  - Worst-case, Best-case, and Average-case time complexity: O(n log n)
  - Space complexity: O(1)
  
- **Priority Queue Operations:**
  - Insertion and Extraction: O(log n)
  - Increase/Decrease Key: O(log n)
  - Space complexity: O(n)

---

## License

This project is licensed under the MIT License.
