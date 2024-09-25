from typing import List, Tuple

def selection_sort(arr: List[int]) -> Tuple[List[List[int]], List[List[int]], List[str]]:
    """
    Performs Selection Sort on the input array.

    Args:
        arr (List[int]): The array to sort.

    Returns:
        Tuple[List[List[int]], List[List[int]], List[str]]:
            - steps: List of array states after each operation.
            - highlights: List of indices to highlight at each step.
            - messages: List of descriptive messages for each step.
    """
    steps = []
    highlights = []
    messages = []
    steps.append(arr.copy())
    highlights.append([])
    messages.append("Initial array")

    for i in range(len(arr)):
        min_idx = i
        messages.append(f"Selecting index {i} as the initial minimum.")
        for j in range(i + 1, len(arr)):
            highlights.append([min_idx, j])
            steps.append(arr.copy())
            messages.append(f"Comparing index {min_idx} (value {arr[min_idx]}) with index {j} (value {arr[j]}).")
            if arr[min_idx] > arr[j]:
                min_idx = j
                messages.append(f"New minimum found at index {min_idx} (value {arr[min_idx]}).")
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            steps.append(arr.copy())
            highlights.append([i, min_idx])
            messages.append(f"Swapped index {i} (value {arr[i]}) with index {min_idx} (value {arr[min_idx]}).")
        else:
            highlights.append([])
            messages.append("No swap needed.")
    messages.append("Selection Sort completed.")
    return steps, highlights, messages


def bubble_sort(arr: List[int]) -> Tuple[List[List[int]], List[List[int]], List[str]]:
    """
    Performs Bubble Sort on the input array.

    Args:
        arr (List[int]): The array to sort.

    Returns:
        Tuple[List[List[int]], List[List[int]], List[str]]:
            - steps: List of array states after each operation.
            - highlights: List of indices to highlight at each step.
            - messages: List of descriptive messages for each step.
    """
    steps = []
    highlights = []
    messages = []
    steps.append(arr.copy())
    highlights.append([])
    messages.append("Initial array")

    n = len(arr)
    for i in range(n):
        swapped = False
        messages.append(f"Starting pass {i + 1}.")
        for j in range(0, n - i - 1):
            highlights.append([j, j + 1])
            steps.append(arr.copy())
            messages.append(f"Comparing index {j} (value {arr[j]}) with index {j + 1} (value {arr[j + 1]}).")
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append(arr.copy())
                highlights.append([j, j + 1])
                messages.append(f"Swapped index {j} (value {arr[j]}) with index {j + 1} (value {arr[j + 1]}).")
                swapped = True
        if not swapped:
            messages.append("No swaps in this pass. Array is sorted.")
            break
    messages.append("Bubble Sort completed.")
    return steps, highlights, messages


def insertion_sort(arr: List[int]) -> Tuple[List[List[int]], List[List[int]], List[str]]:
    """
    Performs Insertion Sort on the input array.

    Args:
        arr (List[int]): The array to sort.

    Returns:
        Tuple[List[List[int]], List[List[int]], List[str]]:
            - steps: List of array states after each operation.
            - highlights: List of indices to highlight at each step.
            - messages: List of descriptive messages for each step.
    """
    steps = []
    highlights = []
    messages = []
    steps.append(arr.copy())
    highlights.append([])
    messages.append("Initial array")

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        messages.append(f"Inserting element at index {i} (value {key}).")
        while j >= 0 and key < arr[j]:
            highlights.append([j, j + 1])
            steps.append(arr.copy())
            messages.append(f"Comparing key (value {key}) with index {j} (value {arr[j]}).")
            arr[j + 1] = arr[j]
            steps.append(arr.copy())
            highlights.append([j, j + 1])
            messages.append(f"Moved value {arr[j]} from index {j} to index {j + 1}.")
            j -= 1
        arr[j + 1] = key
        steps.append(arr.copy())
        highlights.append([j + 1])
        messages.append(f"Inserted key (value {key}) at index {j + 1}.")
    messages.append("Insertion Sort completed.")
    return steps, highlights, messages


