from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import yt_dlp
import os
import time
import uuid

router = APIRouter()


class AudioDownloadRequest(BaseModel):
    url: str
    output_path: str = '.'  # Default output path


@router.post("/download-audio")
async def download_audio(audio_request: AudioDownloadRequest):
    # Generate a unique UUID for the file name
    unique_id = str(uuid.uuid4())
    # unique_filename = f"{unique_id}.wav"

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'postprocessor_args': [
            '-ar', '16000'
        ],
        'prefer_ffmpeg': True,
        'keepvideo': False,
        # Custom file name template,
        'outtmpl': f'{audio_request.output_path}/{unique_id}.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(audio_request.url, download=True)
            # Change the output file name after download
            file_path = f"{audio_request.output_path}/{unique_id}.wav"

            # Wait for the file to be fully written
            time.sleep(1)

            # Check if the file exists before renaming
            if os.path.exists(file_path):
                return {"message": f"Downloaded and converted audio from {audio_request.url}",
                        "filename": file_path}
            else:
                raise HTTPException(
                    status_code=400, detail="File not found after download")

    except yt_dlp.utils.DownloadError as e:
        raise HTTPException(status_code=400, detail=f"Download error: {e}")
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {e}")


# To run the FastAPI app, use the command: uvicorn <filename>:app --reload
