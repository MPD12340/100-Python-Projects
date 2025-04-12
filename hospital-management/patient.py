class PatientManager:
    def __init__(self):
        self.patients = []

    def add_patient(self):
        """
        Adds a new patient to the patient list.

        Prompts the user to input the patient's name and age, generates a unique
        patient ID based on the current number of patients, and appends the new
        patient information to the patients list.

        Attributes:
            name (str): The name of the patient entered by the user.
            age (int): The age of the patient entered by the user.
            patient_id (int): A unique identifier for the patient, generated
                              based on the current number of patients.

        Side Effects:
            Modifies the `self.patients` list by appending a dictionary containing
            the new patient's ID, name, and age.
            Prints a success message indicating the patient has been added.

        Raises:
            ValueError: If the input for age cannot be converted to an integer.
        """
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        patient_id = len(self.patients) + 1
        self.patients.append({"id": patient_id, "name": name, "age": age})
        print(f"Patient {name} added successfully!")

    def display_patients(self):
        if not self.patients:
            print("No patients found!")
            return

        # Sort patients by name (Insertion Sort)
        for i in range(1, len(self.patients)):
            key = self.patients[i]
            j = i - 1
            while j >= 0 and key["name"] < self.patients[j]["name"]:
                self.patients[j + 1] = self.patients[j]
                j -= 1
            self.patients[j + 1] = key

        print("\n=== Patient Records (Sorted by Name) ===")
        for patient in self.patients:
            print(
                f"ID: {patient['id']}, Name: {patient['name']}, Age: {patient['age']}"
            )

    def manage_patients(self):
        while True:
            print("\n1. Add Patient\n2. View Patients\n3. Back")
            choice = int(input("Enter choice: "))
            if choice == 1:
                self.add_patient()
            elif choice == 2:
                self.display_patients()
            elif choice == 3:
                break
            else:
                print("Invalid choice!")
