from matplotlib import pyplot as plt
from matplotlib import animation
import random

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def bubble_sort(arr):
    swapped = True
    highlight_bars = [] # Store indices of bars being compared

    for i in range(len(arr)-1):
        if not swapped:
            return # If no swaps, the array is sorted
        swapped = False 

        # Comparisons and swapping
        for j in range(len(arr)-1-i):
            highlight_bars = [j, j+1] 
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
                swapped = True # Indicates swap occured
            yield arr, highlight_bars

def visualize():
    arr_size = 35
    arr = list(range(1,arr_size+1))
    random.shuffle(arr)

    generator = bubble_sort(arr)

    # Creates a bar plot
    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort O(n\N{SUPERSCRIPT TWO})")
    bars = ax.bar(range(len(arr)), arr, align = "edge")

    ax.set_xlim(0,arr_size)

    # Update bar heights and colors during visualization
    def update(data):
        arr, highlight_bars = data
        for i, rect in enumerate(bars):
            rect.set_height(arr[i])
            if i in highlight_bars:
                rect.set_color("magenta") # Highlights compared bars in magenta
            else:
                rect.set_color("black") # If not compared, black
                
    # Creates animation object
    anim = animation.FuncAnimation(
        fig,
        func = update, # update will be called at each frame
        frames = generator, # generator has data needed for each frame
        blit = False,
        interval = 15, # Each frame will be displayed for 15 ms
        save_count = 90000, # Animation can consist of up to 90 000 frames
    )

    # Show animation
    plt.show()
    plt.close()

if __name__ == '__main__':
    visualize()