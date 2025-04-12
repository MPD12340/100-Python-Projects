from patient import PatientManager
from appointment import AppointmentScheduler
from inventory import InventoryManager
from utils import display_menu, get_valid_input


def main():
    """
    Main function to run the application.

    This function initializes the core components of the application, including
    the PatientManager, AppointmentScheduler, and InventoryManager. It then
    displays a menu in a loop, allowing the user to manage patients, appointments,
    and inventory, or exit the application.

    Menu Options:
    1. Manage patients
    2. Manage appointments
    3. Manage inventory
    4. Exit the application

    The function ensures valid input is received and performs the corresponding
    action based on the user's choice.

    Raises:
        ValueError: If the input is not a valid integer within the specified range.
    """
    patient_manager = PatientManager()
    appointment_scheduler = AppointmentScheduler()
    inventory_manager = InventoryManager()

    while True:
        display_menu()
        choice = get_valid_input("Enter your choice (1-5): ", int, 1, 5)

        if choice == 1:
            patient_manager.manage_patients()
        elif choice == 2:
            appointment_scheduler.manage_appointments()
        elif choice == 3:
            inventory_manager.manage_inventory()
        elif choice == 4:
            print("\nExiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
