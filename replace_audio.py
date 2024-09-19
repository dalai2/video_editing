import subprocess
import sys

def replace_audio_in_video(input_video, input_audio, output_video):
    # Use FFmpeg to replace the audio in the video
    command = [
        'ffmpeg',
        '-i', input_video,     # Input video file
        '-i', input_audio,      # Input audio file
        '-c:v', 'copy',         # Copy the video without re-encoding
        '-c:a', 'aac',          # Re-encode audio using AAC codec
        '-strict', 'experimental',  # Allow experimental aac encoder
        '-map', '0:v:0',        # Select the video from the first input
        '-map', '1:a:0',        # Select the audio from the second input
        output_video            # Output file with new audio
    ]

    try:
        # Run the FFmpeg command
        subprocess.run(command, check=True)
        print(f"Audio replaced successfully. Output video: {output_video}")
    except subprocess.CalledProcessError as e:
        print(f"Error during audio replacement: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python replace_audio.py <input_video.mp4> <input_audio.wav> <output_video.mp4>")
        sys.exit(1)

    input_video = sys.argv[1]
    input_audio = sys.argv[2]
    output_video = sys.argv[3]

    replace_audio_in_video(input_video, input_audio, output_video)
