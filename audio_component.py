# extract_audio.py
import ffmpeg
import sys

def extract_audio(video_file, audio_output_file):
    stream = ffmpeg.input(video_file)
    stream = ffmpeg.output(stream, audio_output_file, **{'q:a': 0, 'vn': None})
    ffmpeg.run(stream)
    print(f"Audio extracted to {audio_output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_audio.py <input_video.mp4> <output_audio.wav>")
        sys.exit(1)

    video_file = sys.argv[1]
    audio_output_file = sys.argv[2]
    
    extract_audio(video_file, audio_output_file)