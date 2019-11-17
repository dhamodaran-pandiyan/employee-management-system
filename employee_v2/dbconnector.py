import sqlite3
conn = sqlite3.connect('employees.db')
print ("Opened database successfully")
conn.execute("INSERT INTO employee(name,id) VALUES ('aa',12 )");
conn.execute("INSERT INTO employee(name,id) VALUES ('bb',13 )");
conn.execute("INSERT INTO employee(name,id) VALUES ('cc',14 )");
conn.commit()
print ("Records created successfully")
conn.close()