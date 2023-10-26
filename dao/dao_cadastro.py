from app.dao.dao import connect_database
from app.schemas.cadastro import User, UserLogin
from mysql.connector import Error

def CreateUser(user: User):

    try:
        connection, cursor = connect_database()

        query = f"""INSERT INTO sca_db.user(
        name,
        password,
        email,
        born_date,
        user)
        VALUES ("{user.name}",
        "{user.password}",
        "{user.email}",
        "{user.born_date}",
        "{user.user}");
        """

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return user
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def LoginUser(user: str, password: str):

    try:
        connection, cursor = connect_database()

        query = f"""SELECT count(*) FROM sca_db.user WHERE user = "{user}"
        AND password = "{password}";"""

        cursor.execute(query)
        item = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return item
    
    except Error as erro:
        return {"Error: {}".format(erro)}
