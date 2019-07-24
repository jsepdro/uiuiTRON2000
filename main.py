import logging
import time

import tweepy

from spotifyConnect import get_artist
from spotifyConnect import show_recommendations_for_artist
from twitterconfig import create_api
from consulta import voltaArtista

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

uiui = create_api()


def check_mentions(api, keywords, since_id):
    logger.info("Esperando pelos tweets...")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
                               since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Tweet localizado do @{tweet.user.screen_name}")
            if tweet.text == "@uiuiTRON2000 debug":
                artista = voltaArtista()
                artist = get_artist(artista)
                if artist:
                    musica = show_recommendations_for_artist(artist)
                else:
                    print(artista, " nao localizado")
                username_to_reply = tweet.user.screen_name
                logger.info(f"Respondendo para {tweet.user.screen_name}")
                reply_status = "@%s %s" % (username_to_reply, musica)
                uiui.update_status(
                    status=reply_status,
                    in_reply_to_status_id=tweet.id,
                )
            if tweet.text == "@uiuiTRON2000 talarico":
                username_to_reply = tweet.user.screen_name
                logger.info(f"Respondendo para {tweet.user.screen_name}")
                reply_status = "@%s" % (username_to_reply)
                uiui.update_with_media(
                    filename="SRC/talarico.jpeg",
                    status=reply_status,
                    in_reply_to_status_id=tweet.id,
                )
            if tweet.text == "@uiuiTRON2000 hentai":
                username_to_reply = tweet.user.screen_name
                logger.info(f"Respondendo para {tweet.user.screen_name}")
                reply_status = "@%s %s" % (username_to_reply, "o @qqfoize nao gosta de hentai, nao acredite em quem fala o contrario")
                uiui.update_status(
                    status=reply_status,
                    in_reply_to_status_id=tweet.id,
                )
    return new_since_id

def main():
    since_id = 1
    while True:
        print(since_id)
        since_id = check_mentions(uiui, ["debug","talarico","zap", "hentai"], since_id)
        time.sleep(20)


if __name__ == "__main__":
    main()
