# sql.py
# Script for interacting with a PostgreSQL database.
# A. Shortridge, 3/2009, 10/2014

import psycopg2

##########################################
## Establish a connection to a database. 
## Using PostgreSQL I would normally connect to it with:
## psql -d dbname_here 
## and then I would be asked for my password. 

dbc = psycopg2.connect(database="michigan",  user="ashton", password="blah")

# Create a cursor to the database from dbc
cursor = dbc.cursor()

#############################################
## Run standard SQL statements using the cursor ##
## to return entire tables at once.             ##

# A select query run on cane
cursor.execute("SELECT * FROM cane")
result = cursor.fetchall()

# result is a table representation as a list of tuples.
# One decent way to print it to screen is via a loop:
for rec in result:
    for field in rec:
        print field,
    print

# A fancier select query run on cane
cursor.execute("SELECT * from cane where year > 1996 order by year")
result = cursor.fetchall()
# Print it:
for rec in result:
    for field in rec:
        print field,
    print


# What if the query isn't valid SQL?
cursor.execute("... we shall them fight in the hills; we shall never surrender")
# Yuck. Try/Exception handling could be a good idea here.

cursor.close()
dbc.close() # Sometimes it's best to re-establish the con
dbc = psycopg2.connect(database="michigan",  user="ashton", password="blah")
cursor = dbc.cursor()

##################################################
## Run standard SQL statements using the cursor ##
## but return each record in sequence, 1 by 1.  ##

# max is the maximum wind speed of the hurricane, in knots.
cursor.execute("SELECT * FROM cane WHERE max > 112.9")   # Wind speed > 130 mph

# get the number of rows in the selection set
numrows = int(cursor.rowcount)

for row in range(0, numrows):
    record = cursor.fetchone()   # grabs the next record
    print 'record', row + 1, ':',
    for field in record:
        print field,
    print

############################################
## A few other SQL syntax things for "fun"

query = "select distinct name, count(name) from cane group by name order by name"
cursor.execute(query) # Be sure query is yours, not user or, worse, web input. That is insecure.
result = cursor.fetchall()
for rec in result:
    for field in rec:
        print field,
    print

# The following uses a subquery! And it converts knots to mph!
query = "SELECT name, year, max*1.15078 FROM cane WHERE max = (SELECT max(max) FROM cane)"
cursor.execute(query) # Be wary of this approach!
result = cursor.fetchall()
for rec in result:
    for field in rec:
        print field,
    print

cursor.close()
dbc.close() 