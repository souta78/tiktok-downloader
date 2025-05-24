"""
TikTok Downloader - Video & Audio
Simple TikTok downloader using yt-dlp for downloading videos without watermark and audio
Author: Souta
"""

import os
import sys
import yt_dlp
from pathlib import Path

class TikTokDownloader:
    def __init__(self):
        self.download_path = self.get_downloads_folder()
        
    def get_downloads_folder(self):
        """Get the default Downloads folder for the current OS"""
        home = Path.home()
        
        downloads_win = home / "Downloads"
        if downloads_win.exists():
            return downloads_win
            
        downloads_paths = [
            home / "Downloads",
            home / "Download",
            home / "downloads",
            home / "Desktop"  
        ]
        
        for path in downloads_paths:
            if path.exists():
                return path
                
        downloads_default = home / "Downloads"
        downloads_default.mkdir(exist_ok=True)
        return downloads_default
    
    def download_video(self, url):
        """Download TikTok video without watermark"""
        ydl_opts = {
            'format': 'best[ext=mp4]',
            'outtmpl': str(self.download_path / 'Souta_%(title)s.%(ext)s'),
            'writeinfojson': False,
            'writesubtitles': False,
            'extractor_args': {
                'tiktok': {
                    'webpage_url_basename': 'video'
                }
            }
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                print("Downloading TikTok video without watermark...")
                ydl.download([url])
                print("Video download completed successfully!")
                return True
            except Exception as e:
                print(f"Error: {str(e)}")
                return False
    


def main():
    print("TikTok Downloader - Video & Audio")
    print("Author: Souta")
    print("=" * 40)
    
    downloader = TikTokDownloader()
    print(f"Download location: {downloader.download_path}")
    
    while True:
        print("\nMenu:")
        print("1. Download Video (No Watermark)")
        print("2. Exit")
        
        choice = input("\nChoose option (1-2): ").strip()
        
        if choice == '2':
            print("Thank you for using TikTok Downloader!")
            break
        
        if choice not in ['1']:
            print("Invalid choice!")
            continue
        
        url = input("\nEnter TikTok URL: ").strip()
        if not url:
            print("URL cannot be empty!")
            continue
        
        if 'tiktok.com' not in url and 'vm.tiktok.com' not in url:
            print("URL must be from TikTok!")
            continue
        
        if choice == '1':
            downloader.download_video(url)

if __name__ == "__main__":
    try:
        import yt_dlp
    except ImportError:
        print("Library yt-dlp is not installed!")
        print("Install with: pip install yt-dlp")
        sys.exit(1)
    
    print("Note: This downloader gets TikTok videos without watermark")
    print("No FFmpeg required for video download\n")
    
    main()
