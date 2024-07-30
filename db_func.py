def insert(cursor, email, website, password):
    query = '''

INSERT INTO Cats (Email, Website, Pssword) VALUES (?, ?, ?)

'''

    cursor.execute(query, (email, website, password))

def get_all_users(cursor):
    query ='''
    SELECT * FROM Users
    '''

    cursor.execute(query)
    