# follow followers source code
import logging
import time
import os
import tweepy

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def create_api():
    CONSUMER_KEY = environ['CONSUMER_KEY']
    CONSUMER_SECRET_KEY = environ['CONSUMER_SECRET_KEY']
    ACCESS_TOKEN = environ['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = environ['ACCESS_TOKEN_SECRET']


    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
 

def follow_followers(api):
    logger.info("getting + following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Now following {follower.name}")
            follower.follow()


def main():
    api = create_api()
    while True:
        follow_followers(api)
        logger.info("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()
