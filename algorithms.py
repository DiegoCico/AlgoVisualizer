def selection_sort(arr: List[int]) -> List[List[int]]:
    steps = []
    steps.append(arr.copy())

    for i in range(len(arr)): 
        min_idx = i
        for j in len(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_idx = j
        if min_idx != i: 
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            steps.append(arr.copy())

    return steps

def bubble_sort(arr: List[int]) -> List[List[int]]:
steps = []
steps.append(arr.copy())  

n = len(arr)
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            steps.append(arr.copy()) 

return steps

def merge_sort(arr: List[int]) -> List[List[int]]:
    steps = []
    steps.append(arr.copy())  

    def merge_sort_recursive(sub_arr: List[int]) -> List[int]:
        if len(sub_arr) > 1:
            mid = len(sub_arr) // 2
            left_half = sub_arr[:mid]
            right_half = sub_arr[mid:]

            merge_sort_recursive(left_half)
            merge_sort_recursive(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    sub_arr[k] = left_half[i]
                    i += 1
                else:
                    sub_arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                sub_arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                sub_arr[k] = right_half[j]
                j += 1
                k += 1

            steps.append(arr.copy())

        return sub_arr

    merge_sort_recursive(arr)
    return steps
            
