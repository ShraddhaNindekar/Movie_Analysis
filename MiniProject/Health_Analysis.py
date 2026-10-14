patients = {}

def add_patient():
    try:
        pid = int(input("Enter patient ID: "))
    except ValueError:
        print("Please enter a valid numeric patient ID.")
        return

    if pid in patients:
        print("Patient already exists.")
        return

    name = input("Enter patient name: ")
    disease = input("Enter disease: ")

    patients[pid] = {"name": name, "disease": disease}
    print("Patient added successfully.")


def view_patient():
    if not patients:
        print("No patients available.")
        return

    for pid, details in patients.items():
        print(f"Patient ID: {pid}")
        print(f"Patient Name: {details['name']}")
        print(f"Disease: {details['disease']}")


def search_patient():
    try:
        pid = int(input("Enter patient ID to search: "))
    except ValueError:
        print("Please enter a valid numeric patient ID.")
        return

    if pid in patients:
        print("Patient found.")
        print(f"Patient ID: {pid}")
        print(f"Patient Name: {patients[pid]['name']}")
        print(f"Disease: {patients[pid]['disease']}")
    else:
        print("Patient not found.")


def delete_patient():
    try:
        pid = int(input("Enter patient ID to delete: "))
    except ValueError:
        print("Please enter a valid numeric patient ID.")
        return

    if pid in patients:
        del patients[pid]
        print("Patient deleted successfully.")
    else:
        print("Patient ID not found.")


while True:
    print("\\n1. Add patient")
    print("2. View patients")
    print("3. Search patient")
    print("4. Delete patient")
    print("5. Exit")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a number from 1 to 5.")
        continue

    if choice == 1:
        add_patient()
    elif choice == 2:
        view_patient()
    elif choice == 3:
        search_patient()
    elif choice == 4:
        delete_patient()
    elif choice == 5:
        print("Thank you!")
        break
    else:
        print("Invalid choice. Please enter 1 to 5.")
