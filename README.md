# MP4 to MP3 Converter

**made by ravejsreal**
[GitHub Repository](https://github.com/ravejsreal/mp4-to-mp3-converter)

Simple tool to extract audio from MP4 videos and save as MP3 files.

## Installation

```bash
pip install -r requirements.txt
```

## How to Use

Just run the script and follow the prompts:

```bash
python mp4_to_mp3.py
```

Paste in your MP4 file path and it extracts the audio. Converted MP3 files go into an "output" folder.

## What It Does

The converter actually extracts the audio stream from the video file and encodes it as MP3. It's not just renaming files, it properly processes the audio data.

File sizes are usually much smaller since you're only keeping the audio track. A 100MB video might become a 3-5MB MP3 file.

## Example

When you run it you'll get something like:

```
============================================================
                 MP4 TO MP3 CONVERTER
                   made by ravejsreal
       github.com/ravejsreal/mp4-to-mp3-converter
============================================================

Convert MP4 video to MP3 audio

Enter MP4 file path (or 'q' to quit):
```

Drop in your MP4 path and it converts it. Shows you the video duration and file sizes when it's done.
