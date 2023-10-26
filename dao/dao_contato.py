from app.dao.dao import connect_database
from app.schemas.contato import Contact, ContactShow
from mysql.connector import Error

def Createcontact(contact: Contact):

    try:
        connection, cursor = connect_database()

        query = f""" INSERT INTO sca_db.contact(
        name,
        number,
        user_id)
        VALUES ("{contact.name}",
        "{contact.number}",
        "{contact.user_id}");
        """

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return contact
    
    except Error as erro:
        return {"Error: {}".format(erro)}


def ShowContact(id: int) -> ContactShow:

    try:
        connection, cursor = connect_database()

        query = f""" SELECT id, name, number FROM sca_db.contact WHERE user_id = {id};"""

        cursor.execute(query)

        item = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return item
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def DeleteContact(id: int) -> int:

    try:
        connection, cursor = connect_database()

        query = f""" DELETE FROM sca_db.contact WHERE user_id = {id};"""

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return id
    
    except Error as erro:
        return {"Error: {}".format(erro)}