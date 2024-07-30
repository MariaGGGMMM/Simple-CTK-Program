def insert(cursor, email, website, password):
    query = '''
    INSERT INTO Cats (Username, Website, Password) VALUES (?,?,?)
    
    '''
    cursor.execute(query, (email, website, password))



def get_all_users(cursor):
    
    query = '''
    SELECT * FROM Cats
    '''
    cursor.execute(query)