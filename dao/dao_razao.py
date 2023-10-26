from app.dao.dao import connect_database
from app.schemas.razao import Reason
from mysql.connector import Error

def CreateReason(reason: Reason):

    try:
        connection, cursor = connect_database()

        query = f""" INSERT INTO sca_db.reason(
        date,
        text,
        user_id)
        VALUES (NOW(),
        "{reason.text}",
        "{reason.user_id}");
        """

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return reason
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def Getreason(user_id: int):

    try:
        connection, cursor = connect_database()

        query = f""" SELECT * FROM sca_db.reason WHERE user_id = {user_id} LIMIT 10;"""

        cursor.execute(query)
        item = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return item
    
    except Error as erro:
        return {"Error: {}".format(erro)}