def heap_sort(arr: List[int]) -> Tuple[List[List[int]], List[List[int]], List[str]]:
    """
    Performs Heap Sort on the input array.

    Args:
        arr (List[int]): The array to sort.

    Returns:
        Tuple[List[List[int]], List[List[int]], List[str]]:
            - steps: List of array states after each operation.
            - highlights: List of indices to highlight at each step.
            - messages: List of descriptive messages for each step.
    """
    steps = []
    highlights = []
    messages = []
    steps.append(arr.copy())
    highlights.append([])
    messages.append("Initial array")

    n = len(arr)

    def heapify(n: int, i: int):
        """
        Ensures the subtree rooted at index i satisfies the heap property.

        Args:
            n (int): Size of the heap.
            i (int): Root index of the subtree.
        """
        largest = i
        l = 2 * i + 1     
        r = 2 * i + 2    

        if l < n:
            highlights.append([largest, l])
            steps.append(arr.copy())
            messages.append(f"Comparing index {largest} (value {arr[largest]}) with left child index {l} (value {arr[l]}).")
            if arr[l] > arr[largest]:
                largest = l
                messages.append(f"New largest found at index {largest} (value {arr[largest]}).")

        if r < n:
            highlights.append([largest, r])
            steps.append(arr.copy())
            messages.append(f"Comparing index {largest} (value {arr[largest]}) with right child index {r} (value {arr[r]}).")
            if arr[r] > arr[largest]:
                largest = r
                messages.append(f"New largest found at index {largest} (value {arr[largest]}).")

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i] 
            steps.append(arr.copy())
            highlights.append([i, largest])
            messages.append(f"Swapped index {i} (value {arr[i]}) with index {largest} (value {arr[largest]}).")
            heapify(n, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        steps.append(arr.copy())
        highlights.append([0, i])
        messages.append(f"Swapped index 0 (value {arr[0]}) with index {i} (value {arr[i]}).")
        heapify(i, 0)
    messages.append("Heap Sort completed.")
    return steps, highlights, messages


def quick_sort(arr: List[int]) -> Tuple[List[List[int]], List[List[int]], List[str]]:
    """
    Performs Quick Sort on the input array.

    Args:
        arr (List[int]): The array to sort.

    Returns:
        Tuple[List[List[int]], List[List[int]], List[str]]:
            - steps: List of array states after each operation.
            - highlights: List of indices to highlight at each step.
            - messages: List of descriptive messages for each step.
    """
    steps = []
    highlights = []
    messages = []
    steps.append(arr.copy())
    highlights.append([])
    messages.append("Initial array")

    def quick_sort_recursive(low: int, high: int):
        """
        Recursively applies Quick Sort on the subarrays.

        Args:
            low (int): Starting index of the subarray.
            high (int): Ending index of the subarray.
        """
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    def partition(low: int, high: int) -> int:
        """
        Partitions the array around a pivot element.

        Args:
            low (int): Starting index for the partition.
            high (int): Ending index for the partition.

        Returns:
            int: The partitioning index.
        """
        pivot = arr[high]
        i = low - 1
        messages.append(f"Choosing pivot at index {high} (value {pivot}).")
        for j in range(low, high):
            highlights.append([j, high])
            steps.append(arr.copy())
            messages.append(f"Comparing index {j} (value {arr[j]}) with pivot index {high} (value {pivot}).")
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                steps.append(arr.copy())
                highlights.append([i, j])
                messages.append(f"Swapped index {i} (value {arr[i]}) with index {j} (value {arr[j]}).")
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        steps.append(arr.copy())
        highlights.append([i + 1, high])
        messages.append(f"Swapped pivot index {i + 1} (value {arr[i + 1]}) with index {high} (value {arr[high]}).")
        return i + 1

    quick_sort_recursive(0, len(arr) - 1)
    messages.append("Quick Sort completed.")
    return steps, highlights, messages


def merge_sort(arr: List[int]) -> Tuple[List[List[int]], List[List[int]], List[str]]:
    """
    Performs Merge Sort on the input array.

    Args:
        arr (List[int]): The array to sort.

    Returns:
        Tuple[List[List[int]], List[List[int]], List[str]]:
            - steps: List of array states after each merge operation.
            - highlights: List of indices to highlight at each step.
            - messages: List of descriptive messages for each merge operation.
    """
    steps = []
    highlights = []
    messages = []
    steps.append(arr.copy())
    highlights.append([])
    messages.append("Initial array")

    def merge_sort_recursive(sub_arr: List[int], start: int):
        """
        Recursively divides and merges the array.

        Args:
            sub_arr (List[int]): The subarray to sort.
            start (int): The starting index of the subarray in the original array.
        """
        if len(sub_arr) > 1:
            mid = len(sub_arr) // 2
            left_half = sub_arr[:mid]
            right_half = sub_arr[mid:]

            merge_sort_recursive(left_half, start)
            merge_sort_recursive(right_half, start + mid)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                highlights.append([start + k])
                steps.append(arr.copy())
                messages.append(f"Merging: Comparing {left_half[i]} (left) with {right_half[j]} (right).")
                if left_half[i] < right_half[j]:
                    arr[start + k] = left_half[i]
                    messages.append(f"Placed {left_half[i]} from left into position {start + k}.")
                    i += 1
                else:
                    arr[start + k] = right_half[j]
                    messages.append(f"Placed {right_half[j]} from right into position {start + k}.")
                    j += 1
                k += 1

            while i < len(left_half):
                arr[start + k] = left_half[i]
                highlights.append([start + k])
                steps.append(arr.copy())
                messages.append(f"Placed {left_half[i]} from left into position {start + k}.")
                i += 1
                k += 1

            while j < len(right_half):
                arr[start + k] = right_half[j]
                highlights.append([start + k])
                steps.append(arr.copy())
                messages.append(f"Placed {right_half[j]} from right into position {start + k}.")
                j += 1
                k += 1

            messages.append(f"Merged subarrays into positions {start} to {start + k - 1}.")

    merge_sort_recursive(arr, 0)
    messages.append("Merge Sort completed.")
    return steps, highlights, messages


def shell_sort(arr: List[int]) -> Tuple[List[List[int]], List[List[int]], List[str]]:
    """
    Performs Shell Sort on the input array.

    Args:
        arr (List[int]): The array to sort.

    Returns:
        Tuple[List[List[int]], List[List[int]], List[str]]:
            - steps: List of array states after each gap insertion.
            - highlights: List of indices to highlight at each step.
            - messages: List of descriptive messages for each step.
    """
    steps = []
    highlights = []
    messages = []
    steps.append(arr.copy())
    highlights.append([])
    messages.append("Initial array")

    n = len(arr)
    gap = n // 2

    while gap > 0:
        messages.append(f"Using gap size {gap}.")
        for i in range(gap, n):
            temp = arr[i]
            j = i
            messages.append(f"Comparing index {j - gap} (value {arr[j - gap]}) with index {j} (value {temp}).")
            while j >= gap and arr[j - gap] > temp:
                highlights.append([j - gap, j])
                arr[j] = arr[j - gap]
                steps.append(arr.copy())
                messages.append(f"Moved value {arr[j - gap]} from index {j - gap} to index {j}.")
                j -= gap
            arr[j] = temp
            steps.append(arr.copy())
            highlights.append([j])
            messages.append(f"Inserted value {temp} at index {j}.")
        gap //= 2
    messages.append("Shell Sort completed.")
    return steps, highlights, messages


def counting_sort(arr: List[int]) -> Tuple[List[List[int]], List[List[int]], List[str]]:
    """
    Performs Counting Sort on the input array.

    Args:
        arr (List[int]): The array to sort.

    Returns:
        Tuple[List[List[int]], List[List[int]], List[str]]:
            - steps: List of array states after counting and placing elements.
            - highlights: List of indices to highlight at each step.
            - messages: List of descriptive messages for each step.
    """
    steps = []
    highlights = []
    messages = []
    steps.append(arr.copy())
    highlights.append([])
    messages.append("Initial array")

    if not arr:
        messages.append("Empty array. Nothing to sort.")
        return steps, highlights, messages

    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)

    for number in arr:
        count[number - min_val] += 1
        highlights.append([number - min_val])
        steps.append(count.copy())
        messages.append(f"Counting number {number}. Current count: {count[number - min_val]}.")

    for i in range(1, len(count)):
        count[i] += count[i - 1]
        highlights.append([i])
        steps.append(count.copy())
        messages.append(f"Updating count for value {i + min_val -1}: {count[i]}.")

    for number in reversed(arr):
        output[count[number - min_val] - 1] = number
        count[number - min_val] -= 1
        highlights.append([number - min_val])
        steps.append(count.copy())
        messages.append(f"Placing number {number} at position {count[number - min_val]}.")

    for i in range(len(arr)):
        arr[i] = output[i]
        highlights.append([i])
        steps.append(arr.copy())
        messages.append(f"Setting arr[{i}] to {arr[i]}.")

    messages.append("Counting Sort completed.")
    return steps, highlights, messages


