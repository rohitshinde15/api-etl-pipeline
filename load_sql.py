import json
import pyodbc

# Read cleaned JSON
with open("clean_list.json", "r") as f:
    clean_list = json.load(f)

# Connect to SQL Server
connection = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=EmployeeETL;"
    "Trusted_Connection=yes;"
)

cursor = connection.cursor()
cursor.execute(
    "SELECT COUNT(*) FROM Employees WHERE id = ?",
    6
)



result = cursor.fetchone()[0]

if result == 1:
    print("ID already exists")
else:
    print("ID does not exist")
#inserting data
for employee in clean_list:

    cursor.execute(
        "SELECT COUNT(*) FROM Employees WHERE id = ?",
        employee["id"]
    )

    result = cursor.fetchone()[0]

    if result == 1:
        print(f"ID {employee['id']} already exists - skipping")
        continue

    cursor.execute(
        """
        INSERT INTO Employees
        (id, First_Name, Last_name, Age, gender, email)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        employee["id"],
        employee["First_Name"],
        employee["Last_name"],
        employee["Age"],
        employee["gender"],
        employee["email"]
    )

    print(f"ID {employee['id']} inserted")
connection.commit()
cursor.close()
connection.close()