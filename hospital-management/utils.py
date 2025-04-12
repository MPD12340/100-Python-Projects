def display_menu():
    print("\n=== Hospital Management System ===")
    print("1. Patient Records")
    print("2. Appointment Scheduler")
    print("3. Medicine Inventory")
    print("4. Exit")


def get_valid_input(prompt, input_type=int, min_val=None, max_val=None):
    """
    Prompt the user for input, validate it, and return the valid input.

    This function repeatedly prompts the user until a valid input is provided.
    The input is validated based on the specified type and optional range.

    Args:
        prompt (str): The message displayed to the user when asking for input.
        input_type (type, optional): The expected type of the input. Defaults to int.
        min_val (optional): The minimum acceptable value for the input. Defaults to None.
        max_val (optional): The maximum acceptable value for the input. Defaults to None.

    Returns:
        input_type: The validated user input converted to the specified type.

    Raises:
        ValueError: If the input is not of the expected type or falls outside the specified range.
    """
    while True:
        try:
            user_input = input_type(input(prompt))
            if (min_val is not None and user_input < min_val) or (
                max_val is not None and user_input > max_val
            ):
                raise ValueError
            return user_input
        except ValueError:
            print("Invalid input! Try again.")
