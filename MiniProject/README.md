==================Patient Management System Using Python – Project Details======================
1. Project Overview
Project Name: Patient Management System
Programming Language: Python
Project Type: Console-Based Application
Domain: Healthcare Management
Level: Beginner Python Project
The Patient Management System is a Python-based application designed to manage basic patient information. It allows users to add, view, search, and delete patient records through a simple menu-driven interface. The project uses a Python dictionary to store patient details temporarily and functions to perform different operations.
2. Project Objectives
- To maintain patient records in an organized manner.
- To add patient information using a unique patient ID.
- To view all available patient records.
- To search for a particular patient by ID.
- To delete patient records when required.
- To understand Python programming concepts through a practical project.
3. Project Modules

Module 1: Add Patient
The user enters the patient ID, name, and disease. The system checks whether the patient ID already exists. If it does not exist, the patient record is added to the dictionary.




Module 2: View Patients
Displays all registered patients, including their ID, name, and disease. If there are no patient records, the system displays a message indicating that no patients are available.




Module 3: Search Patient
Accepts a patient ID from the user and checks whether that ID exists in the dictionary. If found, it displays the patient's details; otherwise, it displays a not-found message.




Module 4: Delete Patient
Takes a patient ID as input and removes the corresponding record using Python's del statement if the ID exists.




Module 5: Menu and Exit
Displays the menu repeatedly using a while loop. The user selects an operation, and the program executes the corresponding function. Selecting Exit terminates the program.



4. Technologies and Concepts Used
Technology / Concept	Purpose
Python	Main programming language
Dictionary	Stores patient records as key-value pairs
Functions	Separates each operation into a reusable block
if-elif-else	Checks conditions and user choices
while loop	Repeats the menu until the user exits
for loop	Iterates through all patient records
return	Exits a function when needed
del	Deletes a patient record
input()	Accepts information from the user
print()	Displays output and messages
5. Data Structure Used
Your project uses a nested dictionary.
Example:
Patient = {    101: {        "name": "Rahul",        "disease": "Fever"    },    102: {        "name": "Priya",        "disease": "Cold"    }}



Here:
- 101 and 102 are patient IDs.
- "name" stores the patient's name.
- "disease" stores the disease information.
- The patient ID acts as the dictionary key, helping the program find records efficiently.
6. Project Workflow
1. Start the Python program.
2. Display the menu with five options.
3. Accept the user's choice.
4. Call the corresponding function.
5. Perform the selected operation.
6. Return to the menu.
7. Exit when the user selects option 5.
7. Sample Output
1. Add Patient
2. View Patient
3. Search Patient
4. Delete Patient
5. Exit

Enter choice: 1
Enter pid: 101
Enter Patient name: Rahul
Enter disease: Fever
Patient added successfully


Searching for the same patient:
Enter choice: 3
Enter patient id to search: 101

Patient id is found
Patient id: 101
Patient name: Rahul
Disease: Fever


8. Advantages
- Simple and easy to use.
- Avoids duplicate patient IDs.
- Supports basic patient record management.
- Uses separate functions for better code organization.
- Helps beginners understand CRUD operations.
CRUD stands for Create, Read, Update, and Delete. Your current project implements Create, Read, and Delete, while searching is an additional retrieval operation. The Update operation can be added as a future enhancement.
9. Limitations
- Patient records are lost when the program closes.
- No database or permanent file storage is used.
- The program does not currently support updating patient details.
- Input validation is limited.
- There is no login system or access control.
10. Future Enhancements
- Integrate SQLite or MySQL for permanent data storage.
- Add an Update Patient Details feature.
- Add a Tkinter graphical interface.
- Validate patient ID and other user inputs.
- Implement login and access control to protect medical information.
- Add further fields such as age, contact number, and appointment date, with appropriate privacy safeguards.
11. Conclusion
The Patient Management System is a beginner-level Python project that demonstrates how patient records can be managed through a menu-driven application. It provides practical experience with dictionaries, functions, loops, conditional statements, and basic record operations. The project can be extended into a more complete application by integrating a database and additional features.