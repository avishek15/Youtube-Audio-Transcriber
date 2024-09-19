import requests
import subprocess

# Example driver code to test the endpoints
if __name__ == "__main__":

    # Replace with your FastAPI server URL
    base_url = "http://127.0.0.1:8000"

    # Test downloading audio from YouTube
    youtube_url = "https://www.youtube.com/watch?v=XiXLti_Y_is"
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

    print(f"RUNNING: {' '.join(command)}")

    # Execute the command using subprocess.Popen
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Read and print the output and error messages in real-time
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())

    # Capture any remaining output and error messages
    stdout, stderr = process.communicate()
    if stdout:
        print("Remaining Standard Output:")
        print(stdout)
    if stderr:
        print("Remaining Standard Error:")
        print(stderr)

    # Check the return code of the process
    return_code = process.poll()
    if return_code == 0:
        print("Command executed successfully.")
    else:
        print(f"Command failed with return code {return_code}.")
