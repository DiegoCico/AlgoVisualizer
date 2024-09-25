import random
from multiprocessing import Process
from algorithms import (
    selection_sort,
    bubble_sort,
    insertion_sort,
    heap_sort,
    quick_sort,
    merge_sort,
    shell_sort,
    counting_sort,
    radix_sort,
    cocktail_shaker_sort
)
from visualizer import (
    visualize_selection_sort,
    visualize_bubble_sort,
    visualize_insertion_sort,
    visualize_heap_sort,
    visualize_quick_sort,
    visualize_merge_sort,
    visualize_shell_sort,
    visualize_counting_sort,
    visualize_radix_sort,
    visualize_cocktail_shaker_sort
)


def run_visualization(sort_func, visualize_func, array):
    """
    Runs the sorting algorithm and its visualization.

    Args:
        sort_func (Callable): The sorting function to execute.
        visualize_func (Callable): The visualization function to display the sorting process.
        array (List[int]): The array to sort.
    """
    steps, highlights, messages = sort_func(array.copy())
    visualize_func(steps, highlights, messages)


def main():
    """
    Main function to execute sorting algorithms and their visualizations.
    """
    array_size = 20 
    array = [random.randint(1, 100) for _ in range(array_size)]
    print("Original array:", array)

    sorting_algorithms = [
        ("Selection Sort", selection_sort, visualize_selection_sort),
        ("Bubble Sort", bubble_sort, visualize_bubble_sort),
        ("Insertion Sort", insertion_sort, visualize_insertion_sort),
        ("Heap Sort", heap_sort, visualize_heap_sort),
        ("Quick Sort", quick_sort, visualize_quick_sort),
        ("Merge Sort", merge_sort, visualize_merge_sort),
        ("Shell Sort", shell_sort, visualize_shell_sort),
        ("Counting Sort", counting_sort, visualize_counting_sort),
        ("Radix Sort", radix_sort, visualize_radix_sort),
        ("Cocktail Shaker Sort", cocktail_shaker_sort, visualize_cocktail_shaker_sort)
    ]

    processes = []

    for name, sort_func, visualize_func in sorting_algorithms:
        print(f"\nPerforming {name}...")
        p = Process(target=run_visualization, args=(sort_func, visualize_func, array))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()


if __name__ == "__main__":
    main()
