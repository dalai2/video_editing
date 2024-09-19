# Video Noise Cancellation and Audio Replacement

This project provides Python scripts to extract audio from an MP4 video, apply noise cancellation to the audio, and replace the original video audio with the noise-canceled version.

## Features
- **Audio Extraction**: Extract audio from an MP4 video using `ffmpeg`.
- **Noise Cancellation**: Reduce noise from extracted audio using the `noisereduce` library.
- **Audio Replacement**: Replace the original audio in the MP4 video with the noise-canceled audio.

## Requirements

Before running the scripts, make sure to install the required libraries:

1. Install `ffmpeg`:
   - **Windows**: Download and install from [FFmpeg.org](https://ffmpeg.org/download.html) and add to your system's PATH.
   - **Linux/Mac**: Install using a package manager like `apt` (Linux) or `brew` (Mac).

2. Install required Python libraries:
```bash
pip install noisereduce numpy scipy
