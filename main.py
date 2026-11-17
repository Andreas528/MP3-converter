import subprocess
import os

def choose_quality():
    quality_options = {
        "1": "128",
        "2": "192",
        "3": "256",
        "4": "320"
    }

    while True:
        print("Choose audio quality:")
        print("1. 128 kbps")
        print("2. 192 kbps")
        print("3. 256 kbps")
        print("4. 320 kbps")

        quality = input("Your choice: ")
        bitrate = quality_options.get(quality)

        if bitrate is None:
            print("Invalid quality selection.")
            continue

        return bitrate

def get_url():
    while True:
        url = input("Enter the URL to convert: ")

        if not url:
            print("No URL provided. Try again")
            continue

        return url
    
def convert_to_mp3(url, bitrate, output_folder):
    try:
        subprocess.run([
            "yt-dlp",
            "-f", "bestaudio",
            "--newline",
            "-x",
            "--download-archive", "downloaded.txt",
            "--no-overwrites",
            "--audio-format", "mp3",
            "--audio-quality", f"{bitrate}K",
            "-o", os.path.join(output_folder, "%(title)s.%(ext)s"),
            url
        ], check=True)


        print(f"URL Received: {url}")

        print("Conversion completed successfully!")
        
    except subprocess.CalledProcessError:
        print("Something went wrong during the download or conversion.")
   
    except FileNotFoundError:
        print("yt-dlp could not be found. Check that it is installed and available in PATH.")

def main():
    output_folder = "generated_mp3s"
    os.makedirs(output_folder, exist_ok=True)

    bitrate = choose_quality()

    while True:
        url = get_url()
        convert_to_mp3(url, bitrate, output_folder)

        while True:
            response = input(
                "Convert another URL? (y/n): "
            ).strip().lower()

            if response == "y":
                break
            elif response == "n":
                print("Exiting program.")
                return
            else:
                print("Please enter y or n.")

if __name__ == "__main__":
    main()