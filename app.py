import pandas as pd
import mysql.connector
from datetime import datetime


# Define date_obj before using it
date_obj = datetime(2025, 3, 12)  # Example date

# Now you can convert to string
date_str = date_obj.strftime('%Y-%m-%d')

# Create connection to MySQL database
conn = mysql.connector.connect(
 host="localhost",
 user="root",
 password="SeDlIc75NA!",
 database="demo"
)
cursor = conn.cursor()

# Excel-Datei einlesen
#excel_data = pd.read_excel("anwesenheit.xlsx")
#excel_data['Datum'] = pd.to_datetime(excel_data['Datum']).dt.strftime('%Y-%m-%d')

# Überprüfen, wie die Excel-Daten aussehen
#print(excel_data.head())

# Iteration durch die Zeilen der Excel-Datei 
#for index, row in excel_data.iterrows():
 #student_id = row['Student_ID']
 #datum = row['Datum']
 #status = row['Status']
 
 # Datum in Tabelle 'Tage' einfügen, falls es nicht existiert
 #cursor.execute("SELECT Tag_ID FROM Tage WHERE Datum = %s", (datum,))
 #tag_id = cursor.fetchone()
 #if tag_id is None:
  #cursor.execute("INSERT INTO Tage (Datum) VALUES (%s)", (datum,))
  #conn.commit()
  #cursor.execute("SELECT Tag_ID FROM Tage WHERE Datum = %s", (datum,))
  #tag_id = cursor.fetchone()


# SQL query to insert data into MySQL database
sql = "INSERT INTO anwesenheit (Student_ID, Tag_ID, Status) VALUES (%s, %s, %s)"
values = [
    (7,5,"anwesend"),
    (8,5,"präsenz"),
    (9,5,"anwesend"),
]
# Ensure the date is passed as a tuple with the datetime object
#cursor.execute(sql, (date_str,))  # Tuple notation for one parameter

#insert multiple rows at once
cursor.executemany(sql, values) 

# Commit changes to the database
conn.commit()

# Close connection
#cursor.close()
#conn.close()

print(f"{cursor.rowcount} Datensätze wurden erfolgreich in die Datenbank geschrieben.")