def radix_sort(arr: List[int]) -> Tuple[List[List[int]], List[List[int]], List[str]]:
    """
    Performs Radix Sort on the input array.

    Args:
        arr (List[int]): The array to sort.

    Returns:
        Tuple[List[List[int]], List[List[int]], List[str]]:
            - steps: List of array states after each digit placement.
            - highlights: List of indices to highlight at each step.
            - messages: List of descriptive messages for each step.
    """
    steps = []
    highlights = []
    messages = []
    steps.append(arr.copy())
    highlights.append([])
    messages.append("Initial array")

    if not arr:
        messages.append("Empty array. Nothing to sort.")
        return steps, highlights, messages

    max_val = max(arr)
    exp = 1  

    while max_val // exp > 0:
        messages.append(f"Sorting based on digit at exponent {exp}.")
        count = [0] * 10
        output = [0] * len(arr)

        for number in arr:
            index = (number // exp) % 10
            count[index] += 1
            highlights.append([index])
            steps.append(count.copy())
            messages.append(f"Counting digit {index}.")

        for i in range(1, 10):
            count[i] += count[i - 1]
            highlights.append([i])
            steps.append(count.copy())
            messages.append(f"Updating count for digit {i}: {count[i]}.")

        for i in range(len(arr)-1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            highlights.append([index])
            steps.append(count.copy())
            messages.append(f"Placing number {arr[i]} at position {count[index]}.")

        for i in range(len(arr)):
            arr[i] = output[i]
            highlights.append([i])
            steps.append(arr.copy())
            messages.append(f"Setting arr[{i}] to {arr[i]}.")

        exp *= 10
    messages.append("Radix Sort completed.")
    return steps, highlights, messages


def cocktail_shaker_sort(arr: List[int]) -> Tuple[List[List[int]], List[List[int]], List[str]]:
    """
    Performs Cocktail Shaker Sort on the input array.

    Args:
        arr (List[int]): The array to sort.

    Returns:
        Tuple[List[List[int]], List[List[int]], List[str]]:
            - steps: List of array states after each swap.
            - highlights: List of indices to highlight at each step.
            - messages: List of descriptive messages for each step.
    """
    steps = []
    highlights = []
    messages = []
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    steps.append(arr.copy())
    highlights.append([])
    messages.append("Initial array")

    while swapped:
        swapped = False
        for i in range(start, end):
            highlights.append([i, i + 1])
            steps.append(arr.copy())
            messages.append(f"Comparing index {i} (value {arr[i]}) with index {i + 1} (value {arr[i + 1]}).")
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                steps.append(arr.copy())
                highlights.append([i, i + 1])
                messages.append(f"Swapped index {i} (value {arr[i]}) with index {i + 1} (value {arr[i + 1]}).")
        if not swapped:
            break
        swapped = False
        end -= 1

        # Traverse the array from right to left
        for i in range(end - 1, start - 1, -1):
            highlights.append([i, i + 1])
            steps.append(arr.copy())
            messages.append(f"Comparing index {i} (value {arr[i]}) with index {i + 1} (value {arr[i + 1]}).")
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                steps.append(arr.copy())
                highlights.append([i, i + 1])
                messages.append(f"Swapped index {i} (value {arr[i]}) with index {i + 1} (value {arr[i + 1]}).")
        start += 1

    messages.append("Cocktail Shaker Sort completed.")
    return steps, highlights, messages
