import yt_dlp
import os
import sys

def download_playlist():
    # === Ask for playlist URL ===
    playlist_url = input("🎵 Enter YouTube Playlist URL: ").strip()

    # === Set ffmpeg path ===
    ffmpeg_path = r"C:\Users\Acer\Documents\Python Code\Youtube Audio Downloader\ffmpeg\bin"

    # === Set output folder ===
    download_folder = r"C:\Users\Acer\Documents\Python Code\Youtube Audio Downloader\Music3"
    os.makedirs(download_folder, exist_ok=True)

    # === yt-dlp options ===
    ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
    'noplaylist': False,
    'quiet': False,
    'ignoreerrors': True,  # 👈 This lets it skip videos with errors
    # 'writeinfojson': True,  # Optional: keep metadata JSONs
    'ffmpeg_location': ffmpeg_path,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

    # === Run the downloader ===
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        print("\n✅ All audio files downloaded and converted to MP3!")
        return True

    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False

# === Main loop ===
while True:
    success = download_playlist()

    if not success:
        choice = input("\n❓ Do you want to try a different playlist? (yes/no): ").strip().lower()
        if choice == 'yes':
            print("👋 Exiting. Goodbye!")
            continue
    else:
        break
