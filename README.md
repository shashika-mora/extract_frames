# Video Frame Extractor

A lightweight Python utility for extracting individual frames from video files.

## Overview
This tool automates the process of decomposing a video file into its constituent frames. It reads a source video (`video.mp4`) and saves each frame as a separate JPEG image in the local directory.

## Prerequisites
- **Python 3.x**
- **OpenCV** (`opencv-python`)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd extract_frames
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare the Video**
   - Place your target video file in the project root.
   - Rename the file to `video.mp4` (or update line 3 in `main.py`).

2. **Run the Script**
   ```bash
   python main.py
   ```

3. **Output**
   - Frames will be generated as `frame_0.jpg`, `frame_1.jpg`, etc. in the same directory.

## Project Structure
- `main.py`: Core logic for video processing and frame extraction.
- `requirements.txt`: Project dependencies.

---
*Created by AMST DAYARATHNA*
