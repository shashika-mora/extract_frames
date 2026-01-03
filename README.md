# Video Frame Extractor

![Python](https://img.shields.io/badge/python-3.x-blue?style=flat-square&logo=python&logoColor=white) ![OpenCV](https://img.shields.io/badge/opencv-python-green?style=flat-square&logo=opencv&logoColor=white)

Turns your video into a mountain of images. Perfect for when you need to analyze every pixel or just want to catch that specific millisecond where things went wrong.

## Overview
A simple script that reads `video.mp4` and dumps every single frame as a `.jpg`. No complex UI, just raw frame extraction power. Useful for creating datasets or analyzing videos frame-by-frame.

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
