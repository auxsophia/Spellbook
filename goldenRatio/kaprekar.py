import random

def kaprekars_constant(n):
    """
    Performs Kaprekar's routine on a given 4-digit number.

    Args:
        n (int): A 4-digit integer with at least two different digits.
    """
    print(f"\nStarting the routine with the number: {n}")
    print("-" * 35)
    
    current_number = n
    step = 0

    # The loop will continue until the number is 6174
    while current_number != 6174 and step < 7:
        step += 1
        
        # Pad the number with leading zeros if it's less than 4 digits
        s_num = str(current_number).zfill(4)
        
        # Create the ascending and descending numbers
        ascending_digits = sorted(s_num)
        descending_digits = sorted(s_num, reverse=True)
        
        ascending_str = "".join(ascending_digits)
        descending_str = "".join(descending_digits)
        
        ascending_num = int(ascending_str)
        descending_num = int(descending_str)
        
        # Perform the subtraction
        current_number = descending_num - ascending_num
        
        print(f"Step {step}: {descending_str} - {ascending_str} = {current_number}")

    if current_number == 6174:
        print("\nWe have reached Kaprekar's Constant: 6174!")
    else:
        print("\nCould not reach Kaprekar's constant within the maximum iterations.")
    print("-" * 35)


def is_valid(num_str):
    """
    Validates if a number is a 4-digit number and has at least two
    different digits.

    Args:
        num_str (str): The number as a string.

    Returns:
        bool: True if the number is valid, False otherwise.
    """
    # Check if the input is a 4-digit number
    if not num_str.isdigit() or len(num_str) != 4:
        print("Error: Please enter a valid 4-digit number.")
        return False
        
    # Check if all digits are the same by converting to a set
    if len(set(num_str)) == 1:
        print("Error: The number must have at least two different digits.")
        return False
        
    return True

def main():
    """
    Main function to run the Kaprekar's Constant program.
    """
    print("--- Welcome to the Kaprekar's Constant Explorer ---")
    print("This fascinating mathematical property states that for any four-digit")
    print("number (with at least two different digits), repeatedly arranging its")
    print("digits into the largest and smallest possible numbers and subtracting")
    print("them will always lead you to the number 6174.")
    print("-" * 55)

    while True:
        choice = input(
            "\nChoose an option:\n"
            "1. Enter your own 4-digit number.\n"
            "2. Generate a random 4-digit number.\n"
            "3. Exit.\n"
            "Your choice: "
        )

        number_str = ""
        if choice == '1':
            number_str = input("Please enter a 4-digit number: ")
            if not is_valid(number_str):
                continue
        elif choice == '2':
            # Generate a random number until a valid one is found
            while True:
                number_str = str(random.randint(1000, 9999))
                if is_valid(number_str):
                    print(f"Generated random number: {number_str}")
                    break
        elif choice == '3':
            print("Thank you for exploring Kaprekar's Constant. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        kaprekars_constant(int(number_str))

if __name__ == "__main__":
    main()
