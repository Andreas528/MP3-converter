# MP3 Converter

A simple Python CLI tool that downloads audio from supported URLs and converts it to MP3 using **yt-dlp** and **FFmpeg**.

## Features

- Download and convert audio to MP3.
- Choose audio quality (128, 192, 256 or 320 kbps).
- Display download progress.
- Save converted files in a dedicated output folder.
- Skip previously downloaded videos.
- Convert multiple URLs in one session.
- Handle common errors.

## Requirements

- Python 3.12+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg](https://ffmpeg.org/)

## Installation

Install yt-dlp:

```bash
python -m pip install yt-dlp
```

Install FFmpeg:

**Ubuntu / WSL:**

```bash
sudo apt update
sudo apt install ffmpeg
```

**Windows:**

Download FFmpeg from the [official website](https://ffmpeg.org/download.html) and make sure it's available in your PATH.

**macOS (using Homebrew):**

```bash
brew install ffmpeg
```


## Usage

Run the program:

```bash
python main.py
```

Choose your preferred audio quality, enter a URL, and follow the prompts.

Converted MP3 files are saved in the `generated_mp3s` folder.

Previously downloaded videos are tracked in `downloaded.txt` to prevent downloading them again.

## Disclaimer

Only download content you own or are authorised to download. Respect copyright laws and the terms of the source platform.