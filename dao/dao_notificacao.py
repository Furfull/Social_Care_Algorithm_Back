from app.dao.dao import connect_database
from app.schemas.notificacao import Notification
from mysql.connector import Error
import random 

lista = [
    "Estamos aqui para ajudar!",
    "Você não está sozinho(a)",
    "Sua força é inspiradora, e estamos aqui para apoiá-lo(a)",
    "Conte conosco",
    "Não se culpe por sentir-se assim",
    "Não tenha medo de pedir ajuda"
    ]

call = "Caso precise clique em Ajuda!"

def CreateNotification(notification: Notification):

    try:
        connection, cursor = connect_database()

        query = f""" INSERT INTO sca_db.notification(
        date,
        text,
        user_id)
        VALUES (NOW(),
        "Vimos seu post: \n {notification.text} \n {random.sample(lista, 1)[0]} \n {call}",
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
    
def CreateNotificationLoc(notification: Notification):

    try:
        connection, cursor = connect_database()

        query = f""" INSERT INTO sca_db.notification(
        date,
        text,
        user_id)
        VALUES (NOW(),
        "Vimos seu post: \n {notification.text} \n para sua segurança, recomendamos que não compartilhe sua localização em tempo real, \n conte com a SCA sempre!",
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
