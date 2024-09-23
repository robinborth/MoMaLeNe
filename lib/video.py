import os
from pathlib import Path
import subprocess


def create_video(video_dir: str, video_path: str, framerate: int = 30) -> None:
    Path(video_path).parent.mkdir(exist_ok=True, parents=True)
    args: list[str] = [
        f"ffmpeg -framerate {framerate}",
        f'-pattern_type glob -i "{Path(video_dir) / "*.png"}"',
        f"-c:v libx264 -pix_fmt yuv420p {video_path}",
        "-y",
    ]
    subprocess.run(
        " ".join(args),
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
