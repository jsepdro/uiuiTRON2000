import logging
import time

import tweepy

from consulta import voltaArtista
from spotifyConnect import get_artist
from spotifyConnect import show_recommendations_for_artist
from twitterconfig import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

sexta_feira = "B A L A D E I R O \n" \
              "X A V E Q U E I R O \n" \
              "C A C H A Ç E I R O \n" \
              "P I R I G U E T E I R O \n" \
              "U A T I Z A P \n" \
              "S E M P R E    C O N G E S T I O N A D O"

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
            if tweet.text == "@uiuiTRON2000 musi":
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
                reply_status = "@%s %s" % (
                username_to_reply, "o @qqfoize nao gosta de hentai, nao acredite em quem fala o contrario")
                uiui.update_status(
                    status=reply_status,
                    in_reply_to_status_id=tweet.id,
                )
            if tweet.text == "@uiuiTRON2000 sexta feira":
                username_to_reply = tweet.user.screen_name
                logger.info(f"Respondendo para {tweet.user.screen_name}")
                reply_status = "@%s %s" % (username_to_reply,sexta_feira)
                uiui.update_with_media(
                    filename="SRC/sexta.gif",
                    status=reply_status,
                    in_reply_to_status_id=tweet.id,
                )
    return new_since_id


def main():
    since_id = 1
    while True:
        print(since_id)
        since_id = check_mentions(uiui, ["musica", "talarico", "sexta feira", "hentai"], since_id)
        time.sleep(20)


if __name__ == "__main__":
    main()
