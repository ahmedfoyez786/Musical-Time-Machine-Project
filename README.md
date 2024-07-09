# Musical Time Machine Project

This project allows users to travel back in time to a specific date and create a Spotify playlist with the top 100 songs from the Billboard Hot 100 chart for that date.

## Features

- Scrape Billboard Hot 100 songs for a specific date using BeautifulSoup.
- Search and retrieve song URIs from Spotify using the Spotipy API.
- Create a private Spotify playlist with the top 100 songs from the specified date.

## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`
- `spotipy`

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/ahmedfoyez786/Musical-Time-Machine-Project.git
   cd Musical-Time-Machine-Project
   ```

2. Install the required libraries:

   ```sh
   pip install requests beautifulsoup4 spotipy
   ```

3. Set up your Spotify developer credentials:

   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
   - Create a new application.
   - Add `http://localhost` as a Redirect URI in the application settings.
   - Note down your `Client ID` and `Client Secret`.

4. Update the `CLIENT_ID` and `CLIENT_SECRET` in the script:
   ```python
   CLIENT_ID = "your_spotify_client_id"
   CLIENT_SECRET = "your_spotify_client_secret"
   ```

## Usage

1. Run the script:

   ```sh
   python musical_time_machine.py
   ```

2. Enter the date you want to travel to in the format `YYYY-MM-DD` when prompted.

3. The script will:
   - Scrape the Billboard Hot 100 chart for the specified date.
   - Search for the songs on Spotify.
   - Create a private playlist on your Spotify account with the top 100 songs.
   - Print the link to the created playlist.

## Example

```sh
Which year do you want to travel to? Type the date in this format YYYY-MM-DD: 1995-12-25
```
