import math
import shutil

def visualize_ratio_plot(ratio, width=50):
    """
    Creates an ASCII plot to visualize the current ratio in relation to
    the golden ratio (φ) on a number line from 1.0 to 2.0.
    """
    phi = (1 + math.sqrt(5)) / 2
    plot_min, plot_max = 1.0, 2.0
    
    if not (plot_min <= ratio <= plot_max):
        return

    ratio_pos = int((ratio - plot_min) / (plot_max - plot_min) * width)
    ratio_pos = max(0, min(width, ratio_pos))
    phi_pos = int((phi - plot_min) / (plot_max - plot_min) * width)

    plot = ['-'] * (width + 1)
    plot[phi_pos] = '|'
    plot[ratio_pos] = '*'
    if ratio_pos == phi_pos:
        plot[ratio_pos] = 'X'

    print(f"  -> Plot:  [1.0 {''.join(plot)}] 2.0   (* = Current Ratio, | = φ)")


def fibonacci_recursive(n, a=0, b=1, count=3, prev_ratio=0.0, precision=3):
    """
    Recursively calculates the Fibonacci sequence and its relationship to the
    golden ratio with text-based visualizations and dynamic precision.
    """
    if count > n:
        print("\nConsole visualization complete.")
        return

    # Define the Golden Ratio
    phi = (1 + math.sqrt(5)) / 2

    next_fib = a + b
    print(f"Step {count}: {next_fib}")
    
    try:
        terminal_width = shutil.get_terminal_size((80, 20)).columns
    except OSError:
        terminal_width = 80
        
    current_precision = precision

    if a > 0:
        current_ratio = b / a
        
        # Format string for comparison based on the precision from the last step
        comparison_format_str = f"{{:.{current_precision}f}}"
        
        # Check if the ratio has stabilized at this precision
        if comparison_format_str.format(current_ratio) == comparison_format_str.format(prev_ratio):
            # If so, increase precision for the CURRENT step's display
            current_precision += 1

        # Format string for the CURRENT step's display, using the potentially updated precision
        display_format_str = f"{{:.{current_precision}f}}"
        
        # Print the ratio and phi to the current level of precision
        print(f"  -> Ratio: {b}/{a} ≈ {display_format_str.format(current_ratio)} (φ ≈ {display_format_str.format(phi)})")

        visualize_ratio_plot(current_ratio)
        prev_ratio = current_ratio
    
    print("-" * (terminal_width - 2))
    # Make the recursive call with the potentially increased precision
    fibonacci_recursive(n, b, next_fib, count + 1, prev_ratio, current_precision)


def main():
    """
    Main function to drive the script. Explains the concept and gets user input.
    """
    try:
        terminal_width = shutil.get_terminal_size((80, 20)).columns
    except OSError:
        terminal_width = 80
    
    print("=" * terminal_width)
    print("   Welcome to the Fibonacci Sequence & Golden Ratio Explorer!".center(terminal_width))
    print("=" * terminal_width)
    print("\nThis script visualizes the Fibonacci sequence and its amazing".center(terminal_width))
    print("relationship to the Golden Ratio (φ ≈ 1.618).".center(terminal_width))
    print("\nAt each step, you'll see the ratio of consecutive numbers converge on φ.")
    print("-" * terminal_width)

    while True:
        try:
            num_terms = int(input("\nEnter the number of Fibonacci terms to generate (e.g., 15): "))
            if num_terms > 2:
                break
            else:
                print("Please enter a number greater than 2.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print("\n--- Generating Console Visualization ---\n")
    print("Step 1: 0\n" + "-" * (terminal_width-2))
    print("Step 2: 1\n  -> Ratio: 1/0 ≈ Not a number\n" + "-" * (terminal_width-2))
    
    # Start the recursion
    fibonacci_recursive(num_terms, a=1, b=1, count=3, prev_ratio=1.0)


if __name__ == "__main__":
    main()
