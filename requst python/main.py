import yt_dlp


def download_video(url, output_path='downloads'):
    """
    Download a video from a supported platform using yt-dlp.

    Parameters:
    url (str): URL of the video to download
    output_path (str): Directory to save the downloaded video

    Returns:
    str: Path to downloaded file
    """
    # Configure yt-dlp options
    ydl_opts = {
        'format': 'best',  # Download best quality
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Output template
        'nocheckcertificate': True,
        'noplaylist': True,  # Download single video, not playlist
    }

    try:
        # Create a yt-dlp object with our options
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract video information
            info = ydl.extract_info(url, download=False)
            filename = ydl.prepare_filename(info)

            # Download the video
            ydl.download([url])

            print(f"Successfully downloaded: {filename}")
            return filename

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


# Example usage
if __name__ == "__main__":
    # Example for downloading from a supported platform
    video_url = "s"  # Replace with actual URL
    downloaded_file = download_video(video_url)