#!/usr/bin/python3
#
# import a table to postgreSQL
#

import psycopg2
import csv

# Database connection
try:
    conn = psycopg2.connect("dbname=test user=postgres host=localhost password=postgres")
    print('Database Connection ... OK')
except:
    print ("Database Connection ... FAILED, please check database connection details")

# Cursor to perform DB operations
cursor=conn.cursor()

# Drop old tables if exists
cursor.execute("DROP TABLE mit_ir")
cursor.execute("DROP TABLE mit_zigbee")

# create tables
cursor.execute("CREATE TABLE IF NOT EXISTS MIT_IR(sender_id integer,local_id integer,data_time timestamp);")
cursor.execute("CREATE TABLE IF NOT EXISTS MIT_Zigbee(sender_id integer,local_id integer,rssi integer,data_time timestamp);")
print('CREATE TABLES ... SUCCESS')

# Read the IR CSV file
with open('IR.csv') as csvfile:
    columnreader = csv.reader(csvfile, delimiter=',', quotechar="|")
    for row in columnreader:
        cursor.execute("INSERT INTO mit_ir (sender_id,local_id,data_time) VALUES("+row[0]+", "+row[1]+", '"+row[2]+"');")
# Read the Zigbee CSV file
with open('Zigbee.csv') as csvfile2:
    columnreader2 = csv.reader(csvfile2, delimiter=',', quotechar="|")
    for row2 in columnreader2:
        cursor.execute("INSERT INTO mit_zigbee (sender_id,local_id,rssi,data_time) VALUES("+row2[0]+", "+row2[1]+", "+row2[2]+", '"+row2[3]+"');")
print ('FILL THE TABLES ... SUCCESS')

print ('Analyze queries before indexation')
# Analyze Queries before indexation
cursor.execute("EXPLAIN (ANALYZE TRUE) SELECT * FROM mit_zigbee WHERE rssi<15 AND rssi>3")
rows=cursor.fetchall()
for row in rows:
    print (row[0])

# Create index
cursor.execute("CREATE INDEX rssi_index ON mit_zigbee (rssi);")
print ('Indexing RSSI column ... SUCCESS')
# Analyze queries after indexation
cursor.execute("EXPLAIN (ANALYZE TRUE) SELECT * FROM mit_zigbee WHERE rssi<15 AND rssi>3")
rows = cursor.fetchall()
for row in rows:
    print(row[0])

# Persiste changes
conn.commit()

# Close communications
cursor.close()
conn.close()
