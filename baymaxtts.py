import os
import time
import edge_tts
import asyncio
from playsound import playsound  # ✅ Import playsound module

MAX_FILES = 1  # Limit saved audio files

async def text_to_speech(text):
    """Converts text to speech and plays it."""
    try:
        timestamp = int(time.time())
        output_file = f"Baymax_voice_{timestamp}.mp3"

        print(f"Generating speech...")

        # Generate speech
        tts = edge_tts.Communicate(
            text=text,
            voice="en-US-GuyNeural",
            rate="-10%",
            pitch="+15Hz"
        )
        await tts.save(output_file)
        print(f"Speech saved: {output_file}")

        # ✅ Play the generated MP3 file
        playsound(output_file)  # ✅ Fix: This now plays the audio

        # Cleanup old files
        files = sorted(
            [f for f in os.listdir() if f.endswith('.mp3')],
            key=os.path.getctime
        )
        if len(files) > MAX_FILES:
            for file in files[:-MAX_FILES]:
                try:
                    os.remove(file)
                    print(f"Deleted old file: {file}")
                except (PermissionError, OSError) as e:
                    print(f"Could not delete {file}: {e}")

    except Exception as e:
        print(f"Error generating speech: {e}")
