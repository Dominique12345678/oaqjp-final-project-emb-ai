"""Flask web interface for emotion detection."""

import requests
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Analyze query parameter textToAnalyze and render a textual response."""
    text = request.args.get("textToAnalyze", "")
    if not text.strip():
        return "Invalid text! Please try again!"
    try:
        result = emotion_detector(text)
    except (requests.RequestException, KeyError, IndexError, ValueError):
        app.logger.exception("Unable to analyze the supplied text")
        return "Emotion detection service is unavailable. Please try again later!", 503
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


@app.route("/", methods=["GET"])
def render_index_page():
    """Render the application's home page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
