import pyodbc

try:
    connection = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"
        "DATABASE=EmployeeETL;"
        "Trusted_Connection=yes;"
    )

    print("Connected successfully!")

    connection.close()

except pyodbc.Error as e:
    print("Connection failed:", e)
