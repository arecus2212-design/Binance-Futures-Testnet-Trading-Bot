import subprocess
import numpy as np
from faster_whisper import WhisperModel

YOUTUBE_URL = "https://www.youtube.com/watch?v=bQaCD4d1Jm0"

CHUNK_DURATION = 5
SAMPLE_RATE = 16000

print("Loading Whisper model...")
model = WhisperModel("base", device="cpu", compute_type="int8")

print("Starting stream...")

command = [
    "yt-dlp",
    "--js-runtimes", "node",
    "-f", "bestaudio/best",
    "-o", "-",
    YOUTUBE_URL
]

yt_process = subprocess.Popen(command, stdout=subprocess.PIPE)

ffmpeg_command = [
    "ffmpeg",
    "-i", "pipe:0",
    "-f", "s16le",
    "-acodec", "pcm_s16le",
    "-ac", "1",
    "-ar", str(SAMPLE_RATE),
    "-"
]

ffmpeg_process = subprocess.Popen(
    ffmpeg_command,
    stdin=yt_process.stdout,
    stdout=subprocess.PIPE,
    stderr=subprocess.DEVNULL
)

chunk_size = SAMPLE_RATE * CHUNK_DURATION * 2

while True:
    raw_audio = ffmpeg_process.stdout.read(chunk_size)

    if not raw_audio:
        break

    audio = np.frombuffer(raw_audio, np.int16).astype(np.float32) / 32768.0

    segments, _ = model.transcribe(audio)

    for segment in segments:
        print(segment.text)