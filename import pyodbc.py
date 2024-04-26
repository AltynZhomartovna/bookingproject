import pyodbc

# Establish connection to the SQL Server database
connection_to_db = pyodbc.connect(r'Driver={SQL Server}; Server=WIN-CS1FA1MBJO0; database=Shop; Trusted_Connection=yes;')
cursor = connection_to_db.cursor()

# Execute SQL query
cursor.execute("select * from Salespeople WHERE city = 'London'")  # Corrected the quotes

# Fetch the first row
row = cursor.fetchone()
rest_of_rows = cursor.fetchall()
print(row)

# Close the database connection
connection_to_db.close()
