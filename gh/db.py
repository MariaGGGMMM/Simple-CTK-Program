import sqlite3

connection = sqlite3.connect('hellokittye.db')

cursor = connection.cursor() 

query = '''

CREATE TABLE IF NOT EXISTS Cats(
    Id INTEGER AUTO_INCREMENT  PRIMARY KEY,
     Name TEXT,
     Surname TEXT,
      DateOfBirth INTEGER

)

'''

cursor.execute(query)



