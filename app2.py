import os
from flask import Flask, render_template, request, jsonify
import numpy as np
import random
import joblib  # For loading pre-trained machine learning models (if any)
import tensorflow as tf  # For deep learning models
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Load a pre-trained model (for example, a stress prediction model)
# Assuming you have a model saved as 'stress_model.pkl' or 'stress_model.h5'
try:
    model = joblib.load('stress_model.pkl')  # Use joblib for traditional ML models
except FileNotFoundError:
    model = None  # In case the model doesn't exist

# Placeholder function for meditation audio selection (could integrate with a database)
def get_meditation_audio():
    audio_files = ["calm_audio_1.mp3", "calm_audio_2.mp3", "calm_audio_3.mp3"]
    return random.choice(audio_files)

# Home route to render the index page
@app.route('/')
def home():
    return render_template('index.html')

# Route for stress level prediction (input through a simple form or API)
@app.route('/predict', methods=['POST'])
def predict_stress():
    if model:
        try:
            # Example: Input features could be heart rate, mood, etc.
            heart_rate = float(request.form['heart_rate'])
            mood = float(request.form['mood'])  # A mood scale from 1-10

            # Example input for the model (you'd scale or process it depending on your model)
            features = np.array([[heart_rate, mood]])

            # Predict stress level using the model
            prediction = model.predict(features)
            return jsonify({"stress_level": prediction[0]})
        except Exception as e:
            return jsonify({"error": str(e)})
    else:
        return jsonify({"error": "Model not loaded or found!"})

# Route for meditation session (provides a meditation audio link)
@app.route('/meditate', methods=['GET'])
def meditate():
    audio_file = get_meditation_audio()
    return render_template('meditate.html', audio_file=audio_file)

# Route for tracking user progress (save the user's meditation sessions, etc.)
@app.route('/track', methods=['POST'])
def track_progress():
    try:
        # Get data from form or request
        user_id = request.form['user_id']
        session_duration = int(request.form['session_duration'])  # Minutes spent meditating
        session_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Here, we could save this data to a database or file (For demo, we just print it)
        print(f"User {user_id} meditated for {session_duration} minutes on {session_date}")

        # Returning success response
        return jsonify({"status": "success", "message": "Meditation session saved!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# Route for getting daily tips or quotes for mindfulness
@app.route('/tip', methods=['GET'])
def get_mindfulness_tip():
    tips = [
        "Breathe deeply and focus on the present moment.",
        "Take a few moments to stretch and release tension.",
        "Start your day with gratitude and calmness.",
        "Mindfulness is a practice. Be patient with yourself.",
        "Focus on your breathing to reduce stress."
    ]
    return jsonify({"tip": random.choice(tips)})

# Main entry point for the Flask application
if __name__ == '__main__':
    app.run(debug=True)
