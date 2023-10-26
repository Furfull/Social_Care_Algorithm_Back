from app.dao.dao import connect_database
from app.schemas.notificacao import Notification
from mysql.connector import Error

def CreateNotification(notification: Notification):

    try:
        connection, cursor = connect_database()

        query = f""" INSERT INTO sca_db.notification(
        date,
        text,
        user_id)
        VALUES (NOW(),
        "{notification.text}",
        "{notification.user_id}");
        """

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return notification
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def Getnotification(user_id: int):

    try:
        connection, cursor = connect_database()

        query = f""" SELECT * FROM sca_db.notification WHERE user_id = {user_id} LIMIT 10;"""

        cursor.execute(query)
        item = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return item
    
    except Error as erro:
        return {"Error: {}".format(erro)}
