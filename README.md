# YouTube Audio Transcriber

**Download + Transcribe YouTube Videos with Whisper**

[![Build Status](https://github.com/avishek15/Youtube-Audio-Transcriber/actions/workflows/main.yml/badge.svg)](https://github.com/avishek15/Youtube-Audio-Transcriber/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/avishek15/Youtube-Audio-Transcriber.svg)](https://github.com/avishek15/Youtube-Audio-Transcriber/stargazers)

![Demo](docs/demo.gif)

## What It Does

Download audio from YouTube videos and transcribe using OpenAI's Whisper model:
- **Audio extraction** — Download audio from any YouTube video
- **AI transcription** — Whisper-powered speech-to-text
- **Multiple models** — tiny, base, small, medium, large
- **GPU acceleration** — CUDA-enabled for faster processing
- **Web UI** — Streamlit interface for easy use

## Why It Matters

Transcribing YouTube videos manually:
- Takes 5-10x video length
- Requires expensive services ($1/minute)
- No control over accuracy

This tool:
- Costs $0 (runs locally)
- Takes ~0.5x video length (with GPU)
- You control the model size

## Quick Start

```bash
# Clone
git clone https://github.com/avishek15/Youtube-Audio-Transcriber.git
cd Youtube-Audio-Transcriber

# Install
pip install -r requirements.txt

# Install ffmpeg (required)
# macOS: brew install ffmpeg
# Linux: sudo apt-get install ffmpeg
# Windows: choco install ffmpeg

# Run Web UI
streamlit run app.py
```

Web UI runs at `http://localhost:8501`

## Features

### Audio Download
- Extract audio from YouTube videos
- Automatic format conversion
- No quality loss

### Whisper Transcription
- Multiple model sizes (tiny → large)
- 99+ languages supported
- Timestamp support
- GPU acceleration

### Web Interface
- Paste YouTube URL → get transcript
- Progress indicators
- Download transcript as TXT

### API Mode
- FastAPI backend
- REST API for automation
- Batch processing

## Usage

### Web UI (Streamlit)

1. Run `streamlit run app.py`
2. Paste YouTube URL
3. Select model size
4. Click "Transcribe"
5. Download transcript

### Command Line

```bash
python main.py --url "https://youtube.com/watch?v=..." --model small
```

**Arguments:**
- `--url` — YouTube video URL
- `--model` — Whisper model (tiny, base, small, medium, large)
- `--output` — Output file path (optional)

### API (FastAPI)

```bash
# Start API server
python driver.py

# Transcribe via API
curl -X POST http://localhost:8000/transcribe \
  -H "Content-Type: application/json" \
  -d '{"url": "https://youtube.com/watch?v=...", "model": "small"}'
```

**Response:**
```json
{
  "transcript": "Hello and welcome to...",
  "language": "en",
  "duration_seconds": 342,
  "model": "small"
}
```

## Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | Streamlit |
| **Backend** | FastAPI |
| **Audio Download** | yt-dlp |
| **Transcription** | OpenAI Whisper |
| **Audio Processing** | ffmpeg |

## Model Comparison

| Model | VRAM | Speed | Accuracy |
|-------|------|-------|----------|
| tiny | ~1GB | Fastest | Good |
| base | ~1GB | Fast | Better |
| small | ~2GB | Medium | Great |
| medium | ~5GB | Slow | Excellent |
| large | ~10GB | Slowest | Best |

*Recommendation: Use `small` for most cases. Use `large` for accuracy-critical work.*

## Performance

| Video Length | Model | Processing Time (CPU) | Processing Time (GPU) |
|--------------|-------|----------------------|----------------------|
| 5 minutes | small | ~3 minutes | ~45 seconds |
| 30 minutes | small | ~15 minutes | ~4 minutes |
| 60 minutes | small | ~30 minutes | ~8 minutes |

*Benchmarks on Intel i7 (CPU) vs RTX 3080 (GPU)*

## Deployment

### Docker

```bash
docker build -t yt-transcriber .
docker run -p 8501:8501 -p 8000:8000 yt-transcriber
```

### Cloud Deployment

Deploy to any cloud with GPU support:
- AWS EC2 (g4dn instances)
- Google Cloud (with GPU)
- RunPod / Lambda Labs

## Use Cases

### 1. Content Repurposing
Transcribe YouTube videos → turn into blog posts

### 2. Research
Transcribe lectures/interviews → analyze content

### 3. Accessibility
Add transcripts to videos for deaf/hard-of-hearing

### 4. SEO
Generate text from video content → improve search ranking

### 5. Note-Taking
Transcribe meetings/webinars → searchable notes

## API Endpoints

### POST `/transcribe`

Transcribe a YouTube video

```bash
curl -X POST http://localhost:8000/transcribe \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://youtube.com/watch?v=...",
    "model": "small"
  }'
```

### GET `/health`

Health check

```bash
curl http://localhost:8000/health
```

## Project Structure

```
Youtube-Audio-Transcriber/
├── app.py                  # Streamlit UI
├── driver.py               # FastAPI server
├── main.py                 # CLI entry point
├── yt_audio_downloader/    # Audio download logic
│   ├── __init__.py
│   └── downloader.py
├── requirements.txt
└── README.md
```

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md)

### Development Setup

```bash
pip install -r requirements.txt
pip install pytest pytest-asyncio
pytest
```

## License

MIT License - see [LICENSE](LICENSE)

## Author

Built by **Avishek Majumder**

- 🌐 [invaritech.ai](https://invaritech.ai)
- 🐦 [@AviMajumder1503](https://x.com/AviMajumder1503)
- 💼 [LinkedIn](https://linkedin.com/in/avishek-majumder)
- 🐙 [GitHub](https://github.com/avishek15)

---

**Star ⭐ this repo if you find it useful!**
