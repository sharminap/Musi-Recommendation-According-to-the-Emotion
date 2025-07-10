import spotipy
from spotipy.oauth2 import SpotifyOAuth

def create_playlist(emotion):
    mood_map = {
        "happy": "pop",
        "sad": "acoustic",
        "angry": "rock",
        "disgust": "metal",
        "surprise": "dance",
        "fear": "ambient",
        "neutral": "chill"
    }

    genre = mood_map.get(emotion, "chill")

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        redirect_uri="http://localhost:8080",
        scope="playlist-modify-public"
    ))

    user_id = sp.me()['id']
    results = sp.search(q=f'genre:{genre}', type='track', limit=10)
    track_ids = [track['id'] for track in results['tracks']['items']]

    playlist = sp.user_playlist_create(user=user_id, name=f"{emotion.capitalize()} Mood Playlist", public=True)
    sp.playlist_add_items(playlist_id=playlist['id'], items=track_ids)

    print(f"🎧 Playlist created: {playlist['external_urls']['spotify']}")