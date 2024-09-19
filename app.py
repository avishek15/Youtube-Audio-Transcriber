import streamlit as st
import requests
import subprocess
import os

# Function to download and process audio


def download_and_process_audio(youtube_url):
    # Replace with your FastAPI server URL
    base_url = "http://127.0.0.1:8000"

    # Send a DELETE request to the endpoint to delete old wav files
    response = requests.delete(f"{base_url}/delete-all-wavs")

    # Send a POST request to download audio from the specified YouTube URL
    response = requests.post(
        f"{base_url}/yt-audio/download-audio", json={"url": youtube_url, "output_path": "."})
    filename = response.json()["filename"]

    # Define the command to run whisper with the desired options
    command = [
        "whisper",  # The whisper command
        "--output_format", "txt",  # Format of the output file (txt)
        f"{filename}",
    ]

    st.write(f"RUNNING: {' '.join(command)}")

    # Execute the command using subprocess.Popen
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Read and print the output and error messages in real-time
    output_lines = []
    error_lines = []
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            output_lines.append(output.strip())
            st.write(output.strip())

    # Capture any remaining output and error messages
    stdout, stderr = process.communicate()
    if stdout:
        output_lines.extend(stdout.splitlines())
    if stderr:
        error_lines.extend(stderr.splitlines())
        st.error("\n".join(error_lines))

    # Check the return code of the process
    return_code = process.poll()
    if return_code == 0:
        st.success("Command executed successfully.")

        # Save the output to a file
        output_filename = f"{'.'.join(filename.split('.')[:-1])}.txt"
        # with open(output_filename, "w") as f:
        #     f.write("\n".join(output_lines))

        # Provide a download link for the output file
        with open(output_filename, "r") as f:
            st.download_button(
                label="Download Output File",
                data=f,
                file_name=output_filename,
                mime="text/plain"
            )

        # Clean up the output file
        os.remove(output_filename)
    else:
        st.error(f"Command failed with return code {return_code}.")


# Streamlit UI
st.title("YouTube Audio Downloader and Whisper Processor")

# Input for YouTube URL
youtube_url = st.text_input("Enter YouTube URL")

# Button to trigger the download and processing
if st.button("Download and Process"):
    if youtube_url:
        download_and_process_audio(youtube_url)
    else:
        st.error("Please enter a valid YouTube URL.")
