from .sentimental_analysis import sample_analyze_sentiment
from .facebook_gather import FacebookApi
from .send_sms import send
from app.dao.dao_feed import CreateFeed
from app.schemas.feed import Feed
from app.schemas.notificacao import Notification
from app.dao.dao_notificacao import CreateNotification, CreateNotificationLoc

def persist_data():

    face = FacebookApi()
    checkText: str = face.checkText
    checkLoc: str = face.checkLocation

    if checkText != None:
        analysed_text: dict = sample_analyze_sentiment(checkText)

        feed = Feed(text=analysed_text["text"],
                    overview=analysed_text["overview"],
                    positive=analysed_text["positive"],
                    negative=analysed_text["negative"],
                    neutral=analysed_text["neutral"])

        try:
            CreateFeed(feed)
            if analysed_text["overview"] == "negative":
                noti = Notification(text=analysed_text["text"],
                    user_id=1)
                CreateNotification(noti)
                send()
        except Exception as e:
            raise e

    if "está em" in checkLoc:
        feedLoc = Feed(text=checkLoc[27:],
                       overview="location",
                       positive="null",
                       negative="null",
                       neutral="null")
        try:
            CreateFeed(feedLoc)
            noti = Notification(text=analysed_text["text"],
                    user_id=1)
            CreateNotificationLoc(noti)
        except Exception as e:
            raise e



    return "OK"
