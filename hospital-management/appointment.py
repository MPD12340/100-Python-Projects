import heapq


class AppointmentScheduler:
    """
    A class to manage and schedule patient appointments based on priority.

    Methods
    -------
    __init__():
        Initializes the AppointmentScheduler with an empty list of appointments.

    schedule_appointment():
        Prompts the user to input a patient ID and priority, and schedules an appointment
        by adding it to the priority queue.

    view_appointments():
        Displays all scheduled appointments in priority order. If no appointments exist,
        it notifies the user.

    manage_appointments():
        Provides a menu-driven interface for scheduling, viewing, and exiting the appointment
        management system.
    """
    def __init__(self):
        self.appointments = []

    def schedule_appointment(self):
        patient_id = int(input("Enter patient ID: "))
        priority = int(input("Enter priority (1- High, 2- Medium, 3- Low): "))
        heapq.heappush(self.appointments, (priority, patient_id))
        print("Appointment scheduled!")

    def view_appointments(self):
        if not self.appointments:
            print("No appointments!")
            return

        temp = self.appointments.copy()
        print("\n=== Appointments (Priority Order) ===")
        while temp:
            priority, pid = heapq.heappop(temp)
            print(f"Patient ID: {pid}, Priority: {priority}")

    def manage_appointments(self):
        while True:
            print("\n1. Schedule Appointment\n2. View Appointments\n3. Back")
            choice = int(input("Enter choice: "))
            if choice == 1:
                self.schedule_appointment()
            elif choice == 2:
                self.view_appointments()
            elif choice == 3:
                break
            else:
                print("Invalid choice!")
