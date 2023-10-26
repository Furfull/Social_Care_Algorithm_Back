from .sentimental_analysis import sample_analyze_sentiment
from .facebook_gather import FacebookApi
from app.dao.dao_feed import CreateFeed
from app.schemas.feed import Feed


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
        except Exception as e:
            raise e

    return "OK"
