from app.dao.dao import connect_database
from app.schemas.feed import Feed
from mysql.connector import Error

def CreateFeed(feed: Feed):

    try:
        connection, cursor = connect_database()

        query = f""" INSERT INTO sca_db.feed(
        text,
        overview,
        positive,
        negative,
        neutral,
        date,
        user_id)
        VALUES (
        "{feed.text}",
        "{feed.overview}",
        "{feed.positive}",
        "{feed.negative}",
        "{feed.neutral}",
        NOW(),
        1);
        """

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return feed
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def GetFeedByUserId(user_id: int):

    try:
        connection, cursor = connect_database()

        query = f""" SELECT * FROM sca_db.feed WHERE user_id = {user_id};"""

        cursor.execute(query)
        item = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return item
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def GetFeedByUserId(user_id: int):

    try:
        connection, cursor = connect_database()

        query = f""" SELECT * FROM sca_db.feed WHERE user_id = {user_id};"""

        cursor.execute(query)
        item = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return item
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def GetFeedByRate(column: str, item: str):

    try:
        connection, cursor = connect_database()

        query = f""" SELECT * FROM sca_db.feed WHERE {column} = "{item}";"""

        cursor.execute(query)
        item = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return item
    
    except Error as erro:
        return {"Error: {}".format(erro)}
    
def GetAllFeed():

    try:
        connection, cursor = connect_database()

        query = f""" SELECT * FROM sca_db.feed;"""

        cursor.execute(query)
        item = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return item
    
    except Error as erro:
        return {"Error: {}".format(erro)}

if __name__ == '__main__':
    CreateFeed()