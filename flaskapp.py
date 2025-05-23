from flask import Flask, render_template, request
from moviepy import VideoFileClip
import os
import uuid
from transformers import pipeline
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# accent prediction
def predict_accent(audio_path):
    classifier = pipeline("audio-classification", model="ylacombe/accent-classifier")
    result = classifier(audio_path)
    best_match = result[0]
    confidence_score = best_match['score']
    accent = best_match['label']

    return accent, confidence_score

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith(('.mp4', '.mov', '.avi')):
            filename = f"{uuid.uuid4()}.mp4"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Extract audio
            video = VideoFileClip(filepath)
            audio_path = filepath.replace('.mp4', '.wav')
            video.audio.write_audiofile(audio_path, logger=None)

            # Predict accent
            accent, confidence = predict_accent(audio_path)

            # Delete the original video file
            try:
                os.remove(filepath)
                os.remove(audio_path)
            except Exception:
                pass

            return render_template('upload.html', videoname=filename, accent=accent, confidence=confidence)

    return render_template('upload.html')

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
