import pyaudio
import wave
import speech_recognition as sr
from transformers import pipeline


def record_audio(filename, duration=5):
    """Record audio from the microphone."""
    chunk = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = 44100

    audio = pyaudio.PyAudio()
    stream = audio.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)

    print("Recording...")
    frames = []

    for _ in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Recording finished.")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))


def transcribe_audio(filename):
    """Transcribe audio to text using SpeechRecognition."""
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError:
            return "Could not request results from Google Speech Recognition service"


def main():
    # Record audio
    audio_filename = "output.wav"
    record_audio(audio_filename)

    # Transcribe audio to text
    transcribed_text = transcribe_audio(audio_filename)
    print("Transcribed Text:", transcribed_text)

    # Load sentiment analysis pipeline
    classifier = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english",
        device="mps"
    )

    # Analyze sentiment
    sentiment_result = classifier(transcribed_text)[0]
    print("Sentiment Analysis Result:", sentiment_result)


if __name__ == "__main__":
    main()
