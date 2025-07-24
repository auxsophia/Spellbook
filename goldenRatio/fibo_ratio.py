import math

def fibonacci_recursive(n, a=0, b=1, count=3, prev_ratio=0.0, precision=3):
    """
    Recursively calculates the Fibonacci sequence and demonstrates its
    relationship with the golden ratio.

    Args:
        n (int): The total number of Fibonacci numbers to generate.
        a (int): The first of the two previous numbers in the sequence.
        b (int): The second of the two previous numbers in the sequence.
        count (int): The current step in the sequence generation.
        prev_ratio (float): The ratio from the previous step.
        precision (int): The decimal precision for printing the ratio.
    """
    # Base case: Stop when we have generated n numbers.
    if count > n:
        print("\nCalculation complete.")
        return

    # Calculate the next number in the sequence.
    next_fib = a + b
    print(f"Step {count}: {next_fib}")

    # Calculate the ratio, handle division by zero for the early terms.
    if a != 0:
        current_ratio = b / a
        
        # Format strings for comparison and printing
        format_str = f"{{:.{precision}f}}"
        
        # Compare the truncated versions of the current and previous ratios
        if format_str.format(current_ratio) == format_str.format(prev_ratio):
             # If they are the same, increase precision for the next step
            precision += 1
            format_str = f"{{:.{precision}f}}"

        print(f"  -> Ratio (n-1/n-2): {b}/{a} ≈ {format_str.format(current_ratio)}")
        
        # Set the new previous ratio for the next recursive call
        prev_ratio = current_ratio

    # The recursive call
    # The new 'a' is the old 'b', and the new 'b' is 'next_fib'.
    fibonacci_recursive(n, b, next_fib, count + 1, prev_ratio, precision)


def main():
    """
    Main function to drive the script. Explains the concept and gets user input.
    """
    print("=" * 60)
    print("   Welcome to the Fibonacci Sequence & Golden Ratio Explorer!")
    print("=" * 60)
    print("\nThe Fibonacci sequence is a series of numbers where each number")
    print("is the sum of the two preceding ones, usually starting with 0 and 1.")
    print("\nAn amazing property of this sequence is the ratio between consecutive")
    print("numbers. As the sequence progresses, this ratio gets closer and closer")
    print("to the Golden Ratio (φ), an irrational number approximately equal")
    print("to 1.61803398875...")
    print("\nThis script will generate the Fibonacci sequence and show this")
    print("convergence in action. As the ratio stabilizes at a certain")
    print("decimal precision, we will add another digit to show how")
    print("the approximation continues to improve.")
    print("-" * 60)

    while True:
        try:
            num_terms = int(input("\nEnter the number of Fibonacci terms to generate (must be > 2): "))
            if num_terms > 2:
                break
            else:
                print("Please enter a number greater than 2.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print("\n--- Generating Fibonacci Sequence ---")
    
    # Handle the first two terms manually before starting recursion
    print("Step 1: 0")
    print("Step 2: 1")
    print("  -> Ratio (n-1/n-2): 1/0 ≈ Not a number")

    # Start the recursion from the 3rd term
    # Initial 'a' is 1, 'b' is 1, to calculate the third term (which is 2)
    # The first ratio to calculate will be 1/1 = 1
    fibonacci_recursive(num_terms, a=1, b=1, count=3, prev_ratio=1.0)


if __name__ == "__main__":
    main()
