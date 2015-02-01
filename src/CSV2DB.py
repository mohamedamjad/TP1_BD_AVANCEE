#!/usr/bin/python3
#
# import a table to postgreSQL
#
from bson import BSON
from bson import json_util
import os
import psycopg2
import csv
from pymongo import MongoClient
from subprocess import call

# Database connection
try:
    conn = psycopg2.connect("dbname=mit user=mit15 host=localhost password=mit15")
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
with open('../data/IR.csv') as csvfile:
    columnreader = csv.reader(csvfile, delimiter=',', quotechar="|")
    for row in columnreader:
        cursor.execute("INSERT INTO mit_ir (sender_id,local_id,data_time) VALUES("+row[0]+", "+row[1]+", '"+row[2]+"');")
# Read the Zigbee CSV file
with open('../data/Zigbee.csv') as csvfile2:
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

# Insert CSV files into MongoDB server
call(["mongoimport", "-d", "mit15", "-c", "IR", "--type", "csv", "--file", "../data/IR_h.csv", "--headerline"])
call(["mongoimport", "-d", "mit15", "-c", "Zigbee", "--type", "csv", "--file", "../data/Zigbee_h.csv", "--headerline"])
print('Importing CSV files into MongoDB ... SUCCESS !')

# Initialize MongoDB Client
mongoClient = MongoClient('localhost',27017)
print('MongoDB Client initilization ... SUCCESS !')

# Initialize DataBase
db = mongoClient.mit15
 # Get the collection
IR_collection = db.IR
Zigbee_collection = db.Zigbee

# first request
doc = db.IR_collection.find({})
print(json_util.dumps(doc, sort_keys=True, indent=4, default=json_util.default))
