````markdown
# YouTube Audio Downloader and Transcriber

## Introduction

This project allows you to download the audio from a YouTube video and transcribe it using the `whisper` model. The transcription process is a cold start, long-running process that uses the `small` model by default unless specified otherwise. The project is designed to be run in a virtual environment and leverages FastAPI for the backend and Streamlit for the frontend.

## Features

- **Audio Download**: Downloads the audio from a specified YouTube video.
- **Transcription**: Transcribes the downloaded audio using the `whisper` model.
- **Model Selection**: Uses the `small` model by default, but can be configured to use other models.
- **Hardware Acceleration**: Supports hardware-accelerated PyTorch for faster processing.

## Prerequisites

- Python 3.7 or higher
- A compatible CUDA-enabled GPU (optional, for hardware acceleration)
- `ffmpeg` for handling multimedia conversions

### Installing `ffmpeg`

- **Windows**:

  ```bash
  choco install ffmpeg
  ```
````

- **Mac**:

  ```bash
  brew install ffmpeg
  ```

- **Linux (Ubuntu/Debian)**:

  ```bash
  sudo apt-get install ffmpeg
  ```

- **Linux (Fedora)**:

  ```bash
  sudo dnf install ffmpeg
  ```

- **Linux (CentOS)**:

  ```bash
  sudo yum install ffmpeg
  ```

## Steps to Run the Project

### 1. Create a Virtual Environment

Create a virtual environment to manage dependencies:

```bash
python3 -m venv .venv
```

### 2. Activate the Virtual Environment

Activate the virtual environment:

- **Windows**:

  ```bash
  .venv\Scripts\activate
  ```

- **Unix/Mac/Linux**:

  ```bash
  source .venv/bin/activate
  ```

### 3. Install Required Libraries

Install the required Python libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Install Hardware-Accelerated PyTorch (Optional)

If you have a CUDA-enabled GPU and want to leverage hardware acceleration, uninstall the default PyTorch installation and install the hardware-accelerated version:

```bash
pip uninstall torch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### 5. Run the FastAPI Server

Start the FastAPI server to handle backend operations:

```bash
uvicorn main:app
```

### 6. Run the Streamlit Server

Start the Streamlit server to provide the frontend interface:

```bash
streamlit run app.py
```

### 7. Navigate to the Streamlit Interface

Open your web browser and navigate to the Streamlit interface (usually at `http://localhost:8501`). Enter a YouTube link and download the transcribed text.

## Usage

1. **Enter YouTube URL**: In the Streamlit interface, enter the URL of the YouTube video you want to transcribe.
2. **Download and Process**: Click the "Download and Process" button to start the download and transcription process.
3. **Download Transcription**: Once the process is complete, a download link will appear. Click the link to download the transcribed text file.

## Troubleshooting

- **Whisper Model Loading**: If you encounter issues with the `whisper` model loading, ensure that the `whisper` package is correctly installed and that the model files are accessible.
- **Hardware Acceleration**: If you experience slow performance, ensure that your GPU is correctly recognized and that the hardware-accelerated PyTorch is installed.
- **ffmpeg Installation**: If you encounter issues with multimedia conversions, ensure that `ffmpeg` is correctly installed and accessible from your system's PATH.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- [Whisper](https://github.com/openai/whisper) - OpenAI's automatic speech recognition system.
- [FastAPI](https://fastapi.tiangolo.com/) - A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- [Streamlit](https://streamlit.io/) - The fastest way to build and share data apps.
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - A fork of youtube-dl with additional features and fixes.
- [ffmpeg](https://ffmpeg.org/) - A powerful multimedia framework for handling audio and video processing.

Feel free to contribute to this project by submitting issues or pull requests. Happy transcribing!

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any problems or have suggestions for improvements.

## Contact

For any questions or feedback, please reach out to the maintainers of this project.
