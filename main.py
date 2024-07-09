from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
CLIENT_ID = "8a62f3b959464d288c6863fbd54cc9bf"
CLIENT_SECRET = "ae5404ebd68e40b79a0a6ec42ec53a06"

input_date = input("Which year do you want to travel to? Type the date in this formate YYYY-MM-DD:")
url = f"https://www.billboard.com/charts/hot-100/{input_date}"
response = requests.get(url)
html_data = response.text

soup = BeautifulSoup(html_data, "html.parser")
song_tags = soup.select("li ul li h3")
top_100_song = [song.getText().strip() for song in song_tags]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
year = input_date.split("-")[0]
song_uris = []
for song in top_100_song:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user=user_id, name=f"{input_date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(playlist["external_urls"])
