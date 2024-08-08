import subprocess

def extract_audio(video_path: str, audio_path: str) -> None:
    command = f"ffmpeg -i {video_path} -q:a 0 -map a {audio_path} -y"
    subprocess.run(command, shell=True, check=True)