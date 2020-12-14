# playlist_scrapper

Simple script I created with purpose of retrieving tracks aired on the internet radio - Radio Luz. It writes each song to new line to a file. For now I use it by simply running it when I hear something worth remembering and coming back to it - saving to playlist or buying it via bandcamp.

## Dependencies:
- **Selenium** needs to be installed first:
> pip install selenium
- Respective driver for a web browser is also needed; here I use **GeckoDriver** for **Firefox**. Put it in your PATH environmental variable so it can be accessed from anywhere:
>https://github.com/mozilla/geckodriver/releases

## Usage:
To run the script simply **cd** to the location of it and if you're on windows:
> python .\app.py
New Firefox window will appear and disappear after the script is done saving tracks. That's it!

## Plans for the future:
- (done) upgrade to omit already saved songs
- upgrade to run in a loop until terminated
- adding other internet radio stations
- optimize to scrape faster
- optimize to open driver browser silently or in background
