class InventoryManager:
    """
    A class to manage an inventory of medicines.

    Methods
    -------
    __init__():
        Initializes the inventory as an empty dictionary.

    add_medicine():
        Prompts the user to input medicine details (ID, name, and quantity)
        and adds the medicine to the inventory.

    search_medicine():
        Prompts the user to input a medicine ID and searches for the medicine
        in the inventory. Displays the medicine details if found, otherwise
        notifies the user that the medicine is not found.

    manage_inventory():
        Provides a menu-driven interface to add medicines, search for medicines,
        or exit the inventory management system.
    """
    def __init__(self):
        self.inventory = {}

    def add_medicine(self):
        med_id = input("Enter medicine ID: ")
        name = input("Enter medicine name: ")
        quantity = int(input("Enter quantity: "))
        self.inventory[med_id] = {"name": name, "quantity": quantity}
        print(f"Medicine {name} added!")

    def search_medicine(self):
        med_id = input("Enter medicine ID: ")
        medicine = self.inventory.get(med_id)
        if medicine:
            print(f"Name: {medicine['name']}, Quantity: {medicine['quantity']}")
        else:
            print("Medicine not found!")

    def manage_inventory(self):
        while True:
            print("\n1. Add Medicine\n2. Search Medicine\n3. Back")
            choice = int(input("Enter choice: "))
            if choice == 1:
                self.add_medicine()
            elif choice == 2:
                self.search_medicine()
            elif choice == 3:
                break
            else:
                print("Invalid choice!")
