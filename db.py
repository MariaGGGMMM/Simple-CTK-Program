import sqlite3

connection = sqlite3.connect('hellokittye.db', check_same_thread = False)

cursor = connection.cursor() # наша рука для роботы

query = '''

CREATE TABLE IF NOT EXISTS Cats(
    Id INTEGER AUTO_INCREMENT  PRIMARY KEY,
     Website TEXT,
     Email TEXT,
     password TEXT

)

'''

cursor.execute(query)



