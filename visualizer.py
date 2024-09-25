from typing import List
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


def create_figure():
    """
    Creates a Matplotlib figure with two subplots:
    - Top subplot for the bar chart.
    - Bottom subplot for descriptive messages.

    Returns:
        Tuple[Figure, Axes, Axes, Text]:
            - fig: The Matplotlib figure object.
            - ax_bar: The Axes for the bar chart.
            - ax_text: The Axes for the messages.
            - message_text: The Text object for displaying messages.
    """
    fig, (ax_bar, ax_text) = plt.subplots(2, 1, figsize=(6, 4))
    fig.tight_layout(pad=3.0)

    # Bar chart configuration
    ax_bar.set_title("Sorting Visualization", fontsize=14)
    ax_bar.set_xlabel("Index", fontsize=10)
    ax_bar.set_ylabel("Value", fontsize=10)
    ax_bar.set_xlim(0, 1) 
    ax_bar.set_ylim(0, 1) 
    ax_bar.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Text box configuration
    ax_text.axis('off')  
    message_text = ax_text.text(0.5, 0.5, "", fontsize=10, ha='center', va='center', wrap=True)

    return fig, ax_bar, ax_text, message_text


def initialize_bars(ax_bar, array: List[int]):
    """
    Initializes the bar chart with the initial array.

    Args:
        ax_bar (Axes): The Axes object for the bar chart.
        array (List[int]): The array to visualize.

    Returns:
        BarContainer: The bar container object.
    """
    ax_bar.clear()
    ax_bar.set_title("Sorting Visualization", fontsize=14)
    ax_bar.set_xlabel("Index", fontsize=10)
    ax_bar.set_ylabel("Value", fontsize=10)
    ax_bar.set_xlim(0, len(array))
    ax_bar.set_ylim(0, max(array) * 1.1)
    ax_bar.grid(True, which='both', linestyle='--', linewidth=0.5)
    bars = ax_bar.bar(range(len(array)), array, align="edge", color='red')
    return bars


def update_visualization(bars, array: List[int], highlights: List[int], message_text, message: str):
    """
    Updates the bar chart and the descriptive message.

    Args:
        bars (BarContainer): The bar container object.
        array (List[int]): The current state of the array.
        highlights (List[int]): Indices to highlight in the current step.
        message_text (Text): The Text object for displaying messages.
        message (str): The descriptive message for the current step.
    """
    for bar, val in zip(bars, array):
        bar.set_height(val)
        bar.set_color('red')  

    for idx in highlights:
        if 0 <= idx < len(bars):
            bars[idx].set_color('blue')  

    message_text.set_text(message)


def visualize_sorting_gui(root, steps: List[List[int]], highlights: List[List[int]], messages: List[str], algorithm_name: str):
    """
    Sets up the Tkinter GUI for visualizing the sorting process with interactive controls.

    Args:
        root (Tk): The main Tkinter window.
        steps (List[List[int]]): List of array states after each operation.
        highlights (List[List[int]]): List of indices to highlight at each step.
        messages (List[str]): List of descriptive messages for each step.
        algorithm_name (str): The name of the sorting algorithm.
    """
    fig, ax_bar, ax_text, message_text = create_figure()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    bars = initialize_bars(ax_bar, steps[0])
    message_text.set_text(messages[0])

    current_step = [0] 
    is_playing = [False]

    def play():
        """
        Starts the automatic progression of the sorting visualization.
        """
        if not is_playing[0]:
            is_playing[0] = True
            advance_step()

    def stop():
        """
        Stops the automatic progression of the sorting visualization.
        """
        is_playing[0] = False

    def back():
        """
        Moves one step backward in the sorting visualization.
        """
        if current_step[0] > 0:
            current_step[0] -= 1
            update_visualization(
                bars,
                steps[current_step[0]],
                highlights[current_step[0]],
                message_text,
                messages[current_step[0]]
            )
            canvas.draw()

    def forward():
        """
        Moves one step forward in the sorting visualization.
        """
        if current_step[0] < len(steps) - 1:
            current_step[0] += 1
            update_visualization(
                bars,
                steps[current_step[0]],
                highlights[current_step[0]],
                message_text,
                messages[current_step[0]]
            )
            canvas.draw()

    def advance_step():
        """
        Advances the visualization by one step if playing.
        """
        if is_playing[0] and current_step[0] < len(steps) - 1:
            current_step[0] += 1
            update_visualization(
                bars,
                steps[current_step[0]],
                highlights[current_step[0]],
                message_text,
                messages[current_step[0]]
            )
            canvas.draw()
            root.after(500, advance_step) 

    control_frame = tk.Frame(root)
    control_frame.pack(side=tk.BOTTOM)

    play_button = tk.Button(control_frame, text="Play", command=play)
    play_button.pack(side=tk.LEFT, padx=5, pady=5)

    stop_button = tk.Button(control_frame, text="Stop", command=stop)
    stop_button.pack(side=tk.LEFT, padx=5, pady=5)

    back_button = tk.Button(control_frame, text="Back", command=back)
    back_button.pack(side=tk.LEFT, padx=5, pady=5)

    forward_button = tk.Button(control_frame, text="Forward", command=forward)
    forward_button.pack(side=tk.LEFT, padx=5, pady=5)

    ax_bar.set_title(f"{algorithm_name} Visualization", fontsize=14)
    canvas.draw()


