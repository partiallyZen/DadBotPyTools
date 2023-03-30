import csv
import sqlite3

# open the CSV file
with open('mydata.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)  # get the headers

    # connect to the database and create the table
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE mytable ({0})'.format(', '.join(headers)))

    # insert the data into the table
    for row in reader:
        cursor.execute('INSERT INTO mytable ({0}) VALUES ({1})'.format(', '.join(headers), ', '.join(['?' for _ in range(len(headers))])),
                       row))

    # commit the changes and close the connection
    conn.commit()
    conn.close()
