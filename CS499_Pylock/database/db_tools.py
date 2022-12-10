
def create_db(cursor):

    create = "CREATE DATABASE if not exists pylock;"
    cursor.execute(create)


def drop_db(cursor):

    drop = "DROP DATABASE if exists pylock;"
    cursor.execute(drop)


def create_table(cursor):

    cursor.execute("USE pylock")

    table = "CREATE TABLE passwords ( " \
            "service  VARCHAR(16) NOT NULL," \
            "username VARCHAR(32) NOT NULL," \
            "password VARCHAR(64) NOT NULL)"

    cursor.execute(table)
    return


def insert_data(cursor, db, service, username, password):

    cursor.execute("USE pylock")

    sql = "INSERT INTO passwords (service, username, password) VALUES (%s, %s, %s)"
    val = (service, username, password)

    cursor.execute(sql, val)
    db.commit()



def select_data(cursor, service, username):

    cursor.execute("USE pylock")

    # selecting query
    query = f"SELECT password FROM passwords WHERE service = '{service}' and username = '{username}'"
    cursor.execute(query)

    result = cursor.fetchall()

    for x in result:
        print(x)


def update_data(cursor, db, service, username, password):

    cursor.execute("USE pylock")

    # selecting query
    query = f"UPDATE passwords SET password = '{password}' WHERE service = '{service}' and username = '{username}'"
    cursor.execute(query)
    db.commit()


def delete_data(cursor, db, service, username):

    cursor.execute("USE pylock")

    # selecting query
    query = f"DELETE FROM passwords WHERE service = '{service}' and username = '{username}'"
    cursor.execute(query)
    db.commit()

