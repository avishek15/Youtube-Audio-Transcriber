from fastapi import FastAPI, HTTPException
from yt_audio_downloader.api import router as yt_audio_router
import os

app = FastAPI()

# Include the routers
app.include_router(yt_audio_router, prefix="/yt-audio")

# Endpoint to delete all .wav files


@app.delete("/delete-all-wavs", summary="Delete all .wav files")
async def delete_all_wavs():
    try:
        # Assuming the .wav files are in a specific directory
        wav_directory = "."
        for filename in os.listdir(wav_directory):
            if filename.endswith(".wav"):
                file_path = os.path.join(wav_directory, filename)
                os.remove(file_path)
        return {"message": "All .wav files deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# To run the FastAPI app, use the command: uvicorn main:app --reload
