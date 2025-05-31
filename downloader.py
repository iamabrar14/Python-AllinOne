import yt_dlp

url = 'https://www.youtube.com/watch?v=8JW6qzPCkE8&list=RD8JW6qzPCkE8&start_radio=1'

with yt_dlp.YoutubeDL() as ydl:
    info = ydl.extract_info(url, download=False)
    for f in info['formats']:
        print(f"{f['format_id']}: {f['ext']} - {f['format_note']} - {f['resolution']}")
