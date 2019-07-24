import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

client_id = "afa255abe5eb4ebfbd9e644935fe8d4d"
client_secret = "1e66c142891f4f019358aca795ba7fa5"
redirect_uri = "http://localhost:8888/callback"

username = '12142627285'

client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

scope = 'user-library-read playlist-read-private'
try:
    token = util.prompt_for_user_token(
        username,
        scope,
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri
    )

    sp = spotipy.Spotify(auth=token)
    print('deu certo')
except:
    print('Token nao deu certo ' + username)


def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None


def show_recommendations_for_artist(artist):
    results = sp.recommendations(seed_artists=[artist['id']])
    for track in results['tracks']:
        resultado1 = track['name']
        resultado2 = " - "
        resultado3 = track['artists'][0]['name']
        resultado4 = " "
        resultado5 = track['external_urls']['spotify']
        resultadoFinal = resultado1 + resultado2 + resultado3 + resultado4 + resultado5
        str(resultadoFinal)
        print(resultadoFinal)
        return resultadoFinal