def visualize_selection_sort(steps: List[List[int]], highlights: List[List[int]], messages: List[str]):
    """
    Launches the Tkinter window for Selection Sort visualization.

    Args:
        steps (List[List[int]]): List of array states after each operation.
        highlights (List[List[int]]): List of indices to highlight at each step.
        messages (List[str]): List of descriptive messages for each step.
    """
    root = tk.Tk()
    root.title("Selection Sort Visualization")
    visualize_sorting_gui(root, steps, highlights, messages, "Selection Sort")
    root.mainloop()


def visualize_bubble_sort(steps: List[List[int]], highlights: List[List[int]], messages: List[str]):
    """
    Launches the Tkinter window for Bubble Sort visualization.

    Args:
        steps (List[List[int]]): List of array states after each operation.
        highlights (List[List[int]]): List of indices to highlight at each step.
        messages (List[str]): List of descriptive messages for each step.
    """
    root = tk.Tk()
    root.title("Bubble Sort Visualization")
    visualize_sorting_gui(root, steps, highlights, messages, "Bubble Sort")
    root.mainloop()


def visualize_insertion_sort(steps: List[List[int]], highlights: List[List[int]], messages: List[str]):
    """
    Launches the Tkinter window for Insertion Sort visualization.

    Args:
        steps (List[List[int]]): List of array states after each operation.
        highlights (List[List[int]]): List of indices to highlight at each step.
        messages (List[str]): List of descriptive messages for each step.
    """
    root = tk.Tk()
    root.title("Insertion Sort Visualization")
    visualize_sorting_gui(root, steps, highlights, messages, "Insertion Sort")
    root.mainloop()


def visualize_heap_sort(steps: List[List[int]], highlights: List[List[int]], messages: List[str]):
    """
    Launches the Tkinter window for Heap Sort visualization.

    Args:
        steps (List[List[int]]): List of array states after each operation.
        highlights (List[List[int]]): List of indices to highlight at each step.
        messages (List[str]): List of descriptive messages for each step.
    """
    root = tk.Tk()
    root.title("Heap Sort Visualization")
    visualize_sorting_gui(root, steps, highlights, messages, "Heap Sort")
    root.mainloop()


def visualize_quick_sort(steps: List[List[int]], highlights: List[List[int]], messages: List[str]):
    """
    Launches the Tkinter window for Quick Sort visualization.

    Args:
        steps (List[List[int]]): List of array states after each operation.
        highlights (List[List[int]]): List of indices to highlight at each step.
        messages (List[str]): List of descriptive messages for each step.
    """
    root = tk.Tk()
    root.title("Quick Sort Visualization")
    visualize_sorting_gui(root, steps, highlights, messages, "Quick Sort")
    root.mainloop()


def visualize_merge_sort(steps: List[List[int]], highlights: List[List[int]], messages: List[str]):
    """
    Launches the Tkinter window for Merge Sort visualization.

    Args:
        steps (List[List[int]]): List of array states after each operation.
        highlights (List[List[int]]): List of indices to highlight at each step.
        messages (List[str]): List of descriptive messages for each step.
    """
    root = tk.Tk()
    root.title("Merge Sort Visualization")
    visualize_sorting_gui(root, steps, highlights, messages, "Merge Sort")
    root.mainloop()


def visualize_shell_sort(steps: List[List[int]], highlights: List[List[int]], messages: List[str]):
    """
    Launches the Tkinter window for Shell Sort visualization.

    Args:
        steps (List[List[int]]): List of array states after each operation.
        highlights (List[List[int]]): List of indices to highlight at each step.
        messages (List[str]): List of descriptive messages for each step.
    """
    root = tk.Tk()
    root.title("Shell Sort Visualization")
    visualize_sorting_gui(root, steps, highlights, messages, "Shell Sort")
    root.mainloop()


def visualize_counting_sort(steps: List[List[int]], highlights: List[List[int]], messages: List[str]):
    """
    Launches the Tkinter window for Counting Sort visualization.

    Args:
        steps (List[List[int]]): List of array states after each operation.
        highlights (List[List[int]]): List of indices to highlight at each step.
        messages (List[str]): List of descriptive messages for each step.
    """
    root = tk.Tk()
    root.title("Counting Sort Visualization")
    visualize_sorting_gui(root, steps, highlights, messages, "Counting Sort")
    root.mainloop()


def visualize_radix_sort(steps: List[List[int]], highlights: List[List[int]], messages: List[str]):
    """
    Launches the Tkinter window for Radix Sort visualization.

    Args:
        steps (List[List[int]]): List of array states after each operation.
        highlights (List[List[int]]): List of indices to highlight at each step.
        messages (List[str]): List of descriptive messages for each step.
    """
    root = tk.Tk()
    root.title("Radix Sort Visualization")
    visualize_sorting_gui(root, steps, highlights, messages, "Radix Sort")
    root.mainloop()


def visualize_cocktail_shaker_sort(steps: List[List[int]], highlights: List[List[int]], messages: List[str]):
    """
    Launches the Tkinter window for Cocktail Shaker Sort visualization.

    Args:
        steps (List[List[int]]): List of array states after each operation.
        highlights (List[List[int]]): List of indices to highlight at each step.
        messages (List[str]): List of descriptive messages for each step.
    """
    root = tk.Tk()
    root.title("Cocktail Shaker Sort Visualization")
    visualize_sorting_gui(root, steps, highlights, messages, "Cocktail Shaker Sort")
    root.mainloop()
