def insert(cursor, Name, Surname, DateOfBirth):
    query = '''

INSERT INTO Cats (Name, Surname, DateOfBirth) VALUES (?, ?, ?)


'''

    cursor.execute(query, (Name, Surname, DateOfBirth))

def get_all_users(cursor):
    query ='''
    SELECT * FROM Cats
    '''

    cursor.execute(query)