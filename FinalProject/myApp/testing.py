import os
from pydub import AudioSegment
import speech_recognition as sr

def mp3_to_wav(mp3_file_path, wav_file_path):
    """
    Convert an MP3 file to WAV format.

    Parameters:
    mp3_file_path (str): Path to the input MP3 file.
    wav_file_path (str): Path to the output WAV file.
    """
    audio = AudioSegment.from_mp3(mp3_file_path)
    audio.export(wav_file_path, format="wav")

def speech_to_text(wav_file_path):
    """
    Convert speech in a WAV file to text using Google's Speech Recognition API.

    Parameters:
    wav_file_path (str): Path to the WAV file.

    Returns:
    str: The transcribed text.
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file_path) as source:
        audio_data = source.record()
        text = recognizer.recognize_google(audio_data)
    return text

def mp3_to_text(mp3_file_path):
    """
    Convert an MP3 file to text by first converting it to WAV and then transcribing it.

    Parameters:
    mp3_file_path (str): Path to the input MP3 file.

    Returns:
    str: The transcribed text.
    """
    wav_file_path = "temp.wav"
    mp3_to_wav(mp3_file_path, wav_file_path)
    text = speech_to_text(wav_file_path)
    os.remove(wav_file_path)  # Clean up temporary file
    return text

# Example usage:
mp3_file_path = "D://test.mp3"
text = mp3_to_text(mp3_file_path)
print(text)
