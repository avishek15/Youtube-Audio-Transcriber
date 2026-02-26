# YouTube Audio Transcriber

**Extract transcripts from YouTube videos using Whisper AI.**

![Demo](demo.gif)

## What It Does

Paste a YouTube URL, get a full transcript. Uses OpenAI's Whisper for accurate transcription.

**Why it matters:** Manual transcription takes hours. This does it in minutes.

## Quick Start

\`\`\`bash
# Clone
git clone https://github.com/avishek15/Youtube-Audio-Transcriber.git
cd Youtube-Audio-Transcriber

# Install
pip install -r requirements.txt

# Run
python transcriber.py --url "https://youtube.com/watch?v=..."
\`\`\`

## Features

- **High accuracy** — Whisper AI transcription
- **Timestamps** — Know when each word was spoken
- **Multi-language** — Supports 100+ languages
- **Export options** — TXT, SRT, JSON

## Tech Stack

- **Python 3.10+**
- **OpenAI Whisper** — Transcription
- **yt-dlp** — Audio extraction
- **FastAPI** — Optional API server

## Use Cases

| Use Case | How It Helps |
|----------|--------------|
| **Content repurposing** | Turn videos into blog posts |
| **Accessibility** | Add captions to videos |
| **Research** | Search through video content |
| **Note-taking** | Extract key points from talks |

## Demo

Live demo: [tools.invaritech.ai/transcriber](https://tools.invaritech.ai/transcriber)

## Roadmap

- [ ] AI summarization
- [ ] Speaker diarization
- [ ] Batch processing
- [ ] Web UI

## License

MIT License - see [LICENSE](LICENSE)

## Author

Built by [Avishek Majumder](https://invaritech.ai)

---

**Part of [Invaritech](https://invaritech.ai)** — AI automation tools.
