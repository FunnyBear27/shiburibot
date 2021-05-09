import mysql.connector


def add(obj):
    print(str(obj['NoteDate']))
    config = {
        'user': 'root',
        'password': 'root',
        'host': '127.0.0.1',
        'port': 8889,
        'database': 'shiburibot',
        'raise_on_warnings': True
    }

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=True)
    a = cursor.execute("INSERT INTO notifies (NoteDate, NoteText, UserId) VALUES (%(NoteDate)s, %(NoteText)s, "
                       "%(UserId)s)", obj)
    cnx.commit()
    cnx.close()
