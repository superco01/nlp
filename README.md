# Audio Sentiment Analysis

This project records audio from your microphone, transcribes it to text, and analyzes the sentiment of the transcribed text using a pre-trained sentiment analysis model from the Hugging Face Transformers library.

## Features

- Record audio for a specified duration.
- Transcribe recorded audio to text using Google Speech Recognition.
- Analyze sentiment of the transcribed text (positive/negative) using a sentiment analysis model.

## Requirements

- Python 3.9 or higher
- `pyaudio` for audio recording
- `speech_recognition` for transcribing audio
- `transformers` for sentiment analysis

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/superco01/nlp.git
   cd nlp
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   conda create -n nlp-env python=3.9
   conda activate nlp-env
   ```

3. Install the required packages:

   ```bash
   pip install pyaudio speechrecognition transformers
   ```

## Usage

1. Run the script:

   ```bash
   python main.py
   ```

2. The script will record audio for 5 seconds (you can modify this in the code), transcribe it to text, and print the sentiment analysis result.

## Code Explanation

- **record_audio(filename, duration)**: Records audio from the microphone and saves it to a specified file.
- **transcribe_audio(filename)**: Uses the SpeechRecognition library to convert audio to text.
- **main()**: The main function that coordinates audio recording, transcription, and sentiment analysis.

## Contributing

Feel free to submit issues or pull requests if you'd like to contribute!

## License

This project is licensed under the MIT License.
