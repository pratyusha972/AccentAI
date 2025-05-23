# AccentAI

AccentAI is a web application that identifies regional accents by analyzing audio extracted from uploaded videos. 
It’s designed to assist customer-facing services by routing users to conversational agents best suited to their accent.

What It Does
- Accepts video files in .mp4, .mov, or .avi format.
- Extracts audio from the video.
- Uses a deep learning model to predict the speaker’s accent.
- Displays the predicted accent along with a confidence score.

Tech Stack
- Backend: Flask (Python 3.12)
- Frontend: HTML
- Model: Deep learning-based accent prediction
- Audio Processing: Extracts audio from video using moviepy.

Getting Started
- Prerequisites: Python 3.12

Installation
- Clone the repository: git clone https://github.com/yourusername/accentAI.git; cd accentAI
- Install the required libraries: pip install -r requirements.txt
- Run the Flask application: python flaskapp.py
- Open your browser and go to http://localhost:5000

File Structure
- flaskapp.py – Main Flask application.
- templates/index.html – HTML template.
- requirements.txt – List of required Python packages.

Cleanup
- Uploaded video files are automatically deleted after audio extraction to save storage space.
